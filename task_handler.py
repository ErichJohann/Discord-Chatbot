import subprocess
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()
basedir = os.getenv('BASEPATH')
me = os.getenv('MYID')

def scriptExc(op, arg, userid):
    #Perhaps change for a list of authorized users in the future
    if(userid != me):
        return "Desculpe, mas você não é autorizado..."
    
    #executes the desired operation on their working diretory
    arg = arg.split(';')
    try:
        match op:
            case "1":
                result = subprocess.run(['python', os.path.join(basedir, 'EventMaker', 'eventmaker.py'), arg[0]], timeout=60, cwd=os.path.join(basedir, 'EventMaker'), capture_output=True, text=True)
            case "2":
                result = subprocess.run(['python', os.path.join(basedir, 'Scheduler', 'scheduler.py'), arg[0]], timeout=60, cwd=os.path.join(basedir, 'Scheduler'), capture_output=True, text=True)
            case "3":
                result = subprocess.run(['python', os.path.join(basedir, 'Automail', 'Automail.py'), arg[0], arg[1]], timeout=60, cwd=os.path.join(basedir, 'Automail'), capture_output=True, text=True)
    
    except subprocess.TimeoutExpired:
        return "O script excedeu o tempo limite de execução"
    except Exception as e:
        return f'Erro ao executar script: {e}'
    
    # Combina stdout e stderr (ou usa apenas stdout se stderr estiver vazio)
    output = result.stdout + (f"\n[Error]\n{result.stderr}" if result.stderr else "")
    return output