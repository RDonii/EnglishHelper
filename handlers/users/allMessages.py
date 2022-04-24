from aiogram import types
from loader import dp, translator
from utils.oxfordLookup import getDefinitions


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    if type(message.text) is str:
        lang = translator.detect(message.text).lang
        if len(message.text.split(' '))>1:
            if lang=='uz':
                await message.reply(translator.translate(message.text).text)
            elif lang=='en':
                await message.reply(translator.translate(message.text, dest='uz').text)
            else:
                await message.answer(f'Yo o`zbekcha yo inglizcha yozing, brat!')
        else:
            if lang!='en':
                await message.reply(translator.translate(message.text).text)
            else:
                data = getDefinitions(message.text)
                if data:
                    await message.answer(f'💠{message.text}:')
                    for e in data:
                        text = '\n'.join(e['definitions'])
                        await message.answer(text)
                        for audio in e['audios']:
                            await message.answer_audio(audio)
                        
                else:
                    await message.reply('Could not find any definitions. Check the spelling or try another word.')
