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
            return """Lista de scripts possíveis:
                        eventmaker.py [nome da planilha] -  Lê eventos de uma planilha do googlesheets e os cria no google calendar
                        scheduler.py [arquivo de eventos csv] - Lê de um arquivo .csv eventos e os cria no google calendar
                        automail.py [arquivo de endereços de email csv] [arquivo com mensagem txt] - Manda uma mensagem de um .txt para vários endereços de email"""
        case "2":
            return subprocess.run(['python', os.path.join(basedir, 'EventMaker', 'eventmaker.py'), arg[0]], timeout=60, cwd=os.path.join(basedir, 'EventMaker'))
        case "3":
            return subprocess.run(['python', os.path.join(basedir, 'Scheduler', 'scheduler.py'), arg[0]], timeout=60, cwd=os.path.join(basedir, 'Scheduler'))
        case "4":
            return subprocess.run(['python', os.path.join(basedir, 'Automail', 'Automail.py'), arg[0], arg[1]], timeout=60, cwd=os.path.join(basedir, 'Automail'))