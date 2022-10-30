import logging
import game as gm
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    Filters,
    MessageHandler,
    ConversationHandler,
)

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

PERSON= 0
CHOISE = 0
PLAY = 0

def start(update, _):
    update.message.reply_text("Игра крестики-нолики")
    update.message.reply_text("1- Играем\n 0 - Выход")
    return CHOISE

def choise(update, _):
    # logger.info(user.first_name, update.message.text)
    user_choise = update.message.text
    if user_choise in "1 0":
        if user_choise == "0":
            update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.' ,
        reply_markup=ReplyKeyboardRemove())
            return ConversationHandler.END
        elif user_choise == "1":
            gm.draw_board(update, _)
            return CHOISE
    else:
        update.message.reply_text("1 - Играем\n 0 - Выход")
        update.message.reply_text(user_choise)

def person(update, _):
    gm.draw_board(update, _)
    update.message.reply_text("Enter a number from 1 to 9.\nSelect a position X? ")
    return PERSON

def play(update, _):
    counter = 0
    token = update.message.text
    while True:
        gm.place_sign(update, _, token) if counter % 2 else gm.place_sign(update, _, token)
    #     gm.draw_board(update, _)

        # if counter > 3:
        #     if check_win():
        #         print(f"{check_win()} - WIN{chr(127942)}{chr(127881)}!")
        #         break
        # if counter == 8:
        #     print(f"Drawn game {chr(129318)}{chr(129309)}!")
        #     break
        # counter += 1


def cancel(update, _):
    # определяем пользователяzxw1 bc
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    # logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater('5673776766:AAFYbvEnMEYV30iuxhnZJF7tuJFEJzY0EXk')
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOISE: [MessageHandler(Filters.text, choise)],
            PERSON: [MessageHandler(Filters.text, person)],
            PLAY: [MessageHandler(Filters.text, play)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()