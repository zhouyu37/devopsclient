import logging
from config import settings

log_file=settings.LOG_FILE_PATH

class Logger(object):
    def __init__(self):
        file_handler = logging.FileHandler(log_file,'a',encoding='utf-8')
        file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s-%(name)s-%(levelname)s-%(module)s: %(message)s"))

        self.logger=logging.Logger('root',level=logging.INFO)
        self.logger.addHandler(file_handler)

    def info(self,msg):
        self.logger.info(msg)

    def error(self,msg):
        self.logger.error(msg)

logger = Logger()


