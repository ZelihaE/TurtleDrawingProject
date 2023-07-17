import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#c3b5e8")
drawing_board.title("Python Turtle")

'''
#square
turtle_instance = turtle.Turtle()

for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)
'''

'''
#star
turtle_instance1 = turtle.Turtle()

turtle_instance1.forward(100)
turtle_instance1.left(36)
turtle_instance1.backward(100)
turtle_instance1.left(36)
turtle_instance1.forward(100)
turtle_instance1.left(36)
turtle_instance1.backward(100)
turtle_instance1.left(36)
turtle_instance1.forward(100)
'''

'''
#star2
turtle_instance1 = turtle.Turtle()
for i in range(5):
    turtle_instance1.right(144)
    turtle_instance1.forward(100)
'''

#polygon
turtle_instance2 = turtle.Turtle()
num_sides = 6
angle = 360.0 / num_sides
side_lenght = 100

for i in range(num_sides):
    turtle_instance2.right(angle)
    turtle_instance2.forward(side_lenght)

turtle.done()