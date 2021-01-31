#Import Turtle Library
import turtle

#Creating a turtle pen
pen = turtle.Turtle()
# window = turtle.Screen()

#Set the fill Color
pen.fillcolor('yellow')

#start the fill Color
pen.begin_full()

#drawing the circle of radius r
pen.up()
pen.goto(0,-120)
pen.circle(200)

#ending the fill of the Color
pen.end_fill()

#eye1 White
pen.fillcolor("white")
pen.begin_fill()
pen.up()
pen.goto(-70,130)
pen.down()
pen.pensize(2)
pen.circle(40)
pen.end_fill()

#eye1 Black
pen.fillcolor("black")
pen.begin_fill()
pen.up()
pen.goto(-70,140)
pen.down()
pen.circle(20)
pen.end_fill()

#eye2 White
pen.fillcolor("white")
pen.begin_fill()
pen.up()
pen.goto(70,130)
pen.down()
pen.pensize(2)
pen.circle(40)
pen.end_fill()

#eye2 Black
pen.fillcolor("black")
pen.begin_fill()
pen.up()
pen.goto(70,140)
pen.down()
pen.circle(20)
pen.end_fill()

#Mouth
pen.up()
pen.goto(-100,20)
pen.down()
pen.pensize(5)
pen.right(90)
pen.circle(100, 180)
pen.left(90)
pen.forward(200)

#Nose
pen.fillcolor("red")
pen.begin_fill()
pen.up()
pen.goto(30,80)
pen.down()
pen.right(60)
pen.forward(60)
pen.left(120)
pen.forward(60)
pen.left(120)
pen.forward(60)
pen.end_fill()

pen.done()


