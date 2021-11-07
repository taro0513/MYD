import sys
from traceback import extract_tb
import logging
from datetime import datetime
from jsonE import loadJson
from pathlib import Path
from params import dp

folderPath = loadJson()["MyselfLog"]
fileName = datetime.now().strftime("[Myself]%Y-%m-%d.log")

logging.basicConfig(
                    level=dp.level, 
                    filename= Path(folderPath, fileName), 
                    filemode='a+',
	                format='[%(levelname).1s %(asctime)s] %(message)s',
	                datefmt='%H:%M:%S'
                )

def ExceptionLog(func):
    def LogRegister(*args, **kwargs):
        try: 
            return func(*args, **kwargs)
        except Exception as e:
            className = e.__class__.__name__
            detail = e.args[0]
            _, _, tb = sys.exc_info()
            callStack = extract_tb(tb)[-1]
            errorMessage = "File \"{}\", line {}, in {}: [{}] {}".format(callStack[0], callStack[1], callStack[2], className, detail)
            logging.warning(errorMessage)
            return None
            
    return LogRegister

        

