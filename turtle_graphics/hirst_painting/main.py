# import colorgram
# colors = colorgram.extract(r"C:\Python\turtle_graphics\hirst_painting\painting.jpg",30)
# colours_list = []
# for i in range(30):
#     first_color = colors[i]
#     rgb = first_color.rgb
#     red,green,blue = rgb[0],rgb[1],rgb[2]
#     colours_list.append((red,green,blue))
# print(colours_list)
from turtle import Turtle,Screen
import random
screen = Screen()
screen.colormode(255)
colours_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149),
                (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.penup()
def random_color():
    choice = random.choice(colours_list)
    return choice
x_cord = 0.00
y_cord = 0.00

#Method_1
# tim.setheading(225)
# tim.forward(350)
# tim.setheading(0)
# num_dots = 100
# for i in range(1,num_dots+1):
#     tim.dot(20,random_color())
#     tim.forward(50)
#     if i%10==0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)

#Method 2
# Loop to create a grid of circles with random colors
for i in range(10):
    for j in range(10):
        tim.goto(x_cord, y_cord)
        tim.dot(20,random_color())
        # tim.color(random_color())
        # tim.begin_fill()
        # tim.circle(10)
        # tim.end_fill()
        x_cord += 40
    y_cord += 40
    x_cord = 0.00
    
tim.hideturtle()
# Exit on click
screen.exitonclick()