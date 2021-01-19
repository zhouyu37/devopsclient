#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import traceback
from lib.response import BaseResponse
from lib.logclass import logger
from .BasePlugin import BasePluginClass

class Disk(BasePluginClass):
    def win(self,handler,hostname):
        pass

    def linux(self,handler,hostname):
        response = BaseResponse()
        try:
            output = handler.cmd(command="/opt/MegaRAID/MegaCli/MegaCli64  -PDList -aALL",hostname=None)
            response.data = self.parse(output)
        except:
            msg = traceback.format_exc()
            response.status = False
            response.error = msg
            logger.error(msg)
        return response.dict
    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        response = {}
        result = []
        for row_line in content.split("\n\n\n\n"):
            result.append(row_line)
        for item in result:
            temp_dict = {}
            for row in item.split('\n'):
                if not row.strip():
                    continue
                if len(row.split(':')) != 2:
                    continue
                key, value = row.split(':')
                name = self.mega_patter_match(key)
                if name:
                    if key == 'Raw Size':
                        raw_size = re.search('(\d+\.\d+)', value.strip())
                        if raw_size:
                            temp_dict[name] = raw_size.group()
                        else:
                            raw_size = '0'
                    else:
                        temp_dict[name] = value.strip()
            if temp_dict:
                response[temp_dict['slot']] = temp_dict
        return response

    @staticmethod
    def mega_patter_match(needle):
        grep_pattern = {'Slot': 'slot', 'Raw Size': 'capacity', 'Inquiry': 'model', 'PD Type': 'pd_type'}
        for key, value in grep_pattern.items():
            if needle.startswith(key):
                return value
        return False
