import turtle
turtle.bgcolor("black")
turtle.screensize(900,900)
turtle.penup()
turtle.goto(300,-350)
turtle.pendown()
#start of filling process
turtle.fillcolor("red")
turtle.begin_fill()
#drawing the shape
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
#end fill to finish filling process
turtle.end_fill()
turtle.penup()
turtle.goto(350,-250)
turtle.pendown()
turtle.left(90)
turtle.pencolor("black")
turtle.forward(25)
turtle.pencolor("white")
turtle.shape("circle")
turtle.color("white")
turtle.speed(0)
for i in range(43):
    turtle.forward(15)
    turtle.left(2)
turtle.right(2)
turtle.color("orange")
turtle.shapesize(5)
turtle.pencolor("purple")
length = 2

ts=turtle.clone()
for i in range (150):
    ts.speed(0)
    ts.color("gold")
    ts.shapesize(1)
    ts.shape("circle")
    ts.forward(length)
    ts.right(88)
    ts.color("orange")
    ts.forward(length)
    ts.right(100)
    ts.color("red")
    ts.forward(length)
    ts.right(44)
    ts.color("orange")

    length+=3
turtle.done()

