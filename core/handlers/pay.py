from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Донат на пиво',
        description='Принимаются донаты на пиво',
        payload='Payment inner data, you know',
        provider_token='381764678:TEST:59128',
        currency='rub',
        prices=[
            LabeledPrice(label='Пиво', amount=100*100),
            LabeledPrice(label='НДС', amount=20*100),
            LabeledPrice(label='Скидка', amount=-20*100),
            LabeledPrice(label='Бонус', amount=-40*100)
        ], # все цены указываются целыми числами в копейках
        max_tip_amount=100*100,
        suggested_tip_amounts=[10*100, 20*100, 30*100, 40*100],
        start_parameter='REPAnya',
        provider_data=None,
        photo_url='https://img2.joyreactor.cc/pics/comment/%D0%BF%D0%B8%D0%B2%D0%BE-%D0%B1%D1%83%D1%85%D0%BB%D0%BE-%D0%9C%D0%B5%D0%BC%D1%8B-%D0%BC%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD-773415.jpeg',
        photo_size=100,
        photo_height=450,
        photo_width=800,
        need_name=True, # если нужно полное имя пользователя
        need_phone_number=True, # если нужен номер телефона пользователя
        need_email=True, # если нужен email пользователя
        need_shipping_address=False, # если нужен адрес для доставки продукта
        send_phone_number_to_provider=False, # если платежный провайдер просит передать номер телефона пользователя
        send_email_to_provider=False, # если платежный провайдер просит отправить email покупателя
        is_flexible=False, # если конечная цена зависит от способда доставки
        disable_notification=False, # если True, то оповещение о покупке будет доставлено без звука
        protect_content=False, # True, если нужно защитить пост от пересылки и копированиня
        reply_to_message_id=None, # id сообщения, которое нужно отправить в счёт покупателю
        allow_sending_without_reply=True, # отправить счёт на оплату даже если цетируемое сообщение не найдено
        reply_markup=None, # если хочется отправить ещё какую-либо клавиатуру дальше, первая кнопка должна быть "оплатить"
        request_timeout=15, # таймаут запроса
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f'Спасибо за донат на пиво {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.'
    await message.answer(msg)