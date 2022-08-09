import turtle as t

def korea() :
    swidth,sheight=600,400
    t.setup(swidth+10,sheight+10)
    t.screensize(swidth,sheight)
    t.ht()
    t.speed(0)
    t.penup()
    
    def a() :
        t.pendown()
        t.begin_fill()
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(50/3)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50/3)
        t.right(90)
        t.forward(50)
        t.end_fill()
        t.penup()
        t.right(90)
        t.forward(25)
        
    def b() :
        t.left(90)
        t.forward(25/6)
        t.pendown()
        t.begin_fill()
        for i in range(2):
            t.forward(275/6)
            t.right(90)
            t.forward(50/3)
            t.right(90)
        t.penup()
        t.left(180)
        t.forward(25/3)
        t.pendown()
        for i in range(2):
            t.forward(275/6)
            t.left(90)
            t.forward(50/3)
            t.left(90)
        t.end_fill()
        t.penup()
        t.right(180)
        t.forward(25/6)
        t.right(90)
        t.forward(25)

    ###태극
    t.pendown()
    t.left(56.31)
    t.color("blue")
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(50,-180)
    t.circle(100,180)
    t.circle(50,180)
    t.end_fill()

    t.color("red")
    t.fillcolor("red")
    t.begin_fill()
    t.circle(50,-180)
    t.circle(100,180)
    t.circle(50,180)
    t.end_fill()

    ###사괘
    t.penup()
    t.color("black")

    ##건
    t.home()
    t.left(146.31)
    t.forward(150)
    a()
    a()
    a()

    ##곤
    t.home()
    t.right(33.69)
    t.forward(150)
    b()
    b()
    b()

    ##감
    t.home()
    t.left(33.69)
    t.forward(150)
    b()
    a()
    b()

    ##리
    t.home()
    t.right(146.31)
    t.forward(150)
    a()
    b()
    a()

def japan() :
    swidth,sheight=600,400
    t.setup(swidth+10,sheight+10)
    t.screensize(swidth,sheight)
    t.ht()
    t.penup()
    
    t.right(90)
    t.forward(120)
    t.left(90)
    t.color("red")
    t.fillcolor("red")
    t.pendown()
    t.begin_fill()
    t.circle(120)
    t.end_fill()

def nation(x,y,z) :
    swidth,sheight=600,400
    t.setup(swidth+10,sheight+10)
    t.screensize(swidth,sheight)
    t.ht()
    t.speed(0)
    t.penup()
    
    t.goto(-300,200)
    t.pendown()
    t.pencolor(x)
    t.fillcolor(x)
    t.begin_fill()
    for i in range(2):
        t.forward(600)
        t.right(90)
        t.forward(400/3)
        t.right(90)
    t.end_fill()
    t.right(90)
    t.forward(400/3)
    t.left(90)
        
    t.pencolor(y)
    t.fillcolor(y)
    t.begin_fill()
    for i in range(2):
        t.forward(600)
        t.right(90)
        t.forward(400/3)
        t.right(90)
    t.end_fill()
    t.right(90)
    t.forward(400/3)
    t.left(90)
        
    t.pencolor(z)
    t.fillcolor(z)
    t.begin_fill()
    
    for i in range(2):
        t.forward(600)
        t.right(90)
        t.forward(400/3)
        t.right(90)
    t.end_fill()

def power() : 
    p = input("1.대한민국 2. 일본 3. 독일 4. 러시아 5. 네덜란드 6.모두그리기 : ")
    if p=="1" :
        t.reset()
        korea()
        power()
    elif p=="2" :
        t.reset()
        japan()
        power()
    elif p=="3" :
        t.reset()
        nation("black","red","yellow")
        power()
    elif p=="4" :
        t.reset()
        nation("white","blue","red")
        power()
    elif p=="5" :
        t.reset()
        nation("red","white","blue")
        power()
    elif p=="6" :
        t.reset()
        korea()
        t.reset()
        japan()
        t.reset()
        nation("black","red","yellow")
        t.reset()
        nation("white","blue","red")
        t.reset()
        nation("red","white","blue")
        power()
        
    else :
        print("다시 입력하세요")
        power()

power()
