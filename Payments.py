from aiogram import Bot, types
from aiogram.types import LabeledPrice, PreCheckoutQuery
from root import PAY_TOKEN


async def order_1(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="iPhone 14 Pro",
                           description="iPhone 14 Pro max 256GB Deep Purple ",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://images.uzum.uz/ck9sgvbk9fq1var6o9h0/original.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=160_000_00),
                               LabeledPrice(label="QQS", amount=19_200_00),
                               LabeledPrice(label="Skidka", amount=-30_200_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Iphone 14 Pro',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: types.Message, bot: Bot):
    msg = f"""
    Payment Done ✅ 
    Product name : {message.successful_payment.invoice_payload}
    Price: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Status Done :  ✅ 
    """

    await message.answer(msg)
