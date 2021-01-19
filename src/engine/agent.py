from Base import BaseClass
from src.plugins import get_server_info
import os
import requests
import time
import json
from config import settings

from lib.auth import gen_sign
from lib.security import encrypt

class AgentHandler(BaseClass):
    def cmd(self,hostname=None,command=None):
        # import subprocess
        # return subprocess.check_output(command)
	    import commands
	    status, output = commands.getstatusoutput(command)
	    return  output

    def handler(self):
        info = get_server_info(self)

        if not os.path.exists(settings.CERT_FILE_PATH):
            info['type'] = 'create'
        else:
            with open(settings.CERT_FILE_PATH,'r') as f:
                cert=f.read()
                print("yu111",cert)
                print("yu222",info['basic']['data']['hostname'])
            if str(cert) == info['basic']['data']['hostname']:
                info['type'] = 'update'
            else:
                info['cert'] = cert
                info['type'] = 'host_update'
        print(info)
        ctime = int(time.time() * 1000)
        r1 = requests.post(
            url=self.asset_api,
            params={"sign": gen_sign(ctime), "ctime": ctime},
            data=encrypt(json.dumps(info).encode("utf-8")),
            headers={
                'Content-Type': 'application/json'
            }
        )
        response = r1.json()
        if response['status']:
            with open(settings.CERT_FILE_PATH, 'w') as f:
                f.write(response['data'])


