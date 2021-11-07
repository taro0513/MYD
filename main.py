from subprocess import Popen
from os import system
import sys
import datetime
import requests
from requests import get
from bs4 import BeautifulSoup

from datetime import datetime
from pathlib import Path, PurePath
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtCore import QFile, QObject, QPropertyAnimation, QThread, Signal
from PySide6.QtGui import QIcon, QPixmap, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QCheckBox, QListWidgetItem
from PySide6.QtWidgets import QMainWindow
from tkinter import Tk, filedialog
from base64 import b64encode, b64decode

from io import BytesIO
from PIL import Image

import threading
import inspect
import ctypes

import jsonE as jsonE
import loggerM as loggerM
from Suggest import em, ctx, hm
from params import dp

def _async_raise(tid, exctype):
    if not inspect.isclass(exctype):
        raise TypeError(em.async_inspect_not_inclasss)
    
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exctype))
    
    if res == 0:
        raise ValueError(em.async_invalid_thread_id)
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError(em.async_set_failed)

class MThread(threading.Thread):
    def _get_my_tid(self):
        if not self.is_alive():
            raise threading.ThreadError(em.thread_not_active)

        if hasattr(self, "_thread_id"):
            return self._thread_id
        
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid
        raise AssertionError(em.thread_cant_determin)
    
    def raise_exc(self, exctype):
        _async_raise(self._get_my_tid(), exctype)
    
    def terminate(self):
        self.raise_exc(SystemExit)


class Myself(QObject):
    QdownloadList = Signal(list)

    @loggerM.ExceptionLog
    def set_Path(self, path: str) -> None:
        ...
    @loggerM.ExceptionLog
    def set_Folder(self, name: str) -> None:
        ...        
    
    @classmethod
    @loggerM.ExceptionLog
    def informCatcher(self, url: str) -> dict:
        """
        url : "https://myself-bbs.com/" + Characterization 
        return : {animeName, description, episode:[(episodeName, episodeUrl), ...]}
        """
        page = get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        episodeName = []
        episodeUrl = []
        animeName = soup.find('meta', attrs={'name':'keywords'}).get('content')
        description = soup.find('div', id='info_introduction_text').string

        for name in soup.select('ul.main_list > li > a[href^="javascript:;"]'):
            episodeName.append(name.string)

        for url in soup.select('li > a[href^="#"]'):
            if 'xfplay' not in str(url): 
                episodeUrl.append(url.get('data-href').replace('https://v.myself-bbs.com/player/play/','').strip())

        loggerM.logging.info(
            ctx.catcher_information%(animeName, description, ','.join(episodeName))
        )
        return {
                "animeName": animeName,
                "description": description,
                "episode": list(zip(episodeName, episodeUrl))
            }

    @loggerM.ExceptionLog
    def _connect_server(self, domain: str, params: str):
        loggerM.logging.info(ctx.connect_server%(domain, params))
        try:
            _startTime = datetime.now()
            _ip = dp.m3u8_url%(domain, params)
            get(_ip ,timeout=(float(dp.server_connecttimeout),float(dp.server_readtimeout)))
            _timeConsuming = datetime.now()-_startTime
            self.serverList.append( (_timeConsuming, domain) )
            loggerM.logging.info(ctx.connect_server_success%str(_timeConsuming))
        except Exception as e:
            _timeConsuming = datetime.now()-_startTime
            loggerM.logging.info(ctx.connect_server_failed%str(_timeConsuming))
            loggerM.logging.info(em.warning_detail%e)

    @classmethod
    @loggerM.ExceptionLog
    def serverCatcher(self, params: str, _retry = 0) -> dict:
        """
        params = ANIMENID/EPISODE
        return : {m3u8, priorityServer, -spareServer}
        """
        self.Qthread = []
        self.serverList = []
        assert _retry < dp.connect_exceed, ctx.connect_exceed

        information =  eval(get(dp.vpx_url%params).text)
        
        for server in information["host"]:
            self.Qthread.append(
                MThread(target= self._connect_server, args=(self, server['host'], params))
            )
            self.Qthread[-1].start()    
            
        for _thread in self.Qthread:
            _thread.join()
        

        if self.serverList:
            serverList = sorted(self.serverList)
            
            if len(serverList) >= 2:
                loggerM.logging.info(ctx.connect_best_spare%(information["video"]["720p"], 
                                                       serverList[0][1], 
                                                       serverList[0][0],
                                                       serverList[1][1],
                                                       serverList[1][0]))
                return {
                        "m3u8": information["video"]["720p"],
                        "priorityServer": serverList[0][1],
                        "priorityServerSpend": serverList[0][0],
                        "spareServer": serverList[1][1],
                        "spareServerSpend": serverList[1][0]
                    }
            else:
                loggerM.logging.info(ctx.connect_best%(information["video"]["720p"], 
                                                       serverList[0][1], 
                                                       serverList[0][0]))
                return {
                        "m3u8": information["video"]["720p"],
                        "priorityServer": serverList[0][1],
                        "priorityServerSpend": serverList[0][0]
                    }
        else:
            loggerM.logging.warning(ctx.connect_retry%(_retry))
            return Myself.serverCatcher(params, _retry+1)
    
    @classmethod
    @loggerM.ExceptionLog
    def fastServer(self, params: str) -> dict:
        """
        _id = ANIMEID/EPISODE
        return : {m3u8, priorityServer, -spareServer}
        """
        information =  eval(get(dp.vpx_url%params).text)
        serverList = information["host"]

        if len(serverList) >= 2:
            loggerM.logging.info(ctx.connect_fast_best_spare%(information["video"]["720p"],
                                                              serverList[0]["host"],
                                                              serverList[1]["host"]))
            return {
                    "m3u8": information["video"]["720p"],
                    "priorityServer": serverList[0]["host"],
                    "priorityServerSpend": None,
                    "spareServer": serverList[1]["host"],
                    "spareServerSpend": None
                }
        else:
            loggerM.logging.info(ctx.connect_fast_best_spare%(information["video"]["720p"],
                                                              serverList[0]["host"]))
            return {
                    "m3u8": information["video"]["720p"],
                    "priorityServer": serverList[0]["host"],
                    "priorityServerSpend": None
                }
    
    @classmethod
    @loggerM.ExceptionLog
    def downloadListGenerator(self, download, folder: str) -> list:
        """
        download : [(Name, Url), ...]
        return : [(downloadUrl, destination), ...]
        """
        downloadList = []
        loggerM.logging.info(ctx.download_list_generate%len(download))
        
        for _download in download:
            information = Myself.serverCatcher(_download[1])
            server = information["priorityServer"]
            m3u8 = information["m3u8"]
            downloadUrl = server + m3u8
            destination = str(Path(folder, dp.download_name%_download[0])).replace(" ", "")
            downloadList.append((downloadUrl, destination))
            loggerM.logging.info(ctx.download_list_add%(downloadUrl, destination))
        
        return downloadList

    @classmethod
    @loggerM.ExceptionLog
    def searchEpisode(self, _list: list) -> list:
        """
        _list = [(name, id), ...]
        """
        for number, name in zip(range(len(_list)), _list):
            print(ctx.select_slection%(number, name[0]))
        
        return tuple(
                    map(
                        lambda x: _list[int(x)], 
                        input(ctx.select_input).split(" ")
                    )
                )

    @classmethod
    @loggerM.ExceptionLog
    def download(self, url: str, destination: str) -> None:
        """
        url = SERVER + ID + "/720p.m3u8"
        destination = DOWNLOADFOLDER + NAME + ".mp4"
        ffmpeg = FFMPEG
        log = LOG
        """
        information = jsonE.loadJson()
        ffmpeg = information[dp.jffmpeg]
        log = Path(information[dp.jdownloadlog], "Download.log")

        loggerM.logging.info(ctx.download_check_ffmpeg%ffmpeg)

        if Path(ffmpeg).is_file():
            loggerM.logging.info(ctx.download_check_ffmpeg_success)
        else:
            loggerM.logging.error(ctx.download_check_ffmpeg_failed)
            return False
        
        if not log.is_file():
            log.touch()
            loggerM.logging.warning(ctx.download_check_log_failed%log)

        cmd = dp.download_cmd%(ffmpeg, url, destination)

        loggerM.logging.warning(ctx.download_excute_cmd%cmd)
        try:
            Popen(
                            cmd,
                            shell = True,
                            stdout = open(log, 'a+'),
                            stderr = open(log, 'a+')
                        )
        except:
            system("start %s"%cmd)
        
    @loggerM.ExceptionLog
    def mutipleDownload(self, downloadList) -> None:
        for _download in downloadList:
            Myself.download(_download[0], _download[1])
            loggerM.logging.info(ctx.download_excute_add%(_download[0], _download[1]))
        

class Hint:
    hint_level_normal = """
    <html><head/><body><p><span style=" color:#ffffff;">%s</span></p></body></html>
    """
    hint_level_waring = """
    <html><head/><body><p><span style=" color:#ff3c3c;">%s</span></p></body></html>
    """


def _image(_url):
    img_b64 = b64encode(requests.get(_url).content)
    img_b64decode = b64decode(img_b64)
    img_io = BytesIO(img_b64decode)
    return Image.open(img_io).toqpixmap()

class informationQ(QThread):
    resultInformation = Signal(dict)

    def information(self, params:str):
        detail = {}
        try:
            url = 'https://myself-bbs.com/forum.php?mod=viewthread&tid=%s'%params
            loggerM.logging.info(ctx.search_key%params)

            soup = BeautifulSoup(requests.get(url).text, 'html.parser')

            name = soup.find('meta', attrs={'name': 'keywords'}).get('content')
            detail.update({"name": "名稱: "+name})
            description = soup.find('div', id='info_introduction_text').string
            if description == None:
                description = soup.find_all('div', id='info_introduction_text')[0].text
            detail.update({"description": "介紹: "+description})
            picture = soup.find('div', {'class': 'info_img_box fl'}).img['src']
            detail.update({"picture": picture})

            loggerM.logging.info(ctx.search_result_name%name)
            loggerM.logging.info(ctx.search_result_description%description)
            loggerM.logging.info(ctx.search_result_picture%picture)

            _information = ['作品類型: ', '首播日期: ', '播出集數: ', '原著作者: ', '官方網站: ', '備注: ']
            _detail = []
            for _l in soup.find_all('div', {'class': 'info_info'}):
                for _i in zip(_information, _l.find_all('li')):
                    _detail.append(_i[0] + ' '.join(_i[1].text.split(' ')[1:]))
                    loggerM.logging.info(ctx.search_result_detail%(_i[0], ' '.join(_i[1].text.split(' ')[1:])))
            detail.update({"detail": _detail})

            name = []
            url = []
            for _name in soup.select('ul.main_list > li > a[href^="javascript:;"]'):
                name.append(_name.string)
            for _url in soup.select('li > a[href^="#"]'):
                if 'xfplay' in str(_url) : 
                    loggerM.logging.warning(ctx.search_xfplay_skip%_url)
                elif 'vod' in str(_url) : 
                    loggerM.logging.warning(ctx.search_vod_skip%_url)
                else: 
                    url.append(_url.get('data-href').replace('https://v.myself-bbs.com/player/play/','').strip())
            
            detail.update({"download": tuple(zip(name, url))})

            self.resultInformation.emit(detail)
        except:
            loggerM.logging.error(ctx.search_no_inforamtion%params)
            self.resultInformation.emit({})

class MyselfGUI(QMainWindow):
    def __init__(self, 
                 parent=None, 
                 login_file = r".\attach\UI_Login.ui",
                 login_logo = r".\attach\logo.png",
                 main_file = r".\attach\UI_Main.ui",
                 check_path_file = r".\attach\UI_Path.ui"):
        super(MyselfGUI, self).__init__(parent)
        self._login = QFile(login_file)
        self.login = QUiLoader().load(self._login)
        self._login.close()
        self.login.setWindowTitle("登入")
        # self.login.setWindowFlags(Qt.FramelessWindowHint)

        
        self._main = QFile(main_file)
        self.main = QUiLoader().load(self._main)
        self._main.close()
        self.main.setWindowTitle("MyselfDownloader")
        
        # self.main.setWindowFlags(Qt.FramelessWindowHint)

        self._check_path = QFile(check_path_file)
        self.check_path = QUiLoader().load(self._check_path)
        self._check_path.close()
        self.check_path.setWindowTitle("確認資料夾名稱")
        # self.check_path.setWindowFlags(Qt.FramelessWindowHint)


        self._login_logo = QPixmap(login_logo)
        self.login.logo.setPixmap(self._login_logo)
        self.login.logo.setScaledContents(True)

        self.login.loginAccount.clicked.connect(self._login_account)
        self.login.loginVisitor.clicked.connect(self._login_visitor)

        self.button_setting()
        self.search_hide()

        self.main.search_listwidget_information.setWordWrap(True)
        #=========================================
        self.main.button_toggle.clicked.connect(lambda: Myselfunctions.toggleMenu(self))
        self.main.button_page_search.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.page_search))
        self.main.button_page_schedule.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.page_schedule))
        self.main.button_page_setting.clicked.connect(self.setting_show)
        self.main.search_button.clicked.connect(self.search)
        self.main.search_download_all.clicked.connect(self.get_all_information)
        self.main.search_download_select.clicked.connect(self.get_selct_information)
        self.check_path.confirm.clicked.connect(self.set_folder)
        self.check_path.cancel.clicked.connect(self.check_path.close)
        self.main.setting_button_Download.clicked.connect(self.select_download)
        self.main.setting_button_FFMPEG.clicked.connect(self.select_ffmpeg)
        self.main.setting_button_DownloadLog.clicked.connect(self.open_downloadLog)
        self.main.setting_button_MyselfLog.clicked.connect(self.open_myselfLog)
        self.main.downloadlist.itemDoubleClicked.connect(self.open_downadFile)
        self.main.button_exit.clicked.connect(self.close_)
        #=========================================

    def button_setting(self):
        self.main.button_toggle.setIcon(QIcon(r".\attach\Icon_menu.png"))
        self.main.button_toggle.setText("")
        self.main.button_page_search.setIcon(QIcon(r".\attach\Icon_home.png"))
        self.main.button_page_search.setText("")
        self.main.button_page_schedule.setIcon(QIcon(r".\attach\Icon_dl.png"))
        self.main.button_page_schedule.setText("")
        self.main.button_page_setting.setIcon(QIcon(r".\attach\Icon_setting.png"))
        self.main.button_page_setting.setText("")

    def search_hide(self):
        self.main.search_listwidget_information.hide()
        self.main.search_picture.hide()
        self.main.search_listwidget_all.hide()
        self.main.search_download_select.hide()
        self.main.search_download_all.hide()
        self.main.downloadlist.hide()

    def search_show(self):
        self.main.search_listwidget_information.show()
        self.main.search_picture.show()
        self.main.search_listwidget_all.show()
        self.main.search_download_select.show()
        self.main.search_download_all.show()
        self.main.downloadlist.show()

    #[================login====================]START
    def _login_account(self):
        self.login.loginSuggestion.setVisible(False)
        _account = self.login.Account.text()
        _password = self.login.Password.text()

        
        if (not _account) and (not _password):
            self.login.loginSuggestion.setVisible(True)
            self.login.loginSuggestion.setText(hm.login_no_enter)

        elif not _account:
            self.login.loginSuggestion.setVisible(True)
            self.login.loginSuggestion.setText(hm.login_no_enter_account)
        elif not _password:
            self.login.loginSuggestion.setVisible(True)
            self.login.loginSuggestion.setText(hm.login_no_enter_password)

        else:
            if self._check_login(_account, _password):
                self._close_login()
                Myselfunctions.hint(self, hm.login_account%_account)
            else:
                self.login.loginSuggestion.setVisible(True)
                self.login.loginSuggestion.setText(hm.login_incorrect)

    def _check_login(self, account, password):
        self.login.loginSuggestion.setVisible(True)
        self.login.loginSuggestion.setText(hm.login_not_open)
        return False

    def _login_visitor(self):
        self._close_login()
        Myselfunctions.hint(self, hm.login_visitor)
    
    def _close_login(self):
        self.login.close()
        self.main.show()

    #[================login====================] END

    #[================Search===================]START
    def show_information(self, value:dict):
        if value:
            Myselfunctions.hint(self, hm.search_result%value["name"])

            self.search_show()

            self.main.search_listwidget_information.item(0).setText(value["name"])
            self.anime_name = value["name"]
            loggerM.logging.info(hm.log_set_item%value["name"])

            for num, _value in zip(range(1,7), value["detail"]):
                self.main.search_listwidget_information.item(num).setText(_value)
                loggerM.logging.info(hm.log_set_item%_value)

            self.main.search_listwidget_information.item(7).setText(value["description"])
            loggerM.logging.info(hm.log_set_item%value["description"])

            self._picture = QPixmap()
            self.main.search_picture.setPixmap(_image(value["picture"]))
            loggerM.logging.info(hm.log_set_item%value["picture"])

            self.download_dictionary = {}
            for _object, _url in value["download"]:
                self.download_dictionary.update({_object: _url})
                box = QCheckBox(_object)
                item = QListWidgetItem()
                self.main.search_listwidget_all.addItem(item)
                self.main.search_listwidget_all.setItemWidget(item, box)

        else:
            Myselfunctions.hint(self, hm.search_no_result, level=Hint.hint_level_waring)

    def _get_information(self, _id:str):
        self._information = informationQ()
        self._information.resultInformation.connect(self.show_information)
        self._information.information(_id)

    def _clear(self, dictionary = False):
        self.count = 0
        self.check_list = []
        if dictionary:
            self.download_dictionary = {}
    
    def search(self):
        self._clear()
        self.main.search_listwidget_all.clear()
        _search_key = self.main.search_input.text()
        Myselfunctions.hint(self, hm.search%_search_key)
        
        self.main.search_input.setText("")
        _id = _search_key.replace("https://myself-bbs.com/thread-", "")[:5]
        self._get_information(_id)

    #[]===================download=========================]
    

    def get_selct_information(self):
        self._temp_downloadList = []
        self._clear()
        self.count = self.main.search_listwidget_all.count()
        self.check_list = [self.main.search_listwidget_all.itemWidget(self.main.search_listwidget_all.item(i)) for i in range(self.count)]
        for _checkbox in self.check_list:
            if _checkbox.isChecked():
                key = _checkbox.text()
                self._temp_downloadList.append((key, self.download_dictionary[key]))
        Myselfunctions.hint(self, hm.select_count%len(self._temp_downloadList))
        
        self.path_folder()

    def get_all_information(self):
        self._temp_downloadList = []
        self._clear()
        self.count = self.main.search_listwidget_all.count()
        self.check_list = [self.main.search_listwidget_all.itemWidget(self.main.search_listwidget_all.item(i)) for i in range(self.count)]
        for _checkbox in self.check_list:
            key = _checkbox.text()
            self._temp_downloadList.append((key, self.download_dictionary[key]))
        Myselfunctions.hint(self, hm.select_count%len(self._temp_downloadList))
        self.path_folder()

    #===============download-<mysel================
    def path_folder(self):
        _inf = jsonE.loadJson()
        self.check_path.name.setText(self.anime_name)
        self.check_path.path.setText(hm.check_path_path%_inf["Download"])
        if self.anime_name in _inf["AnimeFolder"]:
            self.check_path.folder_input.setText(_inf["AnimeFolder"][self.anime_name])
        else:
            self.check_path.folder_input.setText("")
        self.check_path.show()
    
    def set_folder(self):
        if self.check_path.folder_input.text():
            _path = self.check_path.folder_input.text().replace(" ","")
            jsonE.modifyAnime(self.anime_name, _path)
            Myselfunctions.hint(self, hm.setting_folder%(_path, self.anime_name))
            self.folder = _path
            self.check_path.close()
            self._generate()
        else: 
            self.check_path.folder_input.setPlaceholderText(hm.setting_folder_no_input)

    def _generate(self):
        Myselfunctions.hint(self, hm.download_list_generate)
        self._path = Path(jsonE.loadJson()["Download"], self.folder)
        self.Qdlg = Myself()
        self.generate(self.Qdlg.downloadListGenerator(self._temp_downloadList, self._path))

    def generate(self, downloadList):
        self.downloadList = downloadList
        for _path, _key in zip(self.downloadList, self._temp_downloadList):
            item = QListWidgetItem(QIcon("./attach/Icon_dl_file.png"), "%s - %s [path:%s]"%(self.anime_name, _key[0], _path[1]))
            self.main.downloadlist.addItem(item)

        loggerM.logging.info(ctx.download_list_end)
        Myselfunctions.hint(self, hm.download_list_end)
        self.download()
        
    def download(self):
        if not Path(self._path).is_dir():
            Path(self._path).mkdir(parents=True, exist_ok=True)
            Myselfunctions.hint(self, ctx.download_check_folder_failed%self._path)
            loggerM.logging.logging.warn(ctx.download_check_folder_fialed%self.path)
        
        Myselfunctions.hint(self, hm.download_queue_enter%(len(self.downloadList)))
        self.Qdlg.mutipleDownload(self.downloadList)
    
    def setting_show(self):
        _inf = jsonE.loadJson()
        self.main.setting_label_Download.setText(_inf["Download"])
        self.main.setting_label_FFMPEG.setText(_inf["FFMPEG"])
        self.main.setting_label_DownloadLog.setText(_inf["MyselfLog"])
        self.main.setting_label_MyselfLog.setText(_inf["DownloadLog"])
        self.main.stackedWidget.setCurrentWidget(self.main.page_setting)
    
    def select_download(self):
        _path = jsonE.loadJson()["Download"]
        root = Tk()
        root.withdraw()
        file_path = filedialog.askdirectory()
        root.quit()
        if file_path:
            jsonE.modifyValue("Download", r"%s"%file_path)
            self.main.setting_label_Download.setText(file_path)
            Myselfunctions.hint(self, hm.change_path_download%(_path, file_path))
        else:
            Myselfunctions.hint(self, em.cancel_action, Hint.hint_level_waring)
    def select_ffmpeg(self):
        _path = jsonE.loadJson()["FFMPEG"]
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        root.quit()
        if file_path:
            jsonE.modifyValue("FFMPEG", r"%s"%file_path)
            self.main.setting_label_FFMPEG.setText(file_path)
            Myselfunctions.hint(self, hm.change_path_ffmpeg%(_path, file_path))
        else:
            Myselfunctions.hint(self, em.cancel_action, Hint.hint_level_waring)
    
    def open_myselfLog(self):
        folderPath = jsonE.loadJson()["MyselfLog"]
        _filename = datetime.now().strftime("[Myself]%Y-%m-%d.log")
        filename= Path(folderPath, _filename)
        Popen("notepad.exe %s"%str(filename))
        Myselfunctions.hint(self, hm.open_file%str(filename))
    
    def open_downloadLog(self):
        folderPath = jsonE.loadJson()["DownloadLog"]
        filename = Path(folderPath, "Download.log")
        Popen("notepad.exe %s"%str(filename))
        Myselfunctions.hint(self, hm.open_file%str(filename))
    
    def open_downadFile(self):
        location = self.main.downloadlist.selectedItems()[0].text()
        path = location.split("path:")[-1][:-1]
        Myselfunctions.hint(self, hm.open_folder%str(PurePath(path).parents[0]))
        Popen("explorer.exe %s"%str(PurePath(path).parents[0]))

    def close_(self):
        try: 
            self.login.close()
            self.check_path.close()
        except: pass
        self.main.close()

class Myselfunctions(MyselfGUI):
    
    def toggleMenu(self, maxWidth=200, enable=True, standard:int = 70):
        if enable:
            width = self.main.frame_left_menu.width()
            widthExtend = maxWidth if width == standard else standard
            if width == standard:
                widthExtend = maxWidth
                self.main.button_page_search.setText("主頁")
                self.main.button_page_schedule.setText("下載")
                self.main.button_page_setting.setText("設定")
            else:
                widthExtend = standard
                self.main.button_toggle.setText("")
                self.main.button_page_search.setText("")
                self.main.button_page_schedule.setText("")
                self.main.button_page_setting.setText("")


            self.animation = QPropertyAnimation(self.main.frame_left_menu, b'minimumWidth')
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
    
    def hint(self, hint:str, level=Hint.hint_level_normal) -> None:
        self.main.hintbox.setText(level%hint)

if '__main__' == __name__:
    app = QtWidgets.QApplication(sys.argv)
    Application = MyselfGUI()
    Application.login.show()
    sys.exit(app.exec())    