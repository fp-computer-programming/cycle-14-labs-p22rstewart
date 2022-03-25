# RTS 3/20/22

# Import turtle moduel
from cgitb import grey
import turtle


window = turtle.Screen()
window.setup()
window.screensize()
window.title("Lab 4")
window.bgcolor("black")


#  Creates color
variable = turtle.Turtle()
variable.shape("turtle")
variable.pencolor("white")
variable.fillcolor("white")
variable.speed(5)
variable.stamp()
variable.setposition(100, 100)

# direction 
variable.begin_fill()
variable.goto(100, 0)
variable.goto(0, 0)
variable.goto(0, 100)
variable.goto(100, 100)
variable.end_fill()

# Keeps open
window.mainloop()
