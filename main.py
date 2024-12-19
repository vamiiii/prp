import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.filters import BaseFilter

API_TOKEN = '8108080352:AAGA7zr8n3ab-KBcmf1TKnnp7DZm1XD-K5M'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

class ContainsText(BaseFilter):
    def __init__(self, text: str):
        self.text = text.lower()

    async def __call__(self, message: Message) -> bool:
        return self.text in message.text.lower()

@dp.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.reply("Привет!\nЯ самый лучший бот!\nОтправь мне любое сообщение, и я тебе отвечу.")

@dp.message(ContainsText("Казань"))
async def about_kazan(message: Message):
    await message.reply("Казань — это столица Республики Татарстан, один из крупнейших культурных и экономических центров России. Что именно вас интересует о Казани?")

@dp.message(ContainsText("достопримечательности"))
async def kazan_attractions(message: Message):
    await message.reply("В Казани много интересных достопримечательностей, таких как Казанский Кремль, мечеть Кул-Шариф, Башня Сююмбике и многие другие. Что бы вы хотели узнать подробнее?")

@dp.message(ContainsText("история"))
async def kazan_history(message: Message):
    await message.reply("Казань имеет богатую историю, начиная с основания в 1005 году. Город был столицей Казанского ханства и играл важную роль в истории России. Что именно вас интересует в истории Казани?")

@dp.message(ContainsText("культура"))
async def kazan_culture(message: Message):
    await message.reply("Казань известна своей богатой культурой и традициями. Здесь проводятся многочисленные фестивали, концерты и выставки. Что бы вы хотели узнать подробнее о культуре Казани?")

@dp.message()
async def echo(message: Message):
    await message.answer("Извините, я не понял ваш вопрос. Давайте поговорим о Казани!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
