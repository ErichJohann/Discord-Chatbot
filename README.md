# Discord Chatbot Assistant
An AI Discord chatbot that executes external scripts for task automation.

### Features
- Responds to all messages in a channel.
- Can either generate a text response or execute an external file and return the result.
- Uses AI to determine if a message is a command or casual conversation.
- Supports different LLM models.
- Easily scalable.

---

### Requirements
- Discord application set up with a bot token.
- Groq API connection configured.
- At least one external script to execute.
- Install the following libraries:
  - discord.py
  - groq

---

### Scripts
The bot uses configuration files located in the `/prompts` folder to determine how it responds and executes commands.  

- **`/persona.txt`** – Defines the bot’s personality and style of conversation.  
  - Used for **casual chat** responses.
  - You can fully customize the tone, vocabulary, and behavior.  
  - Default is Rimuru from Tensei Shitara Slime since I like it
- **`/scripts.txt`** is the first request to identify if a code is being invoked or not
  - Asks the model to answer in a specific way

> **Note:** Both files contain references to the available scripts. Any time you add or remove a script, you should update these files to keep the bot’s understanding accurate.
  
---

### Running
```bash
python Discord_Chatbot_Assistant
```
