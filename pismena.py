from turtle import*
def pismeno_f (velikost):
    left (90)
    forward(5*velikost)
    right(90)
    forward(2*velikost)
    right (180)
    forward(2*velikost)
    left(90)
    forward(2*velikost)
    left(90)
    forward(2*velikost)
    left(180)
    forward(2*velikost)
    left(90)
    forward(3*velikost)
    left(90)
def pismeno_k(velikost):
    left(90)
    forward(2.5*velikost)
    right(45)
    forward(3*velikost)
    right(180)
    forward(3*velikost)
    left(90)
    forward(3*velikost)
    left(180)
    forward(3*velikost)
    right(45)
    forward(2.5*velikost)
    left(180)
    forward(5*velikost)
    left(90)
def pismeno_p (velikost):
    speed(10)
    left(90)
    forward(5*velikost)
    right(90)
    for i in range(59):
        right(3)
        forward(0.06*velikost)
    right(3)
    left(90)
    forward(2.7*velikost)
    left(90)
def pismeno_o (velikost):
    penup()
    forward(2*velikost)
    pendown()
    for i in range(45):
        left(2)
        forward(0.06*velikost)
    forward(0.45*velikost)
    for i in range(90):
        left(2)
        forward(0.06*velikost)
    forward(0.45*velikost)
    for i in range(45):
        left(2)
        forward(0.06*velikost)
    penup()
    forward(2*velikost)
    pendown()






speed(10)
pismeno_o(20)
exitonclick()
