import turtle

def rec_turtle(r):

    if r >= 10:
        turtle.pendown()
        turtle.circle(r)
        turtle.penup()

        for j in range(4):
            turtle.left(90)
            turtle.forward(r)
            turtle.left(90)
            turtle.forward(r)
            turtle.left(90)

            rec_turtle(r / 2)

if __name__ == '__main__':
    turtle.color('purple')
    turtle.speed="fastest"
    rec_turtle(100)
    turtle.exitonclick()

