jornal = "spisok1.txt"                  # имя файла
# sp = []
#
# while True:                             # Создаем цикл
#     sp0 = input("Введите строку: ")     # Вводстроки пользователем
#     if sp0 == "":                       # Проверяем на наличие пустой строки
#         break                           # Выход из цикла если строка пустая
#     else:
#         sp.append(sp0 + " оценка - ")   # Добовляем введенную строку в список
#         sp1 = input("Введите оценку:")  # Вводстроки пользователем
#         if sp1 == "":                   # Проверяем на наличие пустой строки
#             break                       # Выход из цикла если строка пустая
#         else:
#             sp.append(sp1 + "\n")       # Добовляем введенную строку в список
# print(sp)                               # Вывод записи в консоль
# print("*****************************************************************")
# with open(jornal, "w") as file:         # Делаем запись файла
#     for i in sp:
#         file.write(i)

with open(jornal, "r") as file:         # Считываем файл
    for i in file:
        print(i, end="")                # Ввывод в консоль список класса
    mark_count = 0                      # Счетчик учеников
    mark_sum = 0                        # Сумма оценок
    print("Ученики чьи оценки меньше 3-х:")
    for i in file.readlines():          # Перебор учеников из файла
        i = i.rstrip("\n")              # Удаление сомволов в конце строки
        mark_count += 1                 # Лоличество (учеников) оценок
        mark = int(i[-1])               # Получаем оценки и переводим в числа
        mark_sum += mark                # Суммируем оценки
        if mark < 3:                    # Проверяем условие оценка меньше 3-х
            print("                             ", *i[:-1].split(" - "))
    print("************************************************************")
    print("Средний бал по классу:", mark_sum / mark_count)
    print("Количество учеников\nв классе:", mark_count)