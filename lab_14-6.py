# RTS 3/20/22

# import turtle moduel
import turtle


window = turtle.Screen()


john = turtle.Turtle()

# color and size
john.color(window.textinput("Color?", "What color would you like?"))
size = int(window.textinput("Size?", "What size would you like the turtle to be (1-5)?"))


if size > 5:
    john.shapesize(5)
elif size < 1:
    john.shapesize(1)
else:
    john.shapesize(size)

# movements 
john.begin_fill()
john.forward(100)
john.right(90)
john.forward(100)
john.right(90)
john.forward(100)
john.right(90)
john.forward(100)
john.end_fill()

# keeps open
window.listen()
window.mainloop()
