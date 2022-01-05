import turtle

turtle.hideturtle()
turtle.speed(0)

n:int = 100
color:int = 1
turtle.bgcolor("white")

turtle.setpos(-150,0)
lists:str = ['blue',"red"]
for i in range(148):
    turtle.pencolor(lists[color%2])
    turtle.pensize(6)
    turtle.forward(n)
    turtle.right(123)
    n += 4
    color += 1
turtle.done()