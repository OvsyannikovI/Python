# 1. Напишите программу, удаляющую 
# из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.

# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def list_rand_words(count, alp: str = "абв"):
    word_list = []
    for i in range(count):
        letters = sample(alp, 3)
        word_list.append("".join(letters))
    return " ".join(word_list)

num =int(input("Count :"))

first_str = list_rand_words(num)

print(first_str)

def replace(my_str: str):
   return " ".join(my_str.replace("абв", "").split())
print(replace(first_str))