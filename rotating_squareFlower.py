import turtle

window = turtle.Screen()
window.bgcolor("black")

pattern_turtle = turtle.Turtle()
pattern_turtle.speed(0)
pattern_turtle.width(2)
pattern_turtle.color("cyan")

num_squares = 36
angle = 10

for _ in range(num_squares):
    for _ in range(4):  
        pattern_turtle.forward(100)
        pattern_turtle.right(90)
    pattern_turtle.right(angle) 


