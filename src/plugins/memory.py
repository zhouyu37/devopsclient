#!/usr/bin/env python
# -*- coding:utf-8 -*-

import traceback
from lib.response import BaseResponse
from lib.logclass import logger
from .BasePlugin import BasePluginClass

class Mem(BasePluginClass):
    def win(self,handler,hostname):
        pass

    def linux(self,handler,hostname):
        response = BaseResponse()
        try:
            output = handler.cmd(command="sudo dmidecode  -q -t 17 2>/dev/null",hostname=None)
            response.data = self.parse(output)
        except:
            msg = traceback.format_exc()
            response.status = False
            response.error = msg
            logger.error(msg)
        for k,v in response.data.items():
            if  v['capacity'] == "No":
                del response.data[k]
        return response.dict

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        ram_dict = {}
        key_map = {
            'Size': 'capacity',
            'Locator': 'slot',
            'Type': 'model',
            'Speed': 'speed',
            'Manufacturer': 'manufacturer',
            'Serial Number': 'sn',
        }
        devices = content.split('Memory Device')
        for item in devices:
            item = item.strip()
            if not item:
                continue
            if item.startswith('#'):
                continue
            segment = {}
            lines = item.split('\n\t')
            for line in lines:
                if len(line.split(':')) > 1:
                    key, value = line.split(':')
                else:
                    key = line.split(':')[0]
                    value = ""
                if key in key_map:
                    if key == 'Size':
                        segment[key_map['Size']] = value.split()[0]
                    else:
                        segment[key_map[key.strip()]] = value.strip()
            ram_dict[segment['slot']] = segment

        return ram_dict

