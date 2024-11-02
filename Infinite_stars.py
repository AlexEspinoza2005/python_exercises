import turtle

window = turtle.Screen()
window.bgcolor("black")
star_turtle = turtle.Turtle()
star_turtle.speed(0)
star_turtle.color('red')

star_limit = 330

for i in range(star_limit):
    star_turtle.forward(i * 3)
    star_turtle.right(145)

window.exitonclick()
