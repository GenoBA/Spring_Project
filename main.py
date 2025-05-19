import turtle
screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("deepskyblue2")
t=turtle.Turtle()
t.speed(0)
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
t.goto(-175,-55)
t.goto(-280,-75)
t.goto(-260,-95)
t.goto(-175,-75)
t.end_fill()
t.penup()
#glass
t.goto(-187,-115)
t.pendown()
t.begin_fill()
t.fillcolor('white')
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.end_fill()
t.penup()
#door
t.goto(-187,-195)
t.pendown()
t.begin_fill()
t.fillcolor('brown')
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()
t.penup()
#doornob
t.goto(-185,-185)
t.pendown()
t.begin_fill()
t.fillcolor('black')
t.circle(5)
t.end_fill()
t.penup()

#stairs
t.goto(-187,-195)
t.begin_fill()
t.fillcolor('gray')
t.pendown()
t.goto(-127,-195)
t.goto(-127,-250)
t.goto(-220,-250)
t.goto(-187,-195)
t.end_fill()
t.penup()

#cloud
t.goto(153,200)
t.begin_fill()
t.fillcolor('white')
t.circle(20)
t.end_fill()
t.goto(137,223)
t.begin_fill()
t.fillcolor('white')
t.circle(20)
t.end_fill()
t.goto(119,200)
t.begin_fill()
t.fillcolor('white')
t.circle(20)
t.end_fill()
t.goto(93,215)
t.begin_fill()
t.fillcolor('white')
t.circle(20)
t.end_fill()
t.goto(100,219)
t.begin_fill()
t.fillcolor('white')
t.circle(20)
t.end_fill()

#bird
t.goto(0,190)
t.begin_fill()
t.fillcolor('yellow')
t.goto(10,200)
t.goto(20,170)
t.goto(10,180)
t.goto(0,160)
t.goto(-10,180)
t.goto(-20,170)
t.goto(-10,200)
t.goto(0,190)
t.end_fill()
#beak
t.goto(0,189)
t.begin_fill()
t.fillcolor('orange')
t.goto(5,180)
t.goto(0,175)
t.goto(-5,180)
t.goto(0,180)
t.end_fill()

#pond
t.goto(45,-335)
t.begin_fill()
t.fillcolor('blue')
t.setheading(130)
for i in range(2):
    t.circle(20,90)
    t.circle(10,90)
t.end_fill()
t.goto(46,-341)
t.begin_fill()
t.fillcolor('blue')
t.setheading(130)
for i in range(2):
    t.circle(20,90)
    t.circle(10,90)
t.end_fill()
t.goto(42,-335)
t.begin_fill()
t.fillcolor('blue')
t.setheading(130)
for i in range(2):
    t.circle(20,90)
    t.circle(10,90)
t.end_fill()
t.goto(45,-338)
t.begin_fill()
t.fillcolor('blue')
t.setheading(130)
for i in range(2):
    t.circle(20,90)
    t.circle(10,90)
t.end_fill()

t.goto(355,400)
t.begin_fill()
t.fillcolor('yellow')
t.circle(70)
t.end_fill()

#tree
#step1:log
t.goto(150,-250)
t.fillcolor('brown')
t.begin_fill()
t.goto(170,-250)
t.goto(170,10)
t.goto(150,10)
t.goto(150,-250)
t.end_fill()
#step2:leaves1
t.goto(165,-210)
t.begin_fill()
t.fillcolor('green')
t.goto(235,-210)
t.goto(170,-100)
t.goto(150,-100)
t.goto(85,-210)
t.goto(150,-210)
t.end_fill()
#step3:leaves2
t.goto(165,-100)
t.begin_fill()
t.fillcolor('green')
t.goto(235,-100)
t.goto(160,30)
t.goto(85,-100)
t.goto(150,-100)
t.end_fill()
#onion
t.goto(150,-250)
t.fillcolor('red')
t.begin_fill()
t.circle(15)
t.end_fill()


















turtle.done()