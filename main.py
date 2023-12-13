from turtle import *
hideturtle()
speed(0)
bgcolor("black")
setup(1.0, 1.0)

def writeUP(name):
    color("yellow")
    if name == "":
         name = "Your name!!!"
    penup()
    goto(0, 300)
    pendown()
    write("Merry", True, align="center", font=("Arial", 30, "normal"))
    penup()
    goto(0, 260)
    pendown()
    write("Christmas", True, align="center", font=("Arial", 30, "normal"))
    penup()
    goto(300, -260)
    pendown()
    write(name, True, "center", ("Arial", 30, "italic"))

def pretty_circles():
    for x in range(4):
        for colors in ["white", "red", "orange", "yellow", "blue", "green", "indigo", "violet"]:
            color(colors)
            left(12)
            for i in range(2):
                circle(50)

name = textinput("Input", "Please Enter Your Name: ")
writeUP(name)
size = -400
for i in range(3):
    penup()
    goto(size, 0)
    pendown()
    pretty_circles()
    size += 400
size = -400
for i in range(3):
    penup()
    goto(-400, -300) if i == 2 else goto(size, 300)
    pendown()
    pretty_circles()
    size += 800

while True:
    clear()
    penup()
    goto(0, 0)
    pendown()
    for x in range(4):
        for colors in ["white", "red", "orange", "yellow", "blue", "green", "indigo", "violet"]:
            color(colors)
            for i in range(2):
                circle(50)
            left(400)
    penup()
    goto(-10, 0)
    pendown()
    write("Thank You", True, align="center", font=("Arial", 40, "normal"))
exitonclick()

