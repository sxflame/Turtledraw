import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward (100)
        some_turtle.right(90)

def draw_bigsquare(some_turtle):
    for i in range (1,5):
        some_turtle.forward (200)
        some_turtle.right(90)

#def draw_circle(some_turtle):
   # some_turtle.cirlce(100)
   
def draw_art():
    window = turtle.Screen()
    window.bgcolor ("black")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1000)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)
    for i in range (38,74):
        draw_bigsquare(brad)
        brad.right(10)
        

   # angie = turtle.Turtle()
   # angie.shape("arrow")
   # angie.color("blue")
   # draw_circle(angie)
   
    window.exitonclick()
    
draw_art()
