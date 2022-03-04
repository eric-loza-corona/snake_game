#importing libraries and modules
import turtle
import time
import random


# head of the snake

head = turtle.Turtle()
head.shape("triangle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"