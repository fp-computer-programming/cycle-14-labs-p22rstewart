# RTS 3/20/22

# Import turtle moduel 
import turtle

window = turtle.Screen()
window.setup(1000, 1000)
window.screensize(100,100)
window.title("Lab 1")

# Creates name 
pierre = turtle.Turtle()


pierre.forward(250)
pierre.right(90)
pierre.forward(100)
pierre.right(90)
pierre.forward(250)
pierre.right(90)
pierre.forward(100)

# Keeps open
window.mainloop()