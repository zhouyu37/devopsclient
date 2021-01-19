from config import settings

class BasePluginClass(object):
    def __init__(self):
        self.base_dir = settings.BASEDIR

    def get_os(self,handler,hostname):
        return "linux"

    def process(self,handler,hostname):
        os = self.get_os(handler,hostname)
        if os == "linux":
            return self.linux(handler,hostname)
        else:
            return self.win(handler,hostname)

    def win(self,handler,hostname):
        raise NotImplementedError("win method must be existed")

    def linux(self,handler,hostname):
        raise NotImplementedError("linux method must be existed")