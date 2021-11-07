import Myself
from collections import deque
import kit.jsonE as jsonE
import kit.loggerM as loggerM
from pathlib import Path

banner = r"""  __  __      ___  
 |  \/  |_  _|   \ 
 | |\/| | || | |) |
 |_|  |_|\_, |___/ 
         |__/       made by Patrickuuuu
"""
print(banner)
Progress = Myself.Myself()
downloadList = []

@loggerM.ExceptionLog
def downloader():
    global downloadList
    preferance = jsonE.loadJson()
    url = input("Please enter URL(Domain by Myself): ")
    inf = Progress.informCatcher(url)
    """
    animeName: 
    description:
    episode:
    """
    print("動漫名稱: %s"%inf["animeName"])
    print("介紹: %s"%inf["description"])
    print("列表清單: ")
    _DownloadList = Progress.searchEpisode(inf["episode"])
    for _episode in _DownloadList:
        if _episode in downloadList: pass
        else: downloadList.append(_episode)
    
    if inf["animeName"] in preferance["AnimeFolder"]:
        print("使用資料夾名稱: %s"%preferance["AnimeFolder"][inf["animeName"]])
        _folderName = preferance["AnimeFolder"][inf["animeName"]]
    else:
        setName = True
        while setName:
            _folderName = input("請輸入下載資料夾名稱: ")
            if jsonE.modifyAnime(inf["animeName"], _folderName):
                print("成功設置資料夾名稱: %s"%_folderName)
                setName = False
            else:
                print("設置資料夾名稱失敗!")
    
    path = Path(preferance["Download"], _folderName)

    if not path.is_dir():
        print("創建資料夾中...")
        path.mkdir(parents=True, exist_ok=False)

    print("生成下載清單中...")
    queueDownload = Progress.downloadListGenerator(downloadList, path)
    downloadList = []
    print("下載清單建立完成!")
    print("開始分配排程...")
    Progress.mutipleDownload(queueDownload)
    print("end")


if __name__ == "__main__":
    while True:
        try: downloader()
        except KeyboardInterrupt: break
        except Exception as e: print(e)
    input("退出程式是否暫停全部下載")
    input("按下Enter鍵退出程式")
        

    
    


    