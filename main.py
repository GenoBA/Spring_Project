import turtle
screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("deepskyblue2")
t=turtle.Turtle()
t.speed(3)
#begin
t.penup()
t.goto(0, 250)
t.pendown()
t.write("Spring Scene", font=("Arial", 45, "bold"), align="center")
t.penup()

#grass
t.goto(-350,-400)
t.begin_fill()
t.fillcolor('green')
t.goto(350,-400)
t.goto(350,-250)
t.goto(-350,-250)
t.goto(-350,-400)
t.end_fill()

#toppetal
t.goto(0,-200)
t.fillcolor('red')
t.begin_fill()
t.circle(10)
t.end_fill()
#leftpetal
t.goto(-10,-210)
t.fillcolor('red')
t.begin_fill()
t.circle(10)
t.end_fill()
#rightpetal
t.goto(10,-210)
t.fillcolor('red')
t.begin_fill()
t.circle(10)
t.end_fill()
#bottompetal
t.goto(0,-220)
t.fillcolor('red')
t.begin_fill()
t.circle(10)
t.end_fill()
#yellowpart
t.goto(0,-208)
t.fillcolor('yellow')
t.begin_fill()
t.circle(8)
t.end_fill()
#grasspart
t.goto(-3,-250)
t.begin_fill()
t.fillcolor('green')
t.goto(3,-250)
t.goto(3,-220)
t.goto(-3,-220)
t.goto(-3,-250)
t.end_fill()


#housewall
t.goto(-250,-250)
t.pendown()
t.fillcolor('firebrick')
t.begin_fill()
t.goto(-100,-250)
t.goto(-100,-75)
t.goto(-250,-75)
t.goto(-250,-250)
t.end_fill()
t.penup()
#roof
t.goto(-175,-75)
t.pendown()
t.fillcolor('rosybrown')
t.begin_fill()
t.goto(-80,-95)
t.goto(-70,-75)
t.end_fill()





turtle.done()