import turtle

wn=turtle.Screen()
leo=turtle.Turtle()
leo.color('red')
leo.speed(20)
leo.shape('turtle')

for i in range(200):
    leo.forward(20+i)
    leo.left(90+i)
wn.exitonclick()


