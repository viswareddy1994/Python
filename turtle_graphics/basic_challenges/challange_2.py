from turtle import Turtle,_Screen,Screen

timmy = Turtle()
timmy.shape("turtle")
# timmy.color("red")
def create_shape(sides,color):
    timmy.color(color)
    right_angle = 360/sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(right_angle)
dict = {
    3:"red",4:"green",5:"blue",6:"orange",7:"black",8:"yellow",9:"indigo",10:"maroon"
}

for size,color in dict.items():
    create_shape(size,color)

    







screen = Screen()
screen.exitonclick()