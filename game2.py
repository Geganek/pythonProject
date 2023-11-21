from turtle import *
left (90)
def nahoru():
    forward(10)
def dolu():
    left(180)
    forward(10)
    left(180)
def doleva():
    left(90)
    forward(10)
    right(90)
def doprava():
    right(90)
    forward(10)
    left(90)
showturtle()
onkey(nahoru,"Up")
onkey(dolu,"Down")
onkey(doleva,"Left")
onkey(doprava,"Right")
listen()
mainloop()
