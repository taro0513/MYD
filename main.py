import json
from os import popen
from pathlib import PurePath
from subprocess import Popen
import sys
import datetime

from PySide6 import QtWidgets
from PySide6.QtCore import QFile, QThread, Signal
from PySide6.QtGui import QIcon, QPixmap, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QCheckBox, QLabel, QListWidgetItem
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QPushButton
import tkinter as tk
from tkinter import filedialog


from main_func import *
from Myself import *
import base64
import requests
import io
from PIL import Image
import kit.jsonE as jsonE

def _image(_url):
    img_b64 = base64.b64encode(requests.get(_url).content)
    img_b64decode = base64.b64decode(img_b64)
    img_io = io.BytesIO(img_b64decode)
    return Image.open(img_io).toqpixmap()

class informationQ(QThread):
    resultInformation = Signal(dict)

    def information(self, id:str):
        detail = {}
        try:

            url = 'https://myself-bbs.com/forum.php?mod=viewthread&tid=%s'%id
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
                

            name = soup.find('meta', attrs={'name': 'keywords'}).get('content')
            detail.update({"name": "名稱: "+name})

            description = soup.find('div', id='info_introduction_text').string
            if description == None:
                description = soup.find_all('div', id='info_introduction_text')[0].text
            detail.update({"description": "介紹: "+description})

            picture = soup.find('div', {'class': 'info_img_box fl'}).img['src']
            detail.update({"picture": picture})

            _information = ['作品類型: ', '首播日期: ', '播出集數: ', '原著作者: ', '官方網站: ', '備注: ']
            _detail = []
            for _l in soup.find_all('div', {'class': 'info_info'}):
                for _i in zip(_information, _l.find_all('li')):
                    _detail.append(_i[0] + ' '.join(_i[1].text.split(' ')[1:]))        
            detail.update({"detail": _detail})

            name = []
            url = []
            for _name in soup.select('ul.main_list > li > a[href^="javascript:;"]'):
                name.append(_name.string)
            for _url in soup.select('li > a[href^="#"]'):
                if 'xfplay' in str(_url) : pass 
                elif 'vod' in str(_url) : pass 
                else: url.append(_url.get('data-href').replace('https://v.myself-bbs.com/player/play/','').strip())
            
            detail.update({"download": tuple(zip(name, url))})

            self.resultInformation.emit(detail)
        except:
            self.resultInformation.emit({})

class MyselfGUI(QMainWindow):
    def __init__(self, 
                 parent=None, 
                 login_file = r".\qml\Login.ui",
                 login_logo = r".\qml\logo.png",
                 close_logo = r".\qml\close.png",
                 main_file = r".\qml\Main.ui",
                 check_path_file = r".\qml\Path.ui"):
        super(MyselfGUI, self).__init__(parent)
        # self.login.setWindowFlags(Qt.CustomizeWindowHint)
        # self.login.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # self.login.setWindowFlags(Qt.WindowMaximizeButtonHint)
        self.Myself = Myself()
        self._login = QFile(login_file)
        self.login = QUiLoader().load(self._login)
        self._login.close()
        self.login.setWindowFlags(Qt.FramelessWindowHint)

        
        self._main = QFile(main_file)
        self.main = QUiLoader().load(self._main)
        self._main.close()
        self.main.setWindowFlags(Qt.FramelessWindowHint)

        self._check_path = QFile(check_path_file)
        self.check_path = QUiLoader().load(self._check_path)
        self._check_path.close()
        self.check_path.setWindowFlags(Qt.FramelessWindowHint)


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
        self.main.button_toggle.setIcon(QIcon(r".\qml\menu.png"))
        self.main.button_toggle.setText("")
        self.main.button_page_search.setIcon(QIcon(r".\qml\home.png"))
        self.main.button_page_search.setText("")
        self.main.button_page_schedule.setIcon(QIcon(r".\qml\download.png"))
        self.main.button_page_schedule.setText("")
        self.main.button_page_setting.setIcon(QIcon(r".\qml\setting.png"))
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
            self.login.loginSuggestion.setText("Please enter your account and password!")

        elif not _account:
            self.login.loginSuggestion.setVisible(True)
            self.login.loginSuggestion.setText("Please enter your account!")
        elif not _password:
            self.login.loginSuggestion.setVisible(True)
            self.login.loginSuggestion.setText("Please enter your password")

        else:
            if self._check_login(_account, _password):
                print(_account)
                print(_password)
                self._close_login()
                Myselfunctions.hint(self, "以 %s 身分登入!"%_account)
            else:
                self.login.loginSuggestion.setVisible(True)
                self.login.loginSuggestion.setText("Account or Password incorrect!")


    
    def _check_login(self, account, password):
        ...
    
    def _login_visitor(self):
        self._close_login()
        Myselfunctions.hint(self, "以訪客身分登入!")
    
    def _close_login(self):
        self.login.close()
        self.main.show()

    #[================login====================] END

    #[================Search===================]START
    def show_information(self, value:dict):
        if value:
            Myselfunctions.hint(self, "查詢結果-%s"%value["name"])
            self.search_show()
            self.main.search_listwidget_information.item(0).setText(value["name"])
            self.anime_name = value["name"]
            for num, _value in zip(range(1,7), value["detail"]):
                self.main.search_listwidget_information.item(num).setText(_value)
            self.main.search_listwidget_information.item(7).setText(value["description"])

            self._picture = QPixmap()
            self.main.search_picture.setPixmap(_image(value["picture"]))
            
            self.download_dictionary = {}
            for _object, _url in value["download"]:
                self.download_dictionary.update({_object: _url})
                box = QCheckBox(_object)
                item = QListWidgetItem()
                self.main.search_listwidget_all.addItem(item)
                self.main.search_listwidget_all.setItemWidget(item, box)

        else:
            Myselfunctions.hint(self, "查無結果! 請確認輸入是否正確.",level=Hint.hint_level_waring)

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
        Myselfunctions.hint(self, "搜尋 %s 中...") #!!!!!!!!!!!!!
        
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
        Myselfunctions.hint(self, "以選取目標: %s 項"%str(len(self._temp_downloadList)))
        
        self.path_folder()

    def get_all_information(self):
        self._temp_downloadList = []
        self._clear()
        self.count = self.main.search_listwidget_all.count()
        self.check_list = [self.main.search_listwidget_all.itemWidget(self.main.search_listwidget_all.item(i)) for i in range(self.count)]
        for _checkbox in self.check_list:
            key = _checkbox.text()
            self._temp_downloadList.append((key, self.download_dictionary[key]))
        Myselfunctions.hint(self, "以選取目標: %s 項"%str(len(self._temp_downloadList)))
        self.path_folder()

    #===============download-<mysel================
    def path_folder(self):
        _inf = jsonE.loadJson()
        self.check_path.name.setText(self.anime_name)
        self.check_path.path.setText("位置: "+_inf["Download"])
        if self.anime_name in _inf["AnimeFolder"]:
            self.check_path.folder_input.setText(_inf["AnimeFolder"][self.anime_name])
        else:
            self.check_path.folder_input.setText("")
        self.check_path.show()
    
    def set_folder(self):
        if self.check_path.folder_input.text():
            _path = self.check_path.folder_input.text().replace(" ","")
            jsonE.modifyAnime(self.anime_name, _path)
            self.folder = _path
            self.check_path.close()
            self.generate()
        else: 
            self.check_path.folder_input.setPlaceholderText("請輸入要新建的資料夾名稱!")

    def generate(self):
        Myselfunctions.hint(self, "建立下載清單中...")
        self._path = Path(jsonE.loadJson()["Download"], self.folder)
        self.downloadList = self.Myself.downloadListGenerator(self._temp_downloadList, self._path)
        for _path, _key in zip(self.downloadList, self._temp_downloadList):
            item = QListWidgetItem(QIcon("./qml/cil-arrow-bottom.png"), "%s - %s [%s]"%(self.anime_name, _key[0], "path: "+_path[1]))
            self.main.downloadlist.addItem(item)
        Myselfunctions.hint(self, "清單建立完成! 可至 '下載' 查看.")
        self.download()
        
    def download(self):
        if not Path(self._path).is_dir():
            Myselfunctions.hint(self, "創建資料夾 - %s 中..."%self._path)
            Path(self._path).mkdir(parents=True, exist_ok=True)
        
        Myselfunctions.hint(self, "%s 項 進入下載排程"%str(len(self.downloadList)))
        # self.Myself.mutipleDownload(self.downloadList)
    
    def setting_show(self):
        _inf = jsonE.loadJson()
        self.main.setting_label_Download.setText(_inf["Download"])
        self.main.setting_label_FFMPEG.setText(_inf["FFMPEG"])
        self.main.setting_label_DownloadLog.setText(_inf["MyselfLog"])
        self.main.setting_label_MyselfLog.setText(_inf["DownloadLog"])
        self.main.stackedWidget.setCurrentWidget(self.main.page_setting)
    
    def select_download(self):
        _path = jsonE.loadJson()["Download"]
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askdirectory()
        root.quit()
        if file_path:
            jsonE.modifyValue("Download", r"%s"%file_path)
            self.main.setting_label_Download.setText(file_path)
            Myselfunctions.hint(self, "更換路徑(download) %s -> %s"%(_path, file_path))
        else:
            pass
    def select_ffmpeg(self):
        _path = jsonE.loadJson()["FFMPEG"]
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        root.quit()
        if file_path:
            jsonE.modifyValue("FFMPEG", r"%s"%file_path)
            self.main.setting_label_FFMPEG.setText(file_path)
            Myselfunctions.hint(self, "更換路徑(ffmpeg) %s -> %s"%(_path, file_path))
        else:
            pass
    
    def open_myselfLog(self):
        folderPath = jsonE.loadJson()["MyselfLog"]
        _filename = datetime.now().strftime("[Myself]%Y-%m-%d.log")
        filename= Path(folderPath, _filename)
        Popen("notepad.exe %s"%str(filename))
        Myselfunctions.hint(self, "開啟檔案: %s"%str(filename))
    
    def open_downloadLog(self):
        folderPath = jsonE.loadJson()["DownloadLog"]
        filename = Path(folderPath, "Download.log")
        Popen("notepad.exe %s"%str(filename))
        Myselfunctions.hint(self, "開啟檔案: %s"%str(filename))
    
    def open_downadFile(self):
        location = self.main.downloadlist.selectedItems()[0].text()
        path = location.split("path:")[-1][:-1]
        Popen("explorer.exe %s"%str(PurePath(path).parents[0]))


    def close_(self):
        try: 
            self.login.close()
            self.check_path.close()
        except: pass
        self.Myself.close_()
        self.main.close()

if '__main__' == __name__:
    app = QtWidgets.QApplication(sys.argv)
    Application = MyselfGUI()
    Application.login.show()
    sys.exit(app.exec())    