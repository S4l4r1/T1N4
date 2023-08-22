#Создадим 2 пустых списка: один будет хранить символы в правильном порядке, другой - в обратном.
emp_list_v1 = []
emp_list_v2 = []
#Создадим функцию, проверяющую строки на палиндром. Дадим пользователю самому вводить строку. Сделаем цикл, заполняющий списки и развернём один из них. Равенство - правда, остальное - ложь.
def palyndrome_check():
    string = input('Введите строку для проверки на палиндром: ')
    for i in string:
        emp_list_v1.append(i)
        emp_list_v2.append(i)
    emp_list_v1.reverse()
    if emp_list_v1 == emp_list_v2:
        return True
    elif emp_list_v1 != emp_list_v2:
        return False
#На финал: обозначение переменной - функции и её принт.
palyndrome = palyndrome_check()
print(palyndrome)
