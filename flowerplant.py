import turtle

def draw_petal(some_turtle):
    x=0
    while x<200:
        some_turtle.circle(x)
        x+=4
        some_turtle.right(90)
        some_turtle.forward(10)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor ("blue")

    bee = turtle.Turtle()
    bee.color("yellow")
    bee.ht()
    bee.speed(100)
    for i in range(1,200):
        draw_petal(bee)
        

    window.exitonclick()
    

draw_flower()
    
