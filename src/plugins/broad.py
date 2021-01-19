#!/usr/bin/env python
# -*- coding:utf-8 -*-

import traceback
from lib.response import BaseResponse
from lib.logclass import logger
from .BasePlugin import BasePluginClass

class MainBoard(BasePluginClass):
    def win(self,handler,hostname):
        pass

    def linux(self,handler,hostname):
        response = BaseResponse()
        try:
            output = handler.cmd(command="sudo dmidecode -t1", hostname=None)
            response.data = self.parse(output)
        except Exception as e:
            msg = traceback.format_exc()
            response.status = False
            response.error = msg
            logger.error(msg)
        return response.dict

    def parse(self, content):

        result = {}
        key_map = {
            'Manufacturer': 'manufacturer',
            'Product Name': 'model',
            'Serial Number': 'sn',
        }

        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data) == 2:
                if row_data[0] in key_map:
                    result[key_map[row_data[0]]] = row_data[1].strip() if row_data[1] else row_data[1]

        return result