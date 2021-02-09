
import turtle
import random
#Beginning
key = ['topright', 'tr', 'middleright', 'mr', 'bottomright', 'br', 'topmiddle', 'tm', 'middlemiddle', 'mm', 'bottommiddle', 'bm', 'topleft', 'tl', 'middleleft', 'ml', 'bottomleft', 'bl']
KeyShow = ['Top Right or TR', 'Middle Right or MR', 'Bottom Right or BR', 'Top Middle or TM', 'Middle Middle or MM', 'Bottom Middle or BM', 'Top Left or TL', 'Middle Left or ML', 'Bottom Left or BL']
tr = 0; mr = 0; br = 0; tm = 0; mm = 0; bm = 0; tl = 0; ml = 0; bl = 0;

#Setting Up Turtle Drawings
def drawX():
    for i in range(2):
        t.pendown()
        t.lt(45)
        t.fd(20)
        t.bk(40)
        t.fd(20)
        t.lt(45)
        t.lt(180)
def drawO():
    t.rt(90)
    t.fd(20)
    t.lt(90)
    t.pendown()
    t.circle(20)
def topright():
    t.penup()
    t.goto(100,100)
def middleright():
    t.penup()
    t.goto(100,0)
def bottomright():
    t.penup()
    t.goto(100,-100)
def topmiddle():
    t.penup()
    t.goto(0,100)
def middlemiddle():
    t.penup()
    t.goto(0,0)
def bottommiddle():
    t.penup()
    t.goto(0,-100)
def topleft():
    t.penup()
    t.goto(-100,100)
def middleleft():
    t.penup()
    t.goto(-100,0)
def bottomleft():
    t.penup()
    t.goto(-100,-100)


    
#Starting off
playernum = input('Will there be two players or just one? You can quit anytime by typing "quit". ')
while True:
    if playernum.lower() == 'quit':
        quit()
    if playernum == '2' or playernum.lower() == 'two' or playernum.lower() == 'one'  or  playernum == '1':
        break
    else:
        playernum = input('Sorry, how many players? Please type either the number "1" or "2". ')


#Turtle Setup
t = turtle.Turtle()
aScreen = turtle.Screen()
t.speed('fastest')
def vertical():
    t.pendown()
    t.right(90)
    t.fd(150)
    t.left(180)
    t.fd(300)
    t.right(90)

def horizontal():
    t.pendown()
    t.fd(150)
    t.left(180)
    t.fd(300)
    t.right(180)
    
#Vertical Left Line
t.penup()
t.goto(-50,0)
vertical()

#Vertical Right Line
t.penup()
t.goto(50,0)
vertical()

#Horizontal Top Line
t.penup()
t.goto(0,50)
horizontal()

#Horizontal Bottom Line
t.penup()
t.goto(0,-50)
horizontal()






#One Player
if playernum == '1' or playernum.lower() == 'one':
    first = input('Do you want to be "X" or "O"? ')
    while True:
        if first.lower() == 'quit':
            quit()
        if first.lower() == 'x' or  first.lower() == 'o':
            break
        else:
            first = input('Sorry, type either the letter "X" or "O" ')
    while True:
        if first.lower() == 'x':
            placement1 = input('Where do you want to put the "X"? For the key just type "Key". ')
            pl1 = placement1.strip()
            if pl1.lower() == 'key':
                print(KeyShow)
            elif pl1.lower() in key:
                pl1 = placement1.strip()
            elif pl1.lower() == 'quit':
                quit()
            else:
                print("Sorry that isn't a position or may have been taken already")
                continue
            try:        
                if pl1.lower() == 'topright' or pl1.lower() == 'tr':
                    topright()
                    drawX()
                    key.remove('topright' and 'tr')
                    KeyShow.remove('Top Right or TR')
                    tr = 1

                elif pl1.lower() == 'middleright' or pl1.lower() == 'mr':
                    middleright()
                    drawX()
                    key.remove('middleright' and 'mr')
                    KeyShow.remove('Middle Right or MR')
                    mr = 1

                elif pl1.lower() == 'bottomright' or pl1.lower() == 'br':
                    bottomright()
                    drawX()
                    key.remove('bottomright' and 'br')
                    KeyShow.remove('Bottom Right or BR')
                    br = 1

                elif pl1.lower() == 'topmiddle' or pl1.lower() == 'tm':
                    topmiddle()
                    drawX()
                    key.remove('topmiddle' and 'tm')
                    KeyShow.remove('Top Middle or TM')
                    tm = 1

                elif pl1.lower() == 'middlemiddle' or pl1.lower() == 'mm':
                    middlemiddle()
                    drawX()
                    key.remove('middlemiddle' and 'mm')
                    KeyShow.remove('Middle Middle or MM')
                    mm = 1

                elif pl1.lower() == 'bottommiddle' or pl1.lower() == 'bm':
                    bottommiddle()
                    drawX()
                    key.remove('bottommiddle' and 'bm')
                    KeyShow.remove('Bottom Middle or BM')
                    bm = 1

                elif pl1.lower() == 'topleft' or pl1.lower() == 'tl':
                    topleft()
                    drawX()
                    key.remove('topleft' and 'tl')
                    KeyShow.remove('Top Left or TL')
                    tl = 1

                elif pl1.lower() == 'middleleft' or pl1.lower() == 'ml':
                    middleleft()
                    drawX()
                    key.remove('middleleft' and 'ml')
                    KeyShow.remove('Middle Left or ML')
                    ml = 1

                elif pl1.lower() == 'bottomleft' or pl1.lower() == 'bl':
                    bottomleft()
                    drawX()
                    key.remove('bottomleft' and 'bl')
                    KeyShow.remove('Bottom Left or BL')
                    bl = 1
                Xwin=((tr == 1 and tm == 1 and tl == 1) or(mr == 1 and mm == 1 and ml == 1)or(br == 1 and bm == 1 and bl == 1)or(tr == 1 and mr == 1 and br == 1)or(tm == 1 and mm == 1 and bm == 1)or(tl == 1 and ml == 1 and bl == 1) or(tr == 1 and mm == 1 and bl == 1)or(tl == 1 and mm == 1 and br == 1))
                Owin=((tr == 2 and tm == 2 and tl == 2)or(mr == 2 and mm == 2 and ml == 2)or(br == 2 and bm == 2 and bl == 2)or(tr == 2 and mr == 2 and br == 2)or(tm == 2 and mm == 2 and bm == 2)or(tl == 2 and ml == 2 and bl == 2)or(tr == 2 and mm == 2 and bl == 2)or(tl == 2 and mm == 2 and br == 2))
                if Xwin:
                    print("X has won the game!!")
                    break;
                elif Owin:
                    print("O has won the game")
                    break;
                comp = random.choice(KeyShow)
                if comp == 'Top Right or TR':
                    topright()
                    drawO()
                    key.remove('topright' and 'tr')
                    KeyShow.remove(comp)
                    tr = 2
                    
                elif comp == 'Middle Right or MR':
                    middleright()
                    drawO()
                    key.remove('middleright' and 'mr')
                    KeyShow.remove(comp)
                    mr = 2
                    
                elif comp == 'Bottom Right or BR':
                    bottomright()
                    drawO()
                    key.remove('bottomright' and 'br')
                    KeyShow.remove(comp)
                    br = 2
                    
                elif comp == 'Top Middle or TM':
                    topmiddle()
                    drawO()
                    key.remove('topmiddle' and 'tm')
                    KeyShow.remove(comp)
                    tm = 2
                    
                elif comp == 'Middle Middle or MM':
                    middlemiddle()
                    drawO()
                    key.remove('middlemiddle' and 'mm')
                    KeyShow.remove(comp)
                    mm = 2
                    
                elif comp == 'Bottom Middle or BM':
                    bottommiddle()
                    drawO()
                    key.remove('bottommiddle' and 'bm')
                    KeyShow.remove(comp)
                    bm = 2
                    
                elif comp == 'Top Left or TL':
                    topleft()
                    drawO()
                    key.remove('topleft' and 'tl')
                    KeyShow.remove(comp)
                    tl = 2
                    
                elif comp == 'Middle Left or ML':
                    middleleft()
                    drawO()
                    key.remove('middleleft' and 'ml')
                    KeyShow.remove(comp)
                    ml = 2
                    
                elif comp == 'Bottom Left or BL':
                    bottomleft()
                    drawO()
                    key.remove('bottomleft' and 'bl')
                    KeyShow.remove(comp)
                    bl = 2

                Xwin=((tr == 1 and tm == 1 and tl == 1) or(mr == 1 and mm == 1 and ml == 1)or(br == 1 and bm == 1 and bl == 1)or(tr == 1 and mr == 1 and br == 1)or(tm == 1 and mm == 1 and bm == 1)or(tl == 1 and ml == 1 and bl == 1) or(tr == 1 and mm == 1 and bl == 1)or(tl == 1 and mm == 1 and br == 1))
                Owin=((tr == 2 and tm == 2 and tl == 2)or(mr == 2 and mm == 2 and ml == 2)or(br == 2 and bm == 2 and bl == 2)or(tr == 2 and mr == 2 and br == 2)or(tm == 2 and mm == 2 and bm == 2)or(tl == 2 and ml == 2 and bl == 2)or(tr == 2 and mm == 2 and bl == 2)or(tl == 2 and mm == 2 and br == 2))
                if Xwin:
                    print("X has won the game!!")
                    break;
                elif Owin:
                    print("O has won the game")
                    break;
                if KeyShow == []:
                    print("It's a tie!")
                    break
            except IndexError:
                print("It's a tie!")
                break
        elif first.lower() == 'o':       
            try:
                comp = random.choice(KeyShow)
                if comp == 'Top Right or TR':
                    topright()
                    drawX()
                    key.remove('topright' and 'tr')
                    KeyShow.remove(comp)
                    tr = 1
                if comp == 'Middle Right or MR':
                    middleright()
                    drawX()
                    key.remove('middleright' and 'mr')
                    KeyShow.remove(comp)
                    mr = 1                    
                if comp == 'Bottom Right or BR':
                    bottomright()
                    drawX()
                    key.remove('bottomright' and 'br')
                    KeyShow.remove(comp)
                    br = 1
                        
                if comp == 'Top Middle or TM':
                    topmiddle()
                    drawX()
                    key.remove('topmiddle' and 'tm')
                    KeyShow.remove(comp)
                    tm = 1
                        
                if comp == 'Middle Middle or MM':
                    middlemiddle()
                    drawX()
                    key.remove('middlemiddle' and 'mm')
                    KeyShow.remove(comp)
                    mm = 1
                        
                if comp == 'Bottom Middle or BM':
                    bottommiddle()
                    drawX()
                    key.remove('bottommiddle' and 'bm')
                    KeyShow.remove(comp)
                    bm = 1
                        
                if comp == 'Top Left or TL':
                    topleft()
                    drawX()
                    key.remove('topleft' and 'tl')
                    KeyShow.remove(comp)
                    tl = 1
                        
                if comp == 'Middle Left or ML':
                    middleleft()
                    drawX()
                    key.remove('middleleft' and 'ml')
                    KeyShow.remove(comp)
                    ml = 1
                if comp == 'Bottom Left or BL':
                    bottomleft()
                    drawX()
                    key.remove('bottomleft' and 'bl')
                    KeyShow.remove(comp)
                    bl = 1

                Xwin=((tr == 1 and tm == 1 and tl == 1) or(mr == 1 and mm == 1 and ml == 1)or(br == 1 and bm == 1 and bl == 1)or(tr == 1 and mr == 1 and br == 1)or(tm == 1 and mm == 1 and bm == 1)or(tl == 1 and ml == 1 and bl == 1) or(tr == 1 and mm == 1 and bl == 1)or(tl == 1 and mm == 1 and br == 1))
                Owin=((tr == 2 and tm == 2 and tl == 2)or(mr == 2 and mm == 2 and ml == 2)or(br == 2 and bm == 2 and bl == 2)or(tr == 2 and mr == 2 and br == 2)or(tm == 2 and mm == 2 and bm == 2)or(tl == 2 and ml == 2 and bl == 2)or(tr == 2 and mm == 2 and bl == 2)or(tl == 2 and mm == 2 and br == 2))
                if Xwin:
                    print("X has won the game!!")
                    break;
                elif Owin:
                    print("O has won the game")
                    break;

                placement1 = input('Where do you want to put the "O"? For the key just type "Key". ')
                pl1 = placement1.strip()
                while True:
                    if pl1.lower() in key:
                        break
                    elif pl1.lower() == 'key':
                        print(KeyShow)
                    elif pl1.lower() not in key:
                        placement1 = input("Sorry that isn't a position or may have been taken already, type 'Key' for help and what is left. ")
                        pl1 = placement1.strip()                  
                if pl1.lower() == 'topright' or pl1.lower() == 'tr':
                    topright()
                    drawO()
                    key.remove('topright' and 'tr')
                    KeyShow.remove('Top Right or TR')
                    tr = 2
                    
                if pl1.lower() == 'middleright' or pl1.lower() == 'mr':
                    middleright()
                    drawO()
                    key.remove('middleright' and 'mr')
                    KeyShow.remove('Middle Right or MR')
                    mr = 2
                if pl1.lower() == 'bottomright' or pl1.lower() == 'br':
                    bottomright()
                    drawO()
                    key.remove('bottomright' and 'br')
                    KeyShow.remove('Bottom Right or BR')
                    br = 2
                if pl1.lower() == 'topmiddle' or pl1.lower() == 'tm':
                    topmiddle()
                    drawO()
                    key.remove('topmiddle' and 'tm')
                    KeyShow.remove('Top Middle or TM')
                    tm = 2
                    
                if pl1.lower() == 'middlemiddle' or pl1.lower() == 'mm':
                    middlemiddle()
                    drawO()
                    key.remove('middlemiddle' and 'mm')
                    KeyShow.remove('Middle Middle or MM')
                    mm = 2
                    
                if pl1.lower() == 'bottommiddle' or pl1.lower() == 'bm':
                    bottommiddle()
                    drawO()
                    key.remove('bottommiddle' and 'bm')
                    KeyShow.remove('Bottom Middle or BM')
                    bm = 2
                    
                if pl1.lower() == 'topleft' or pl1.lower() == 'tl':
                    topleft()
                    drawO()
                    key.remove('topleft' and 'tl')
                    KeyShow.remove('Top Left or TL')
                    tl = 2
                    
                if pl1.lower() == 'middleleft' or pl1.lower() == 'ml':
                    middleleft()
                    drawO()
                    key.remove('middleleft' and 'ml')
                    KeyShow.remove('Middle Left or ML')
                    ml = 2
                    
                if pl1.lower() == 'bottomleft' or pl1.lower() == 'bl':
                    bottomleft()
                    drawO()
                    key.remove('bottomleft' and 'bl')
                    KeyShow.remove('Bottom Left or BL')
                    bl = 2
                #Determin Winner
                Xwin=((tr == 1 and tm == 1 and tl == 1) or(mr == 1 and mm == 1 and ml == 1)or(br == 1 and bm == 1 and bl == 1)or(tr == 1 and mr == 1 and br == 1)or(tm == 1 and mm == 1 and bm == 1)or(tl == 1 and ml == 1 and bl == 1) or(tr == 1 and mm == 1 and bl == 1)or(tl == 1 and mm == 1 and br == 1))
                Owin=((tr == 2 and tm == 2 and tl == 2)or(mr == 2 and mm == 2 and ml == 2)or(br == 2 and bm == 2 and bl == 2)or(tr == 2 and mr == 2 and br == 2)or(tm == 2 and mm == 2 and bm == 2)or(tl == 2 and ml == 2 and bl == 2)or(tr == 2 and mm == 2 and bl == 2)or(tl == 2 and mm == 2 and br == 2))
                if Xwin:
                    print("X has won the game!!")
                    break;
                elif Owin:
                    print("O has won the game")
                    break;
                if KeyShow == []:
                    print("It's a tie!")
                    break
            except IndexError:
                print("It's a tie!")
                break









