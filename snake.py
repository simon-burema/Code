# snake game

import os
import turtle
import time
import random

delay = 0.1

# setup the screen
window = turtle.Screen()
window.title("PythonSnake")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)  # turns off animation on the screen

# Snake head
head = turtle.Turtle()
head.speed(0)  # animation speed
head.shape("square")
head.color("Red")
head.penup()
head.goto(0, 0)
head.direction = "right"

# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_right():
    head.direction = "right"

def go_left():
    head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# Keyboard bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")

# Main game loop
while True:
    window.update()
    move()
    time.sleep(delay)

window.mainloop()
