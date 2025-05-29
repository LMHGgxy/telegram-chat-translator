import asyncio
import telebot
from os import getenv
from python_translator import Translator
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(getenv('TOKEN'))

id_1 = int(getenv('ID_ONE'))
id_1_lang = getenv('LANG_ONE')
id_2 = int(getenv('ID_TWO'))
id_2_lang = getenv('LANG_TWO')

translator = Translator()

@bot.message_handler(commands=["start"])
async def start(message):
    await bot.reply_to(message, "Bot activo y escuchando.")

@bot.message_handler(content_types=['text'])
async def handle_text(message):
    try:
        from_id = message.from_user.id
        target_id = id_1 if from_id == id_2 else id_2 if from_id == id_1 else None

        if not target_id:
            return

        source_lang = id_2_lang if from_id == id_1 else id_1_lang
        target_lang = id_1_lang if from_id == id_2 else id_2_lang

        translated_text = translator.translate(message.text, target_lang, source_lang)
        await bot.send_message(chat_id=target_id, text=translated_text, parse_mode='HTML')
    except Exception as e:
        await bot.send_message(message.chat.id, f"Error en traducción: {e}")

@bot.message_handler(content_types=['document', 'video', 'photo', 'sticker'])
async def handle_media(message):
    try:
        from_id = message.from_user.id
        target_id = id_1 if from_id == id_2 else id_2 if from_id == id_1 else None

        if not target_id:
            return

        await bot.forward_message(chat_id=target_id, from_chat_id=message.chat.id, message_id=message.message_id)

        if message.caption:
            source_lang = id_2_lang if from_id == id_1 else id_1_lang
            target_lang = id_1_lang if from_id == id_2 else id_2_lang
            translated_caption = translator.translate(message.caption, target_lang, source_lang)
            caption_text = f"<code>CAPTION TRADUCIDO:</code> {translated_caption}"
            await bot.send_message(chat_id=target_id, text=caption_text, parse_mode='HTML')

    except Exception as e:
        await bot.send_message(message.chat.id, f"Error en reenvío o traducción: {e}")

if __name__ == "__main__":
    asyncio.run(bot.infinity_polling())
