# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

name = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]

def ololo(st):
    st = sorted(st)
    #print(st)
    res = {}
    for i in st:
        if i[0] not in res:
            res[i[0]] = [i]
        res[i[0]] += [i]
    return res

print(ololo(name))