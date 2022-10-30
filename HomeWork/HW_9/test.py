from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Определяем константы этапов разговора
CHOISE, PLAY, LOCATION, BIO = range(4)

# функция обратного вызова точки входа в разговор
def start(update, _):
    update.message.reply_text("Играем в крестики-нолики?\n1 - Game\n0 - Exit")
    return CHOISE

def choise(update, _):    
    # user = update.message.from_user
    user_choise = update.message.text
    if user_choise in "1 0":
        if user_choise == "0":
            return cancel
            # cancel(update, _)
        elif user_choise == "1":
            return update.message.reply_text("You Start")
    else:
        update.message.reply_text("You" + user_choise)

def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END

if __name__ == '__main__':
    updater = Updater("5673776766:AAFYbvEnMEYV30iuxhnZJF7tuJFEJzY0EXk")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOISE: [MessageHandler(Filters.text, choise)]
            # PLAY: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            # LOCATION: [
            #     MessageHandler(Filters.location, location),
            #     CommandHandler('skip', skip_location),
            # ],
            # BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()