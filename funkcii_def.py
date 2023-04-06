# _*_coding:cp1251_*_

# импорт тартилы
import turtle
# скорость движения
turtle.speed(2)
def move(a): # функция "move" - движения
    # движение (вперед - forward, назад - backward) значение в скобках это (количество пиксилей)
    turtle.forward(100)
    # поворот на (лево - left, право - right) значение в скобках это (градус поворота)
    turtle.left(90)
def drawSquare(a):                  # вызов функции рисования врадрата
    for i in range(4):              # итерация функции рисования врадрата
        move(a)                     # вызов функции "move"

def drawSquareColor(a, color):      # вызов функции рисования врадрата
    # turtle.color(color)             # зарисовка в указанный цвет
    # turtle.begin_fill()             # начало закрашивания
    for i in range(4):              # итерация функции рисования врадрата
        move(a)                     # вызов функции "move"
    # turtle.end_fill()               # конец закрашивания

def move2(b):                       # функция "move" - движения
    turtle.backward(100)
    # поворот на (лево - left, право - right) значение в скобках это (градус поворота)
    turtle.right(-90)
def drawSquare2(b):                 # функция рисования врадрата 2
    for i in range(4):              # итерация функции рисования врадрата
        move2(b)                    # вызов функции "move"

def drawSquare2Color(b, color):     # функция рисования врадрата 2
    # turtle.color(color)  # зарисовка в указанный цвет
    # turtle.color(color)             # зарисовка в указанный цвет
    # turtle.begin_fill()
    for i in range(4):              # итерация функции рисования врадрата
        move2(b)                    # вызов функции "move"
    # turtle.end_fill()               # конец закрашивания

# вызов функции рисования врадрата
drawSquareColor(60, 'red'):
# движение в строну по оси X, Y + или - , значение в скобках это (растояние)
turtle.goto(-150, -150)
# вызов функции рисования врадрата 2
drawSquare2Color(160, 'green'):

