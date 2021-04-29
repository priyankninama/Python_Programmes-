import turtle             
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)

# import turtle  

# slider = turtle.Turtle()
# slider.fillcolor('orange')
# Num_sides = int(input("Enter Number of side: "))
# Side_length = int(input("Enter length of side: "))
# angle = 360.0 / Num_sides
# for i in range(Num_sides):
#    slider.forward(Side_length)           
#    slider.right(angle)
   
# turtle.done()
