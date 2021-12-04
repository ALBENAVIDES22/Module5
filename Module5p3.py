#Alberto Benavides
#11-04-2021
#Ask the user the number of sides , length of sides , color of outline, and the fill color

import turtle

alex = turtle.Turtle ()
Kayla = turtle.Screen ()

sides_number = int(input("Enter the number of sides you want"))
sides_length = int(input("Enter the length of each side"))
outline_color = input("Enter the color of the outline")
fill_color = input("Enter the fill color of your shape")

alex.color(outline_color)
alex.fillcolor(fill_color)
alex.begin_fill()
for i in range(sides_number):
    alex.forward(sides_length)
    alex.left(360 / sides_number)
alex.end_fill()
#360 / 4 = 90
#360 / 6 = 60
#360 / 8 = 45
Kayla.exitonclick()