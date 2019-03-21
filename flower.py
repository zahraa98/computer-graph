import turtle
m=turtle.Turtle()
turtle.bgcolor('black')
m.pencolor("white")
def flower():
     for i in range(13):
         m.left(36)
         m.circle(60,60)
         m.left(120)
         m.circle(60,60)
flower()
m.hideturtle()
turtle.done()