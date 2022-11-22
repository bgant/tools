import turtle
import random

def triangle():
    for side in range(3):
        turtle.forward(100)
        turtle.right(120)

def draw():
    colors=['red','orange','yellow','green','blue']
    for j in range(72):
        turtle.color(random.choice(colors))
        triangle()
        turtle.left(5)

if __name__ == '__main__':
    turtle.speed = "fastest"
    draw()

