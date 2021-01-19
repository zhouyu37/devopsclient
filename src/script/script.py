from config import settings
from lib.strtomod import StrToMod


def run():
    clspath=settings.HANDLER_TYPE_DICT[settings.HANDLER_TYPE]
    cls=StrToMod(clspath)
    obj=cls()
    obj.handler()



