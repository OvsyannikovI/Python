# 1. Напишите программу, удаляющую 
# из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.

# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def list_rnd_words(count: int, alp: s = "абв"):
    words_list = []
    for i in range(count):
        letters = samle(alp,3)
        words_list.append("".join(letters))
    return " ".join(words_list)

def list_rnd_word(count: int, apl: str = "абв"):
    return " ".join(sample(apl, 3)) for _ in range(count)

def simple_sentence(words: str) -> str:
    return " ".join(words.replace("абв", "").split())

all_list = list_rand_words(int(input("Number of  words: ")))
print(all_list)
print(simple_sentence(all_list))