from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
help_button = KeyboardButton(text='/help', )
description_button = KeyboardButton(text='/description')
location_button = KeyboardButton(text='/location')
photo_button = KeyboardButton(text='/photo')
keyboard.add(help_button, description_button, location_button, photo_button)


ph_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
back_button = KeyboardButton(text='Главное меню')
random_photo = KeyboardButton(text='Случайное фото')
ph_keyboard.add(random_photo, back_button)


photo_keyboard = InlineKeyboardMarkup(row_width=2)
next_photo_button = InlineKeyboardButton('Следующее фото', callback_data='next')
like_button = InlineKeyboardButton('Нравится', callback_data='like')
dislike_button = InlineKeyboardButton('Не нравится', callback_data='dislike')
back_button = InlineKeyboardButton('В главное меню', callback_data='back')
photo_keyboard.insert(next_photo_button).add(like_button, dislike_button).insert(back_button)
