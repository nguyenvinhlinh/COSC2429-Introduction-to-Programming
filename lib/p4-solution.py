# python -m lib/p4-solution
import turtle

def draw_bar_chart(record_date, large_thick, large_thin, medium_thick, medium_thin):
    '''
      This function will draw the stacked bar chart
      :param record_date: record date (str)
      :param large_thick: a number (int)
      :param large_thin: a number (int)
      :param medium_thick: a number (int)
      :param medium_thin: a number (int)
      :return: none
    '''
    win = turtle.Screen()
    win.title("pizza stacked bar chart")
    pz = turtle.Turtle()
    pz.speed(100)
    pz.penup()                  #Drawing the axis
    pz.setpos(-150,-150)
    pz.pendown()
    pz.forward(200)
    pz.stamp()
    pz.write("Date", font=("TimeNewRomans", 10, "bold"))
    pz.backward(200)
    pz.left(90)
    pz.forward(400)
    pz.stamp()
    pz.write("Pizza Sales", font=("TimeNewRomans", 10, "bold"))
    pz.penup()
    pz.goto(-90,-150)
    pz.pendown()
    pz.up()
    pz.setpos(-95,-170) #To set the position to write date under the bar
    pz.write(record_date, font=("TimeNewRomans", 10, "bold"))
    pz.setpos(-90,-150) #Set position to start drawing stacked bar
    pz.down()
    color_list = ["red", "orange", "gold", "yellow"]
    color_counting = 0 #This help to change color when we use loops
    pizza_amount = [large_thick, large_thin, medium_thick, medium_thin]
    pizza_sales = sum(pizza_amount)
    for i in pizza_amount:      #Loops to draw stacked bar
        bar_width = 50
        bar_height = 5
        pz.fillcolor(color_list[color_counting])
        pz.begin_fill()
        pz.forward(bar_height * i)
        pz.right(90)
        pz.forward(bar_width)
        pz.right(90)
        pz.forward(bar_height * i)
        pz.right(90)
        pz.forward(bar_width)
        pz.right(90)
        pz.forward(bar_height * i)
        pz.end_fill()
        color_counting += 1
    pz.up()
    pz.setpos(-75, -150 + pizza_sales * 5)      #Total of pizza printed on the top
    pz.write(pizza_sales, font=("TimeNewRomans", 10, "bold"))
    pz.goto(130,100)                            #Writing note
    pz.write(": medium thin", font=("TimeNewRomans", 10, "bold"))
    pz.goto(100,100)
    pz.pendown()
    pz.fillcolor("yellow")
    pz.begin_fill()
    for i in range(4):
        pz.forward(20)
        pz.right(90)
    pz.end_fill()
    pz.penup()
    pz.goto(130, 70)
    pz.write(": medium thick",font=("TimeNewRomans", 10, "bold"))
    pz.goto(100,70)
    pz.pendown()
    pz.fillcolor("gold")
    pz.begin_fill()
    for i in range(4):
        pz.forward(20)
        pz.right(90)
    pz.end_fill()
    pz.penup()
    pz.goto(130, 40)
    pz.write(": large thin", font=("TimeNewRomans", 10, "bold"))
    pz.goto(100, 40)
    pz.pendown()
    pz.fillcolor("orange")
    pz.begin_fill()
    for i in range(4):
        pz.forward(20)
        pz.right(90)
    pz.end_fill()
    pz.penup()
    pz.goto(130, 10)
    pz.write(": large thick", font=("TimeNewRomans", 10, "bold"))
    pz.goto(100, 10)
    pz.pendown()
    pz.fillcolor("red")
    pz.begin_fill()
    for i in range(4):
        pz.forward(20)
        pz.right(90)
    pz.end_fill()
    pz.hideturtle()
    win.exitonclick()


draw_bar_chart("26/12/2021", 20,10,15,25)
