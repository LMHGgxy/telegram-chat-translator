import telebot
from os import getenv
from python_translator import Translator
from telebot.async_telebot import AsyncTeleBot
import asyncio

bot = AsyncTeleBot(getenv('TOKEN'))

id_1 = int(getenv('ID_ONE'))
id_1_lang = getenv('LANG_ONE')
id_2 = int(getenv('ID_TWO'))
id_2_lang = getenv('LANG_TWO')

@bot.message_handler(commands=["start"])
async def start(message):
    await bot.reply_to(message,"the bot are running")


@bot.message_handler(func=lambda message: True, content_types=['text'])
async def echo_message(message):
    if message.from_user.id == id_2:
        await bot.send_message(chat_id=id_1, text=Translator().translate(
            message.text, id_1_lang, id_2_lang), parse_mode='HTML')
    elif message.from_user.id == id_1:
        await bot.send_message(chat_id=id_2, text=Translator().translate(
            message.text, id_2_lang, id_1_lang), parse_mode='HTML')


@bot.message_handler(func=lambda message: True, content_types=['document', 'video', 'photo', 'sticker'])
async def handle_files(message):
    if message.from_user.id == id_2:
        await bot.forward_message(id_1, message.chat.id, message.message_id)
        if message.caption:
            message_text = f"<code>CAPTION TRADUCIDO: </code> {message.caption}"
            await bot.send_message(chat_id=id_1, text=Translator().translate(
                message_text, id_1_lang, id_2_lang), parse_mode='HTML')
    elif message.from_user.id == id_1:
        await bot.forward_message(id_2, message.chat.id, message.message_id)
        if message.caption:
            message_text = f"<code>CAPTION TRADUCIDO: </code> {message.caption}"
            await bot.send_message(chat_id=id_2, text=Translator().translate(
                message_text, id_2_lang, id_1_lang), parse_mode='HTML')


asyncio.run(bot.infinity_polling())