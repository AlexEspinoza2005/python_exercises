import turtle

window = turtle.Screen()
window.bgcolor("black")

star_turtle = turtle.Turtle()
star_turtle.speed(0)
star_turtle.width(2)
star_turtle.color("yellow")

num_stars = 36
angle = 360 / num_stars

for _ in range(num_stars):
    for _ in range(5):  
        star_turtle.forward(100)
        star_turtle.right(144)
    star_turtle.right(angle) 