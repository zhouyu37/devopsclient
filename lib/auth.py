#!/usr/bin/python
# -*- coding:utf-8 -*-
import hashlib
from config import settings

def gen_sign(ctime):
    val="%s|%s"%(settings.URL_AUTH_KEY,ctime)
    obj=hashlib.md5()
    obj.update(val.encode("utf-8"))
    return obj.hexdigest()


