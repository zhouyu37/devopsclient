from Base import BaseClass

class SaltHandler(BaseClass):
    def cmd(self,hostname,command):
        import subprocess
        return subprocess.check_output(command)

    def handler(self):
        print("salt")