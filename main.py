TOKEN = '###'
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('I have been started up')

h_MESSAGE = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>запуск бота</em>
<b>/description</b> - <em>описание бота</em>"""





ikb = InlineKeyboardMarkup(row_width=2)
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='Верх',
                               callback_data="up")
    ib2 = InlineKeyboardButton(text='Низ',
                               callback_data="down")
    ikb.add(ib1, ib2)

    await bot.send_message(chat_id=message.from_user.id,
                         text='Выбери что ты будешь качать',
                         reply_markup=ikb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=h_MESSAGE, parse_mode="html")
    await message.delete()
@dp.message_handler(commands=['description'])
async def help_command(message: types.Message):
    await message.answer(text=f'Привет!\nЭтот бот создан для прокачки определенной группы мышц!\nРад видеть тебя {message.from_user.full_name}!')
    await message.delete()


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'up':
        kb = InlineKeyboardMarkup(row_width=3)
        ib1_1 = InlineKeyboardButton(text='Бицепс',
                                   callback_data="biceps")
        ib1_2 = InlineKeyboardButton(text='Грудь',
                                   callback_data="chest")
        ib1_3 = InlineKeyboardButton(text='Пресс',
                                     callback_data="press")
        ib1_4 = InlineKeyboardButton(text='Предплечья',
                                     callback_data="forearms")
        ib1_5 = InlineKeyboardButton(text='Плечи',
                                     callback_data="shoulders")
        ib1_6 = InlineKeyboardButton(text='Трапеции',
                                     callback_data="traps")
        ib1_7 = InlineKeyboardButton(text='Спина',
                                     callback_data="back")
        kb.add(ib1_1, ib1_2, ib1_3, ib1_4, ib1_5, ib1_6, ib1_7)
        await callback.message.answer(text='Выбери группу мышц, которую ты хочешь прокачать',
                                      reply_markup=kb)

    if callback.data == 'down':
        kb = InlineKeyboardMarkup(row_width=2)
        ib2_1 = InlineKeyboardButton(text='Икры',
                                     callback_data="calves")
        ib2_2 = InlineKeyboardButton(text='Квадрицепсы',
                                     callback_data="quadriceps")
        kb.add(ib2_1, ib2_2)
        await callback.message.answer(text='Выбери группу мышц, которую ты хочешь прокачать',
                                      reply_markup=kb)

    if callback.data == 'biceps':
        await callback.message.answer_photo(
            photo="https://cross.expert/wp-content/uploads/2018/03/uprazhneniya-na-bitseps-podem-shtangi.jpeg")

        await callback.message.answer_photo(
            photo="https://sv-sport.ru/wp-content/uploads/2/c/6/2c6a5303c5e1beb72b09d10dbdba6f41.jpeg")

        await callback.message.answer_photo(
            photo="https://www.mentoday.ru/upload/img_cache/801/801d84eed539ffa9d3fe426201f08d62_cropped_666x500.jpg")
        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать',
                               reply_markup=ikb)
    if callback.data == 'chest':
        await callback.message.answer_photo(
            photo="https://webpulse.imgsmail.ru/imgpreview?mb=webpulse&key=pulse_cabinet-image-5bee0d78-1acc-4bd8-ba53-3dcaf1f6d430")
        await callback.message.answer_photo(
            photo="https://webpulse.imgsmail.ru/imgpreview?mb=webpulse&key=pulse_cabinet-image-d0c6c861-d4f9-4a15-96e4-8da4649bb234")
        await callback.message.answer_photo(
            photo="https://avatars.dzeninfra.ru/get-zen_doc/3446134/pub_5edf169db7b200124a0db2a8_5edf2498dc508b6b094a198c/scale_1200")
        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать',
                                      reply_markup=ikb)
    if callback.data == 'press':
        await callback.message.answer_photo(
            photo="https://ss.sport-express.ru/userfiles/materials/172/1727559/volga.jpg")
        await callback.message.answer_photo(
            photo="https://qph.cf2.quoracdn.net/main-qimg-9f3b3d829223aefa978477541418d474-lq")

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать',
                                      reply_markup=ikb)
    if callback.data == 'forearms':
        await callback.message.answer_photo(
            photo="https://www.inspireusafoundation.org/wp-content/uploads/2021/11/dumbbell-reverse-wrist-curl-benefits.jpg")
        await callback.message.answer_photo(
            photo="https://mobilephysiotherapyclinic.in/wp-content/uploads/2022/02/813393198sst1644214778-1.jpg")

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать',
                                      reply_markup=ikb)
    if callback.data == 'shoulders':
        await callback.message.answer_photo(
            photo="https://generationiron.com/wp-content/uploads/2022/02/Screen-Shot-2022-03-09-at-6.51.14-PM.png")
        await callback.message.answer_photo(
            photo="https://s3.amazonaws.com/prod.skimble/assets/2416111/image_iphone.jpg")
        await callback.message.answer_photo(
            photo="https://www.inspireusafoundation.org/wp-content/uploads/2022/03/upright-row-768x578.png")

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать',
                                      reply_markup=ikb)
    if callback.data == 'traps':
        await callback.message.answer_photo(
            photo="https://www.mybodycreator.com/content/files/2020/05/10/446_M.png")
        await callback.message.answer_photo(
            photo="https://www.burnthefatinnercircle.com/members/images/1893b.jpg")
        await callback.message.answer_photo(
            photo="https://www.inspireusafoundation.org/wp-content/uploads/2022/03/upright-row-768x578.png")

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать',
                                      reply_markup=ikb)
    if callback.data == 'back':
        await callback.message.answer_photo(
            photo="https://www.inspireusafoundation.org/wp-content/uploads/2022/11/pull-up-variations.jpg")
        await callback.message.answer_photo(
            photo="https://webpulse.imgsmail.ru/imgpreview?mb=webpulse&key=pulse_cabinet-image-9d62563e-f37e-454c-96b2-5e3bf68d0a3d")
        await callback.message.answer_photo(
            photo="https://www.mybodycreator.com/content/files/exercises/47.png")

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать',
                                      reply_markup=ikb)
    if callback.data == 'calves':
        await callback.message.answer_photo(
            photo="https://images.squarespace-cdn.com/content/v1/5ffcea9416aee143500ea103/1638439412667-VVRLZIFSASOD7Q6TJNE7/7.%2BShouldered%2BSmith%2BMachine%2BStanding%2BCalf%2BRaises.png")
        await callback.message.answer_photo(
            photo="https://static.strengthlevel.com/images/illustrations/seated-calf-raise-1000x1000.jpg")

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать',
                                      reply_markup=ikb)
    if callback.data == 'quadriceps':
        await callback.message.answer_photo(
            photo="https://www.inspireusafoundation.org/wp-content/uploads/2022/05/high-bar-squat-768x447.png")
        await callback.message.answer_photo(
            photo="https://cdn.shopify.com/s/files/1/1876/4703/files/shutterstock_421042393_480x480.jpg?v=1644566569")
        await callback.message.answer_photo(
            photo="https://avatars.dzeninfra.ru/get-zen_doc/1931664/pub_5d86351e2beb4900aec636c2_5d86377da06eaf00ad1d6bf2/scale_1200")

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать',
                                      reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
