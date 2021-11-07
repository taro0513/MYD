from json import load, dump
from copy import deepcopy
path = "./setting.json"

def loadJson(path: str=path) -> dict:
    with open(path, mode='r', encoding='utf-8') as _file:
        preference = load(_file)
    return preference


def modifyValue(key: str, value: str, path: str=path) -> None:
    _json = loadJson(path)
    _copy_json = deepcopy(_json)
    _json.update({key: value})
    
    with open(path, mode = "w", encoding="utf-8") as _file:
        try: dump(_json, _file, indent=4)
        except Exception as e:
            dump(_copy_json, _file, indent=4)
            print(e)
            return False
    return value


def modifyAnime(key: str, value: str, path: str=path) -> None:
    _json = loadJson(path)
    _copy_json = deepcopy(_json)
    _json["AnimeFolder"].update({key: value})
    
    with open(path, mode = "w", encoding="utf-8") as _file:
        try: dump(_json, _file, indent=4)
        except Exception as e:
            dump(_copy_json, _file, indent=4)
            return False
    return value

        

