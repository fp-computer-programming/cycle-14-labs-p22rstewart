# RTS 3/20/22

# Import turtle moduel
from cgitb import grey
import turtle


window = turtle.Screen()
window.setup(500, 500)
window.screensize(100,100)
window.title("Lab 3")
window.bgcolor("grey")

# Creates color 
nolan = turtle.Turtle()
nolan.shape("turtle")
nolan.pencolor("green")


for x in range(200):
    nolan.back(200)
    nolan.right(120)

# Keeps open
window.mainloop()
