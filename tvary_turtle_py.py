from turtle import *
speed(int (textinput("rychlost", " ")))
def otazka():
    a=textinput("jaky chces tvar?", " ")
    while a!=("kytka") and a!=("ctverec") and a!=("kruh"):
        a=textinput("jaky chces tvar?", " ")
    return a
def kytka():
    for i in range(9):
        for i in range(15):
            forward(15)
            right(5)
        right(85)
def ctverec():
    for i in range(4):
        forward(50)
        left(90)
def kruh():
    for i in range(75):
        forward(10)
        right(5)
def otazka_i_to_ostatni():
    a=otazka()
    if a==("kytka"):
      kytka()
    elif a==("ctverec"):
        ctverec()
    elif a==("kruh"):
        kruh()
def pismeno_p ():
    speed(10)
    left(90)
    forward(50)
    right(90)
    forward(25)
    right(90)
    forward(20)
    right(90)
    forward(25)
    left(90)
pismeno_p()
exitonclick()
