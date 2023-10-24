from turtle import *
aaa = 1
while aaa == 1:
    if onkey ('d'):
        right (5)
    if onkey ('w'):
        forward (1)
    if onkey ('a'):
        left(5)
    if onkey ('s'):
        forward(-5)
    forward(1)
    left(5)
    right(5)

exitonclick()
