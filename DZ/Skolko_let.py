# _*_coding:cp1251_*_
from datetime import date
def Let():

    print("Введите день, месяц и год своего рождения!")

    today = date.today()
    try:
        day = int(input("Введите день:""- "))
        if 1<=day<=31:
            pass
        else:
            print("Введите число от 1 до 31!")
    except (ValueError, (NameError)):
        print("Недопустимое значение ДНЯ!")
    try:
        month = int(input("Введите месяц:""- "))
        if 1<=month<=12:
            pass
        else:
            print("Введите число от 1 до 12!")
    except (ValueError, (NameError)):
        print("Недопустимое значение МЕСЯЦА!")
    try:
        year = int(input("Введите год:""- "))
        if 1000<=year<today.year:
            pass
        else:
            print("Введите правильно ГОД!")
    except (ValueError, (NameError)):
        print("Недопустимое значение ГОДА!")
    try:
        age = today.year - year - ((today.month, today.day) < (month, day))
        last_dig = age % 10
        if 10 < age < 20:
            print("Вам", age, "лет!")
        elif 1 < last_dig < 5:
            print("Вам", age, "года!")
        elif last_dig == 1:
            print("Вам", age, "год!")
        else:
            print("Вам", age, "лет!")
    except NameError:
        print("ВЫ ВВЕЛИ НЕ ВЕРНЫЕ ДАННЫЕ!!!")
