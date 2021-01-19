#!/usr/bin/env python
# -*- coding:utf-8 -*-
import traceback
from lib.response import BaseResponse
from lib.logclass import logger
from .BasePlugin import BasePluginClass

class Basic(BasePluginClass):
    def os_platform(self,handler,hostname):
        output = handler.cmd(command='uname',hostname=None)
        return output.strip()

    def os_version(self,handler,hostname):
        output=handler.cmd(command='cat /etc/issue',hostname=None)
        result=output.strip().split('\n')[0]
        return result

    def os_hostname(self,handler,hostname):
        output = handler.cmd(command='hostname', hostname=None)
        return output.strip()

    def win(self,handler,hostname):
        pass

    def linux(self,handler,hostname):
        response=BaseResponse()
        try:
            ret = {
                'os_platform':self.os_platform(handler,hostname),
                'os_version':self.os_version(handler,hostname),
                'hostname':self.os_hostname(handler,hostname),
            }
            response.data=ret
        except:
            msg=traceback.format_exc()
            response.status=False
            response.error=msg
            logger.error(msg)

        return response.dict




