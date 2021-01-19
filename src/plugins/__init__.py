from config import settings
from lib.strtomod import StrToMod

def get_server_info(handler,hostname=None):
    info = {}
    for key,infopath in settings.SERVER_INFO_DICT.items():
        cls=StrToMod(infopath)
        obj=cls()
        info[key]=obj.process(handler,hostname=None)
    return info
