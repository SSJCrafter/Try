import turtle
import time

tw = turtle.Screen()
p1 = turtle.Turtle()
p2 = turtle.Turtle()
p2.pencolor("white")


def Right():
    p1.right(90)


tw.onkey(Right, "Right")


def Left():
    p1.left(90)


tw.onkey(Left, "Left")


def Down():
    time.sleep(2)


tw.onkey(Down, "Down")


def Right2():
    p2.right(90)


tw.onkey(Right2, "d")


def Left2():
    p2.left(90)


tw.onkey(Left2, "a")

tw.listen()

x = 6
while x > 5:
    p1.fd(5)
    p2.fd(2)

turtle.mainloop()

