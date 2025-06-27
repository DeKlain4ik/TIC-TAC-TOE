import turtle 

screen = turtle.Screen()
a = turtle.Turtle()
a.speed(1000)
screen.bgcolor("moccasin")
a.pensize(2)

end = False

player1 = True
player2 = False

bot_game = False
game = False


x = [0, 0, 0, 0, 0, 0, 0, 0, 0]

o = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def bot():
    global player1
    win()
    if bot_game == True and end == False:
        for i in range(9):
            if x[i] == 0 and o[i] == 0:
                column = i % 3
                row = i // 3

                x_pos = -150 + column * 100
                y_pos = 150 - row * 100

                circle(x_pos + 50, y_pos - 100)
                o[i] = 1
                print("Бот сделал ход")
                player1 = True
                break
            
def main_menu():
    a.clear()
    goto(-80, 150)
    a.write("Крестики-нолики", font=("Arial", 24, "normal"))
    goto(-100, 0)
    a.pencolor("red")
    a.setheading(45) 
    a.pendown()
    a.forward(125)   

    goto(-100, 90)
    a.pendown()
    a.setheading(-45)  
    a.forward(125)
    a.penup()
    a.pencolor("black")
    a.setheading(0)

    a.pencolor("blue")
    goto(120, 0)
    a.circle(45)
    a.pencolor("black")

    # кнопка играть 1 на 1
    goto(-280, -200)
    for i in range(2):
        a.forward(250)
        a.left(90)
        a.forward(125)
        a.left(90)  
    goto(-240, -140)
    a.write("1 на 1", font=("Arial", 24, "normal"))

    # против бота
    goto(200, -200)
    a.setheading(0)
    for i in range(2):
        a.forward(250)
        a.left(90)
        a.forward(125)
        a.left(90)  
    goto(240, -140)
    a.write("против бота", font=("Arial", 24, "normal"))
    goto(1000, 1000)

def start_game(x_click, y_click):
    if (-280 < x_click < -30 and -200 < y_click < -75):
        global game
        game = True
        a.clear()
        print("Игра запущена!")
        start()
    if (200 < x_click < 450 and -200 < y_click < -75):
        global bot_game, end
        bot_game = True
        end = False
        a.clear()
        print("Игра запущена!")
        start_bot()



def start_bot():
    if bot_game == True:
        goto(-150, 200)
        a.write("Что бы вернуться в меню нажмите Escp", font=("Arial", 24, "normal"))
        cell()
        screen.onclick(attack2)

def start():
    if game == True:
        goto(-150, 200)
        a.write("Что бы вернуться в меню нажмите Escp", font=("Arial", 24, "normal"))
        cell()
        screen.onclick(attack1)
        

def back_to_menu():
    global game, x, o, end, player1, player2
    game = False
    end = False
    player1 = True
    player2 = False
    
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    o = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    a.speed(1000)
    main_menu()
    screen.onclick(start_game)

def goto(x, y):
    a.penup()
    a.goto(x, y)
    a.pendown()

def win():
    global end
    if x[0] and x[1] and x[2] == 1:
        a.pensize(5)
        goto(-150, 100)
        a.goto(150, 100)
        print("Игрок 1 победил!")
        end = True
        a.pensize(2)
    elif x[3] and x[4] and x[5] == 1:
        a.pensize(5)
        goto(-150, 0)
        a.goto(150, 0)
        print("Игрок 1 победил!")
        end = True
        a.pensize(2)
    elif x[6] and x[7] and x[8] == 1:
        a.pensize(5)
        goto(-150, -100)
        a.goto(150, -100)
        print("Игрок 1 победил!")
        end = True
        a.pensize(2)
    elif x[0] and x[3] and x[6] == 1:
        a.pensize(5)
        goto(-100, 150)
        a.goto(-100, -150)
        print("Игрок 1 победил!")
        end = True
        a.pensize(2)
    elif x[1] and x[4] and x[7] == 1:
        a.pensize(5)
        goto(0, 150)
        a.goto(0, -150)
        print("Игрок 1 победил!")
        end = True
        a.pensize(2)
    elif x[2] and x[5] and x[8] == 1:
        a.pensize(5)
        goto(100, 150)
        a.goto(100, -150)
        print("Игрок 1 победил!")
        end = True
        a.pensize(2)
    elif x[0] and x[4] and x[8] == 1:
        a.pensize(5)
        goto(-150, 150)
        a.goto(150, -150)
        print("Игрок 1 победил!")
        end = True
        a.pensize(2)
    elif x[2] and x[4] and x[6] == 1:
        a.pensize(5)
        goto(150, 150)
        a.goto(-150, -150)
        print("Игрок 1 победил!")
        end = True
        a.pensize(2)
    elif o[0] and o[1] and o[2] == 1:
        a.pensize(5)
        goto(-150, 100)
        a.goto(150, 100)
        print("Игрок 2 победил!")
        end = True
        a.pensize(2)
    elif o[3] and o[4] and o[5] == 1:
        a.pensize(5)
        goto(-150, 0)
        a.goto(150, 0)
        print("Игрок 2 победил!")
        end = True
        a.pensize(2)
    elif o[6] and o[7] and o[8] == 1:
        a.pensize(5)
        goto(-150, -100)
        a.goto(150, -100)
        print("Игрок 2 победил!")
        end = True
        a.pensize(2)
    elif o[0] and o[3] and o[6] == 1:
        a.pensize(5)
        goto(-100, 150)
        a.goto(-100, -150)
        print("Игрок 2 победил!")
        end = True
        a.pensize(2)
    elif o[1] and o[4] and o[7] == 1:
        a.pensize(5)
        goto(0, 150)
        a.goto(0, -150)
        print("Игрок 2 победил!")
        end = True
        a.pensize(2)
    elif o[2] and o[5] and o[8] == 1:
        a.pensize(5)
        goto(0, 150)
        a.goto(100, -150)
        print("Игрок 2 победил!")
        end = True
        a.pensize(2)
    elif o[0] and o[4] and o[8] == 1:
        a.pensize(5)
        goto(-150, 150)
        a.goto(150, -150)
        print("Игрок 2 победил!")
        end = True
        a.pensize(2)
    elif o[2] and o[4] and o[6] == 1:
        a.pensize(5)
        goto(150, 150)
        a.goto(-150, -150)
        print("Игрок 2 победил!")
        end = True
        a.pensize(2)

def attack2(x_click, y_click):
    global player1 
    player1 = True
    win() 
    if (-150 < x_click < 150 and -150 < y_click < 150) and end == False:

        сolumn = (x_click + 150) // 100 
        row = (150 - y_click) // 100  
        cell = int(row * 3 + сolumn)  

        if x[cell] != 0 or o[cell] != 0:
            print("Клетка занята!!")
            return
        x_pos = -150 + сolumn * 100
        y_pos = 150 - row * 100

        if player1 == True:
            cross(x_pos, y_pos, x_pos + 100, y_pos)  
            x[cell] = 1  
            player1 = False  
            bot()        
    print(x)
    print(o)

def attack1(x_click, y_click):
    global player1, player2  


    if  (-150 < x_click < 150 and -150 < y_click < 150) and not end:

        сolumn = (x_click + 150) // 100 
        row = (150 - y_click) // 100  
        cell = int(row * 3 + сolumn)  

        if x[cell] != 0 or o[cell] != 0:
            print("Клетка занята!!")
            return
        x_pos = -150 + сolumn * 100
        y_pos = 150 - row * 100

        if player1 == True:
            cross(x_pos, y_pos, x_pos + 100, y_pos)  
            x[cell] = 1  
            player1 = False  
            player2 = True
        else:
            circle(x_pos + 50, y_pos - 100)  
            o[cell] = 1  
            player1 = True  
            player2 = False
        
        win()  
            
    print(x)
    print(o)

def cross(x, y, z, k):
    a.pencolor("red")
    goto(x, y)
    a.setheading(315)
    a.forward(140)
    a.penup()
    a.goto(z, k)
    a.pendown()
    a.setheading(225)
    a.forward(140)
    a.pencolor("black")

def circle(x, y):
    goto(x, y)
    a.setheading(0)
    a.pencolor("blue")
    a.circle(50)
    a.pencolor("black")

def square():
    a.setheading(0)
    for i in range(4):
        a.forward(100)
        a.right(90)

# Игровое поле
def cell():
    goto(-150, 150)

    for i in range(3):
        square()
        a.forward(100)

    goto(-150, 50)

    for i in range(3):
        square()
        a.forward(100)

    goto(-150, -50)

    for i in range(3):
        square()
        a.forward(100)

    a.speed(3)

