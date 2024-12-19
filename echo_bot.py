import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F

API_TOKEN = '7544298641:AAFWQhs3ii7E-_7B1qQ4blDFTFjS4r2FHrM'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Удаление вебхука
async def on_startup(dispatcher: Dispatcher):
    await bot.delete_webhook(drop_pending_updates=True)

# Обработчик команды /start
@dp.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.reply("Привет! Я эхо-бот. Отправьте мне любое сообщение, и я верну его вам.")

# Обработчик текстовых сообщений
@dp.message(F.text)
async def echo(message: Message):
    await message.answer(message.text)

if __name__ == '__main__':
    dp.startup.register(on_startup)
    dp.run_polling(bot)
