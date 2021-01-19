from config import settings

class BaseClass(object):
    def __init__(self):
        self.asset_api=settings.ASSET_API

    def cmd(self,hostname=None,command=None):
        raise NotImplementedError("cmd must be implemented")

    def handler(self):
        raise NotImplementedError("handler must be implemented")
