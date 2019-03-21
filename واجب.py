import turtle
m=turtle.Turtle()
m.speed(300)
turtle.bgcolor("black")
color=['red','blue','green','pink']
for i in range(200):
    m.pencolor(color[i % 4])
    m.width(i/100+1)
    m.forward(i)
    m.left(73)
turtle.done()
