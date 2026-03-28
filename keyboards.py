from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SERVICES

def get_services_kb():
    buttons =[]
    for key,(name,price) in SERVICES.items():
        buttons.append([
            InlineKeyboardButton(text=f"{name}-{price}",callback_data=f"ser_{key}")
        ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
