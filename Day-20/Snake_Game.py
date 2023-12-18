from turtle import Turtle, Screen
import time

is_race_on = False
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    new_snake = Turtle(shape="square")
    new_snake.color("white")
    new_snake.penup()
    new_snake.goto(position)
    segments.append(new_snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    for seg in segments:
        seg.forward(20)








screen.exitonclick()
