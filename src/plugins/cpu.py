#!/usr/bin/env python
# -*- coding:utf-8 -*-

import traceback
from lib.response import BaseResponse
from lib.logclass import logger
from .BasePlugin import BasePluginClass

class Cpu(BasePluginClass):
    def win(self,handler,hostname):
        pass

    def linux(self,handler,hostname):
        response = BaseResponse()
        try:
            output=handler.cmd(command="cat /proc/cpuinfo",hostname=None)
            response.data=self.parse(output)
        except:
            msg = traceback.format_exc()
            response.status = False
            response.error = msg
            logger.error(msg)
        return response.dict

    @staticmethod
    def parse(content):
        response = {'cpu_count':0,'cpu_physical_count':0,'cpu_model':''}
        cpu_physical_set = set()

        content=content.strip()
        for item in content.split('\n\n'):
            for row_line in item.split('\n'):
                key, value = row_line.split(':')
                key = key.strip()
                if key == 'processor':
                    response['cpu_count'] += 1
                elif key == 'physical id':
                    cpu_physical_set.add(value)
                elif key == 'model name':
                    if not response['cpu_model']:
                        response['cpu_model'] = value
        response['cpu_physical_count'] = len(cpu_physical_set)

        return response
