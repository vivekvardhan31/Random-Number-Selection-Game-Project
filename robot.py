import turtle as t
def rectangle(horizantal , vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizantal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
    
def draw_feet():
    t.speed('fast')
    t.bgcolor('Dodger blue')
    t.goto(-100,-150)
    rectangle(50, 20, 'blue')
    t.goto(-30,-150)
    rectangle(50, 20, 'blue')
draw_feet()

def draw_legs():
    t.goto(-25,-50)
    rectangle(15, 100,'grey')
    t.goto(-55,-50)
    rectangle(-15,100,'grey')
draw_legs()

def draw_body():
    t.goto(-90,100)
    rectangle(100,150,'red')
draw_body()

def draw_arms():
    t.goto(-150,70)
    rectangle(60,15,'grey')
    t.goto(-150,110)
    rectangle(15,40,'grey')

    t.goto(10,70)
    rectangle(60,15,'grey')
    t.goto(55,110)
    rectangle(15,40,'grey')
draw_arms()

def draw_neck():
    t.goto(-50,120)
    rectangle(15,20,'grey')
draw_neck()

def  draw_head():
    t.goto(-85,170)
    rectangle(80,50,'red')
draw_head()

def draw_eyes():
    t.goto(-60,160)
    rectangle(30,10,'white')
    t.goto(-55,155)
    rectangle(5,5,'black')
    t.goto(-40,155)
    rectangle(5,5,'black')
draw_eyes()

def draw_mouth():
    t.goto(-65,135)
    rectangle(40,5,'black')
    t.hideturtle()
draw_mouth()


t.done()

