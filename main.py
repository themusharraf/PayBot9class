import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from root import TOKEN
from bottons import menu, catMenu, inlineBtn
from Payments import order_1, pre_checkout_query, successful_payment

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello", reply_markup=menu)


@dp.message(F.text == "Category")
async def category(message: Message):
    await message.answer("Choose", reply_markup=catMenu)


@dp.message(F.text == "Product 1")
async def product_1(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/ck9sgvbk9fq1var6o9h0/original.jpg",
                               caption="Iphone 14 Pro Max\n"
                                       "Battery Level: 100%\n", reply_markup=inlineBtn)


dp.callback_query.register(order_1, F.data == "pay_1")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
