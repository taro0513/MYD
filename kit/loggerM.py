import sys
import traceback
import logging
import datetime
from kit.jsonE import loadJson
from pathlib import Path

folderPath = loadJson()["MyselfLog"]

fileName = datetime.datetime.now().strftime("[Myself]%Y-%m-%d.log")

logging.basicConfig(
                    level=logging.INFO, 
                    filename= Path(folderPath, fileName), 
                    filemode='a+',
	                format='[%(levelname).1s %(asctime)s] %(message)s',
	                datefmt='%H:%M:%S'
                )

def ExceptionLog(func):
    def LogRegister(*args, **kwargs):
        try: return func(*args, **kwargs)
        except Exception as e:
            className = e.__class__.__name__
            detail = e.args[0]
            _, _, tb = sys.exc_info()
            callStack = traceback.extract_tb(tb)[-1]
            errorMessage = "File \"{}\", line {}, in {}: [{}] {}".format(callStack[0], callStack[1], callStack[2], className, detail)
            logging.warning(errorMessage)
            print("發生錯誤! 程式終止.")
            print(errorMessage)
            return None
            
    return LogRegister

        

