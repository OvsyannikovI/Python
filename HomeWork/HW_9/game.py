from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    Filters,
    MessageHandler,
    ConversationHandler,
)

board = list(map(str, range(1, 10)))


def draw_board(update, _):
    str_line = ""
    update.message.reply_text('-' * 20)
    for i in range(3):
        for k in range(3):
            str_line += " ".join(board[k + i * 3]) + " " * 12
        update.message.reply_text(str_line)
        str_line = ""
        update.message.reply_text(f"\n{'-' * 20}")


def place_sign(update, _, token):
    global board
    while True:
        if token.isdigit() and int(token) in range(1, 10):
            token = int(token)
            pos = board[token - 1]
            if pos not in (chr(10060), chr(11093)):
                board[token - 1] = chr(10060) if token == "X" else chr(11093)
                break
            else:
                update.message.reply_text("This cell is already occupied X or O")
        else:
            update.message.reply_text("Incorrect. Are you sure you entered a correct number?")


def check_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n

