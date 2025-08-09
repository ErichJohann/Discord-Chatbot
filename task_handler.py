import subprocess
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()
basedir = os.getenv('BASEPATH')

def scriptExc(op, arg):
    arg = arg.split(';')
    match op:
        case "1":
            return subprocess.run(['python', os.path.join(basedir, 'EventMaker', 'eventmaker.py'), arg[0]], timeout=60, cwd=os.path.join(basedir, 'EventMaker'))
        case "2":
            return subprocess.run(['python', os.path.join(basedir, 'Scheduler', 'scheduler.py'), arg[0]], timeout=60, cwd=os.path.join(basedir, 'Scheduler'))
        case "3":
            return subprocess.run(['python', os.path.join(basedir, 'Automail', 'Automail.py'), arg[0], arg[1]], timeout=60, cwd=os.path.join(basedir, 'Automail'))