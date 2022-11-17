import os
import random

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardRemove, InputFile
from aiogram.dispatcher.filters import Text
from keyboards import keyboard, photo_keyboard, ph_keyboard

load_dotenv()
TOKEN = str(os.environ.get('TOKEN'))

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('BOT HAVE BEEN STARTED')


HELP_COMMAND = '''
<b>/start</b> - <em>Запускает бота</em>
<b>/help</b> - <em>Помощь</em>
<b>/description</b> - <em>Описание</em>
<b>/photo</b> - <em>Выбрать случайное фото</em>
<b>/location</b> - <em>Получить случайную локацию</em>
'''

DESCRIPTION_COMMAND = '''
Привет! Этот бот умеет:
-Отправлять случайную локацию
-Проводить голосование за случайную картинку
Для вывода справки напишите /help
'''

PHOTOS = [
    'data/photo1.jpg',
    'data/photo2.jpg',
    'data/photo3.jpg',
]
photo = random.choice(PHOTOS)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Добро пожаловать!', reply_markup=keyboard)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode='HTML', reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=DESCRIPTION_COMMAND, reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Получите случайное фото', reply_markup=ph_keyboard)
    await message.delete()


@dp.message_handler(Text('Случайное фото'))
async def photo_command(message: types.Message):
    await message.answer(text='Рандомная фотка', reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(chat_id=message.from_user.id, photo=InputFile(photo), reply_markup=photo_keyboard)


@dp.message_handler(Text('Главное меню'))
async def main_menu_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Вы в главном меню!', reply_markup=keyboard)
    await message.delete()


@dp.callback_query_handler()
async def photo_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='Вам понравилась эта фотография')
    elif callback.data == 'dislike':
        await callback.answer(text='Вам не понравилась эта фотография')
    elif callback.data == 'back':
        await callback.message.answer(text='Вы в главном меню!', reply_markup=keyboard)
    else:
        global photo
        photo = random.choice(list(filter(lambda x: x != photo, PHOTOS)))
        await callback.message.edit_media(types.InputMedia(media=InputFile(photo), type='photo'), reply_markup=photo_keyboard)
        await callback.answer()


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    main()
