import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import BaseFilter
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router

API_TOKEN = '7544298641:AAFWQhs3ii7E-_7B1qQ4blDFTFjS4r2FHrM'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

class ContainsText(BaseFilter):
    def __init__(self, text: str):
        self.text = text.lower()

    async def __call__(self, message: Message) -> bool:
        return self.text in message.text.lower()

# Создание клавиатуры
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Казань")],
        [KeyboardButton(text="Достопримечательности")],
        [KeyboardButton(text="История")],
        [KeyboardButton(text="Культура")],
    ],
    resize_keyboard=True
)

# Обработчик команды /start
@router.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.reply("Привет!\nЯ самый лучший бот!\nОтправь мне любое сообщение, и я тебе отвечу.", reply_markup=keyboard)

# Обработчик сообщений, содержащих текст "Казань"
@router.message(ContainsText("Казань"))
async def about_kazan(message: Message):
    await message.reply("Казань — это столица Республики Татарстан, один из крупнейших культурных и экономических центров России. Что именно вас интересует о Казани?", reply_markup=keyboard)

# Обработчик сообщений, содержащих текст "достопримечательности"
@router.message(ContainsText("достопримечательности"))
async def kazan_attractions(message: Message):
    await message.reply("В Казани много интересных достопримечательностей, таких как Казанский Кремль, мечеть Кул-Шариф, Башня Сююмбике и многие другие. Что бы вы хотели узнать подробнее?", reply_markup=keyboard)

# Обработчик сообщений, содержащих текст "история"
@router.message(ContainsText("история"))
async def kazan_history(message: Message):
    await message.reply("Казань имеет богатую историю, начиная с основания в 1005 году. Город был столицей Казанского ханства и играл важную роль в истории России. Что именно вас интересует в истории Казани?", reply_markup=keyboard)

# Обработчик сообщений, содержащих текст "культура"
@router.message(ContainsText("культура"))
async def kazan_culture(message: Message):
    await message.reply("Казань известна своей богатой культурой и традициями. Здесь проводятся многочисленные фестивали, концерты и выставки. Что бы вы хотели узнать подробнее о культуре Казани?", reply_markup=keyboard)

# Обработчик всех остальных сообщений
@router.message()
async def echo(message: Message):
    await message.answer("Извините, я не понял ваш вопрос. Давайте поговорим о Казани!", reply_markup=keyboard)

# Регистрация роутера в диспетчере
dp.include_router(router)

async def main():
    # Удаление вебхука
    await bot.delete_webhook(drop_pending_updates=True)
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
