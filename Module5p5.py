#Alberto Benavides
#12-03-2021
#Create the shape

import turtle

john = turtle.Turtle ()
christian = turtle.Screen ()

sides_number = int(input("Enter the number of sides you want"))
sides_length = int(input("Enter the length of each side"))
outline_color = input("Enter the color of the outline")
fill_color = input("Enter the fill color of your shape")

john.color(outline_color)
john.fillcolor(fill_color)
john.begin_fill()
for i in range(sides_number):
    john.forward(sides_length)
    john.left(360 / sides_number)
john.end_fill()
christian.exitonclick()