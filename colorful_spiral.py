import turtle

window = turtle.Screen()
window.bgcolor("black")

spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)
spiral_turtle.width(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

spiral_limit = 150

for i in range(spiral_limit):
    spiral_turtle.color(colors[i % len(colors)])  # Cambia de color en cada iteración
    spiral_turtle.forward(i * 2)
    spiral_turtle.right(59)  # Ajusta el ángulo para cambiar la forma de la espiral
