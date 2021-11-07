
import requests
from requests.exceptions import ReadTimeout
from tqdm import tqdm
from datetime import datetime
from bs4 import BeautifulSoup
import subprocess
import kit.loggerM as loggerM
import threading
from pathlib import Path
import threading
import inspect
import ctypes
import time

"""
[Upgrade] inf_Cacher from Config -> json
"""

def _async_raise(tid, exctype):
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:

        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")

class MThread(threading.Thread):
    def _get_my_tid(self):
        if not self.is_alive():
            raise threading.ThreadError("the thread is not active")

        if hasattr(self, "_thread_id"):
            return self._thread_id
        
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid
        
        raise AssertionError("could not determine the thread's id")
    
    def raise_exc(self, exctype):
        _async_raise(self._get_my_tid(), exctype)
    
    def terminate(self):
        self.raise_exc(SystemExit)

class Myself:
    def __init__(self) -> None:
        self.thread = []
        
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
        page = requests.get(url)
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

        return {
                "animeName": animeName,
                "description": description,
                "episode": list(zip(episodeName, episodeUrl))
            }

    
    @classmethod
    @loggerM.ExceptionLog
    def serverCatcher(self, _id: str, _retry = 0) -> dict:
        """
        _id = ANIMENID/EPISODE
        return : {m3u8, priorityServer, -spareServer}
        """
        assert _retry < 3, "Server exceeded, please try again later !" 
        information =  eval(requests.get("https://v.myself-bbs.com/vpx/%s"%_id).text)

        serverList = []
        for server in tqdm(information["host"]):
            startTime = datetime.now()
            try: requests.get('%svpx/%s'%(server['host'], _id) ,timeout=(1.00, 1.00))
            except ReadTimeout: pass
            serverList.append((datetime.now()-startTime, server["host"]))
        
        if serverList:
            if len(serverList) >= 2:
                return {
                        "m3u8": information["video"]["720p"],
                        "priorityServer": serverList[0][1],
                        "priorityServerSpend": serverList[0][0],
                        "spareServer": serverList[1][1],
                        "spareServerSpend": serverList[1][0]
                    }
            else:
                return {
                        "m3u8": information["video"]["720p"],
                        "priorityServer": serverList[0][1],
                        "priorityServerSpend": serverList[0][0]
                    }
        else:
            return Myself.serverCatcher(_id, _retry+1)
    
    @classmethod
    @loggerM.ExceptionLog
    def fastServer(self, _id: str) -> dict:
        """
        _id = ANIMEID/EPISODE
        return : {m3u8, priorityServer, -spareServer}
        """
        information =  eval(requests.get("https://v.myself-bbs.com/vpx/%s"%_id).text)
        serverList = information["host"]
        if len(serverList) >= 2:
            return {
                    "m3u8": information["video"]["720p"],
                    "priorityServer": serverList[0]["host"],
                    "priorityServerSpend": None,
                    "spareServer": serverList[1]["host"],
                    "spareServerSpend": None
                }
        else:
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
        for _download in download:
            information =  eval(requests.get("https://v.myself-bbs.com/vpx/%s"%_download[1]).text)
            server = information["host"][0]["host"]
            m3u8 = information["video"]["720p"]
            downloadUrl = server + m3u8

            destination = str(Path(folder, "%s.mp4"%_download[0])).replace(" ", "")
            downloadList.append((downloadUrl, destination))
        
        return downloadList

    @classmethod
    @loggerM.ExceptionLog
    def searchEpisode(self, _list: list) -> list:
        """
        _list = [(name, id), ...]
        """
        for number, name in zip(range(len(_list)), _list):
            print("[%s] %s"%(number, name[0]))
        
        return tuple(
                    map(
                        lambda x: _list[int(x)], 
                        input("Please select the number of episodes: ").split(" ")
                    )
                )

    @classmethod
    @loggerM.ExceptionLog
    def download(self, url: str, destination: str, ffmpeg="ffmpeg.exe", log="log/download.log") -> None:
        """
        url = SERVER + ID + "/720p.m3u8"
        destination = DOWNLOADFOLDER + NAME + ".mp4"
        ffmpeg = FFMPEG
        log = LOG
        """
        cmd = "%s -i %s -c copy %s"%(ffmpeg, url, destination)
        subprocess.Popen(
                        cmd, 
                        stdout = open(log, 'a+'),
                        stderr = open(log, 'a+')
                    )
    
    @loggerM.ExceptionLog
    def mutipleDownload(self, downloadList, ffmpeg="ffmpeg.exe", log="log/download.log") -> None:
        for _download in downloadList:
            print("[Progress] adding thread! [%s]" %_download[1])
            self.thread.append(
                MThread(target= Myself.download, args=(_download[0], _download[1]))
            )
            self.thread[-1].start()

        for _download in self.thread:
            _download.join()

    def close_(self):
        self.__del__()
    
    def __del__(self):
        for _thread in self.thread:
            try:_thread.terminate()
            except:pass
        del self.thread
        

        

    
