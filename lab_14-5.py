# RTS 3/20/22

# import turtle moduel
import turtle

# Movment
def move_forward():
    x.forward(50)

def move_backward():
    x.backward(50)

def turn_left():
    x.left(90)

def turn_right():
    x.right(90)


window = turtle.Screen()


x = turtle.Turtle()

# allows for use of keys
window.onkey(move_forward, "Up")
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")

# keeps open
window.listen()
window.mainloop()
