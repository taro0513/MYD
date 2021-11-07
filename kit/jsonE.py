import json
import copy
path = "./setting.json"

def loadJson(path: str=path) -> dict:
    with open(path, mode='r', encoding='utf-8') as _file:
        preference = json.load(_file)
    return preference


def modifyValue(key: str, value: str, path: str=path) -> None:
    _json = loadJson(path)
    _copy_json = copy.deepcopy(_json)
    _json.update({key: value})
    
    with open(path, mode = "w", encoding="utf-8") as _file:
        try: json.dump(_json, _file, indent=4)
        except Exception as e:
            json.dump(_copy_json, _file, indent=4)
            print(e)
            return False
    return value


def modifyAnime(key: str, value: str, path: str=path) -> None:
    _json = loadJson(path)
    _copy_json = copy.deepcopy(_json)
    _json["AnimeFolder"].update({key: value})
    
    with open(path, mode = "w", encoding="utf-8") as _file:
        try: json.dump(_json, _file, indent=4)
        except Exception as e:
            json.dump(_copy_json, _file, indent=4)
            print(e)
            return False
    return value

        

