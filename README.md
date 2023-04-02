
# TELEGRAM-CHAT-TRANSLATOR

This is a simple bot that works through ```PyTelegramApiBot``` in an ```asynchronous``` way, it allows you to translate the messages that you send to the person you want through their chatId the messages in their language.
## Installation

clone telegram-chat-translator with `git` 
```bash
git clone https://github.com/LMHGgxy/telegram-chat-translator
cd telegram-chat-translator
pip3 install -r requirements.txt
```
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

| variables| data |
|----------|------
|`ID_ONE`  | your id
|`LANG_ONE`| your language
|`ID_TWO`  | someone else's id
|`LANG_TWO`| someone else's language

## Deployment

To deploy this project run
```bash
  python bot.py
```
