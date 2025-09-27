import turtle
turtle.screensize(900,900)
sides = int(input("give me a number bigger that 2, i will draw a polygone with the number of sides"))
length  = int(input("give me the length of each side"))

for i in range(sides):
    turtle.forward(length)
    banana = (180-((sides - 2) * 180 / sides))
    turtle.right(banana)
    print((sides-2)*180/sides)
# start of filling process

turtle.done()