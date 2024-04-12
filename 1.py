# import logging
# from telegram.ext import Application, CommandHandler, CallbackQueryHandler
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
#
# from config import BOT_TOKEN
#
# # Запускаем логгирование
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
# )
#
# logger = logging.getLogger(__name__)
#
# async def start(update, context):
#     """Отправляет сообщение когда получена команда /start"""
#     keyboard = [[InlineKeyboardButton("Команда 1", callback_data='command1'),
#                  InlineKeyboardButton("Команда 2", callback_data='command2')],
#                 [InlineKeyboardButton("Команда 3", callback_data='command3'),
#                  InlineKeyboardButton("Команда 4", callback_data='command4')]]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text('Выберите команду:', reply_markup=reply_markup)
#
# async def help_command(update, context):
#     """Отправляет сообщение когда получена команда /help"""
#     await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")
#
# async def button(update, context):
#     """Функция обработки нажатия на инлайн-кнопки"""
#     query = update.callback_query
#     query.answer()
#     await query.message.reply_text("1")
#     # (text=f"Вы выбрали: {query.data}")
#
# def main():
#     application = Application.builder().token(BOT_TOKEN).build()
#
#     # Добавляем обработчики команд
#     application.add_handler(CommandHandler("help", help_command))
#     application.add_handler(CommandHandler("start", start))
#
#     # Добавляем обработчик инлайн-кнопок
#     application.add_handler(CallbackQueryHandler(button))
#
#     # Запускаем бота
#     application.run_polling()
#
# if __name__ == '__main__':
#     main()
