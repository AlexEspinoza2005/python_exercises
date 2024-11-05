import turtle
window = turtle.Screen()
window.bgcolor("black")

flower_turtle = turtle.Turtle()
flower_turtle.speed(0)
flower_turtle.width(2)
flower_turtle.color("cyan")

num_petals = 36
angle = 360 / num_petals

for _ in range(num_petals):
    flower_turtle.circle(100)  
    flower_turtle.right(angle) 