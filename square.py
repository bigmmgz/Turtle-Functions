#!/usr/bin/env python

print("hello")

import turtle

def square(t,x:float,y:float):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        t.left(90)
        t.forward(100)

def quit():
    turtle.bye()

#create my main turtle
my_turtle=turtle.Turtle()
#tell the screen to listen for kay events
turtle.Screen().listen()
#in the escape kay is pressed exit
turtle.onkeypress(quit,key="Escape")
#enter main loop so window stays in view
square(my_turtle,-100,-100)
turtle.mainloop()