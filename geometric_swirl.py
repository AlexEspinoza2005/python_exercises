import turtle

window = turtle.Screen()
window.bgcolor("black")

triangle_turtle = turtle.Turtle()
triangle_turtle.speed(0)
triangle_turtle.width(2)
triangle_turtle.color("orange")

num_triangles = 150
angle = 60

for i in range(num_triangles):
    for _ in range(3): 
        triangle_turtle.forward(i * 3)  
        triangle_turtle.left(120)       
    triangle_turtle.left(5)  