from groq import Groq
from dotenv import load_dotenv
import os
from collections import deque

from task_handler import scriptExc

load_dotenv()
groqKey = os.getenv('GROQ_KEY')
groqClient = Groq(api_key=groqKey)

with open(r'prompts\persona.txt', 'r', encoding='utf-8') as file:
    BehavePrompt = file.read()
with open(r'prompts\scripts.txt', 'r', encoding='utf-8') as file:
    ScriptPrompt = file.read()

history = {}
MAX_HIST = 10
def getHistory(channel):
    if channel not in history:
        history[channel] = deque(maxlen=MAX_HIST)
    return history[channel]

async def checkCommand(msg):
    messages=[
        {
            "role": "system",
            "content": ScriptPrompt
        }
    ]
    messages.append({"role": "user", "content": msg})

    try:
        completion = groqClient.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            max_completion_tokens=64,
            temperature=0.2
        )
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content
    
    except Exception:
        return "Error api groq"

async def getResponse(input,channel, username, userid):
    answer = await checkCommand(input)
    codOp, args = answer.split(';', 1)
    if(codOp != "0"):
        return scriptExc(codOp, args, str(userid))
    
    history = getHistory(channel)

    messages=[
                {
                    "role": "system",
                    "content":BehavePrompt
                }
            ]
    
    for msg in history:
        messages.append({
            "role": "assistant" if msg["is_bot"] else "user",
            "content": msg["content"]
        })
        #print(msg['content'])
    messages.append({"role": "user", "content": f'{username}: {input}'}) 
    
    try:
        completion = groqClient.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            max_completion_tokens=128,
            temperature=1
        )

        history.append({'content': f'{username}: {input}', 'is_bot': False})
        history.append({'content': completion.choices[0].message.content, 'is_bot': True})

        return completion.choices[0].message.content
    
    except Exception:
        return "Não consigo pensar direito, estou confuso... Acho que meu mana acabou\n Zzz..."