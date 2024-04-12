import telegram
import logging
from telegram.ext import (
    Application,
    MessageHandler,
    filters,
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler
)

from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_TOKEN

# Запуск логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

bot = telegram.Bot(token=BOT_TOKEN)


# reply_keyboard = [["Учебник 📚", "Практика ✍️"], ["Дополнительно ⚙️"]]
# markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


# Команды
async def start(update, context) -> None:
    """Отправляет сообщение когда получена команда /start"""
    try:
        reply_keyboard = [["Учебник 📚", "Практика ✍"], ["Дополнительно ⚙"]]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        # await update.message.reply_text("", reply_markup=markup)

        user = update.effective_user
        chat_id = update.message.chat_id
        photo_path = "data/penguin.gif"

        await update.message.reply_html(
            rf"Привет {user.mention_html()}! Меня зовут Никита. Я помогу тебе подготовиться к ЕГЭ по профильной математике💯", )

        await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))

        await update.message.reply_text(
            "У меня есть учебник с актуальной теорией и тесты. Для навигации используй кнопки или меню в нижней части экрана.")


    except Exception as ex:
        print(f"ERROR {ex}")


async def tutorial(update, context) -> None:
    """Отправляет сообщение кнопок когда получена команда /tutorial"""

    keyboard = [
        [
            InlineKeyboardButton("1", callback_data='Задние 1'),
            InlineKeyboardButton("2", callback_data='Задние 2'),
            InlineKeyboardButton("3", callback_data='Задние 3')
        ],

        [
            InlineKeyboardButton("4", callback_data='Задние 4'),
            InlineKeyboardButton("5", callback_data='Задние 5'),
            InlineKeyboardButton("6", callback_data='Задние 6')
        ],

        [
            InlineKeyboardButton("7", callback_data='Задние 7'),
            InlineKeyboardButton("8", callback_data='Задние 8'),
            InlineKeyboardButton("9", callback_data='Задние 9')
        ],

        [
            InlineKeyboardButton("10", callback_data='Задние 10'),
            InlineKeyboardButton("11", callback_data='Задние 11'),
            InlineKeyboardButton("12", callback_data='Задние 12')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите номер задания ЕГЭ по математике:', reply_markup=reply_markup)


async def practice(update, context) -> None:
    """Отправляет сообщение кнопок когда получена команда /practice"""

    keyboard = [
        [
            InlineKeyboardButton("Задание 1", callback_data='Задние 1'),
            InlineKeyboardButton("Задание 2", callback_data='Задние 2'),
            InlineKeyboardButton("Задание 3", callback_data='Задние 3')
        ],

        [
            InlineKeyboardButton("Задание 4", callback_data='Задние 4'),
            InlineKeyboardButton("Задание 5", callback_data='Задние 5'),
            InlineKeyboardButton("Задание 6", callback_data='Задние 6')
        ],

        [
            InlineKeyboardButton("Задание 7", callback_data='Задние 7'),
            InlineKeyboardButton("Задание 8", callback_data='Задние 8'),
            InlineKeyboardButton("Задание 9", callback_data='Задние 9')
        ],

        [
            InlineKeyboardButton("Задание 10", callback_data='Задние 10'),
            InlineKeyboardButton("Задание 11", callback_data='Задние 11'),
            InlineKeyboardButton("Задание 12", callback_data='Задние 12')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери задание для нарешивания 👇", reply_markup=reply_markup)


async def button(update, context) -> None:
    """Функция обработки инлайн-кнопок"""
    query = update.callback_query
    query.answer()
    await query.message.reply_text(f"Вы выбрали: {query.data}")


# Ответы
async def handler_response(update, context):
    ...


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    # Команды
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("tutorial", tutorial))
    application.add_handler(CommandHandler("practice", practice))

    # Сообщения
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.Regex("Учебник 📚"), tutorial))
    application.add_handler(MessageHandler(filters.Regex("Практика ✍"), practice))

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()
