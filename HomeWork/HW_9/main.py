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
board = list(map(str, range(1, 10)))
counter = 0

# функция обратного вызова точки входа в разговор
def start(update, _):
    update.message.reply_text(draw_board())
    update.message.reply_text("Играем в крестики-нолики?\n1 - Game\n0 - Exit")
    return CHOISE


def choise(update, _):
    # user = update.message.from_user
    user_choise = update.message.text
    if user_choise in "1 0":
        if user_choise == "0":
            return cancel
        elif user_choise == "1":
            return PLAY
    else:
        update.message.reply_text("You" + user_choise)
        return cancel


def draw_board():
    str_line = ""
    str_line += "-" * 20
    for i in range(3):
        str_line += "\n"
        for k in range(3):
            str_line += " ".join(board[k + i * 3]) + " " * 12
        str_line += f"\n{'-' * 20}"
    return str_line


def place_sign(token, answer):
    global board
    rez = ""
    while True:
        if int(answer) in range(1, 10):
            answer = int(answer)
            pos = board[answer - 1]
            if pos not in (chr(10060), chr(11093)):
                board[answer - 1] = chr(10060) if token == "X" else chr(11093)
                break
            else:
                rez += f"This cell is already occupied{chr(9995)}{chr(129292)}"
        else:
            rez += f"Incorrect input{chr(9940)}. Are you sure you entered a correct number?"


def whatistoken(counter):
    if counter % 2:
        return "O"
    else:
        return "X"


def play(update, _):
    global counter
    update.message.reply_text(draw_board())
    while True:
        answer = update.message.text
        update.message.reply_text(
            f"Enter a number from 1 to 9.\nSelect a position {whatistoken(counter)}?"
        )
        place_sign(whatistoken(counter), answer)
        update.message.reply_text(draw_board())
        if counter > 3:
            if check_win():
                update.message.reply_text(
                    f"{check_win()} - WIN{chr(127942)}{chr(127881)}!"
                )
                break
        if counter == 8:
            update.message.reply_text(f"Drawn game {chr(129318)}{chr(129309)}!")
            break
        counter += 1


def check_win():
    win_coord = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n


def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        "Мое дело предложить - Ваше отказаться" " Будет скучно - пиши.",
        reply_markup=ReplyKeyboardRemove(),
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == "__main__":
    updater = Updater("5673776766:AAFYbvEnMEYV30iuxhnZJF7tuJFEJzY0EXk")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler("start", start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOISE: [MessageHandler(Filters.text, choise)],
            PLAY: [MessageHandler(Filters.text, play)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()
