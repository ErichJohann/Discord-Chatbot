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

#get last 16 messages from current channel
history = {}
MAX_HIST = 16
def getHistory(channel):
    if channel not in history:
        history[channel] = deque(maxlen=MAX_HIST)
    return history[channel]

#looks if user wishes to execute a script
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
        return completion.choices[0].message.content
    
    except Exception:
        return "Error api groq"

async def getResponse(input,channel, username, userid):
    isCommand = await checkCommand(input)
    #split operation number and arguments
    op, args = isCommand.split(';', 1)

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

    messages.append({"role": "user", "content": f'{username}: {input}'}) 

    #if operation is not zero, user wishes to execute a script
    if(op != "0"):
        output = scriptExc(op, args, str(userid))
    else:
        try:
            completion = groqClient.chat.completions.create(
                messages=messages,
                model="llama-3.3-70b-versatile",
                max_completion_tokens=128,
                temperature=1
            )
            output = completion.choices[0].message.content
        
        except Exception:
            return "Não consigo pensar direito, estou confuso... Acho que meu mana acabou\n Zzz..."

        #updates message history
        history.append({'content': f'{username}: {input}', 'is_bot': False})
        history.append({'content': output, 'is_bot': True})

    return output