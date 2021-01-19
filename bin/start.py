import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from src.script.script import run
if __name__ == "__main__":
    run()
