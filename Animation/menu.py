from pygame import *
from math import*
from random import*
ss=image.load("startscreen.jpg")
ss=transform.scale(ss,(1200,650))
backPic = image.load("bg.png")
screen = display.set_mode((1200,650))

startRect=Rect(408,480,342,77)


def running():
    ''' check the event queue for an quit as well as the keyboard
        for the escape key. return false if either are seen true
        if we make it to the end.
    ''' 
    for evnt in event.get():
        if evnt.type == QUIT:
            return False
        
    keys = key.get_pressed()
    if keys[27]:
        return False
    return True

def moveBadGuys(badGuys, goodX, goodY):
    ''' The AI for the badGuys is real simple. If the goodGuy is left/right
        they move left/right. Same with up/down.
        badGuys - A list of bad guy positions ([x,y] lists)
        goodX, goodY - good guy position
    '''
    for guy in badGuys[:6]:
        if goodX > guy[0] +2:
            guy[0]+=2                    
        elif goodX < guy[0]-2:   
            guy[0]-=2        
        if goodY > guy[1] +2:
            guy[1]+=2
        elif goodY < guy[1]-2:
            guy[1]-=2


def checkHits(badGuys, goodX, goodY):
    ''' Both good and bad guys are circles, so to check hits we just need to check if the
        distance from center to center is < 20.
        For this simple example when they do collide we re-set the bad guy
    '''
    for i, guy in enumerate(badGuys):
        if ((goodX-guy[0])**2 + (goodY-guy[1])**2)**0.5 < 20:
            guy[0], guy[1] = i*200,0

def drawScene1(screen, badGuys, goodX, goodY):
    ''' The scene is very simple. Each bad guy is a red circle, and the good guy is
        a green circle. 
    '''
    for guy in badGuys:
        draw.circle(screen, red, guy, 20)

    display.flip()

    
init()
size = width, height = 1200, 650
screen = display.set_mode(size)
badX, badY = 0,0
red = 255, 0, 0
green = 0, 255, 0
badGuys = [[0,0], [200,0], [400,0], [600, 0],[800, 0],[1000, 0]]    # 6 x,y pairs 
myClock = time.Clock()

def moveIsaac():
    rapid = 0
    bullets = []
    mx,my=mouse.get_pos()
    global move, frame
    keys = key.get_pressed()

    
    newMove = -1
    if keys[K_DOWN]:
        newMove = DOWN
        isaac[1] += 5
    elif keys[K_LEFT]:
        newMove = LEFT
        isaac[0] -= 5
    elif keys[K_RIGHT]:
        newMove = RIGHT
        isaac[0] += 5
    elif keys[K_UP]:
        newMove = UP
        isaac[1] -= 5 
    else:
        frame = 0

    if move == newMove:    
        frame = frame + 0.25 
        if frame >= len(pics[move]):
            frame = 1
    elif newMove != -1:     
        move = newMove      
        frame = 1
    if rapid>0:
        rapid-=1
    if keys[32] and rapid==0:
        rapid = 10
        ang = atan2(my-300,mx-400)
        vx = cos(ang)*2
        vy = sin(ang)*2
        bullets.append([400,300,vx,vy])
        #print(bullets)

    for b in bullets[:]:
        b[2]*=1.1
        b[3]*=1.1
        b[0]+=b[2]
        b[1]+=b[3]
        if max(b) > 1000 or min(b) < -100:
            bullets.remove(b)

    for b in bullets:
        draw.circle(screen,(255,0,0),(int(b[0]),int(b[1])), 4)
    return isaac[0],isaac[1] 

def makeMove(name,start,end):
    
    move = []
    for i in range(start,end+1):
        move.append(image.load("%s/%s%03d.png" % (name,name,i)))
        
    return move


def drawScene():
    offset=250-isaac[0]
    offsety=250-isaac[1]
    screen.blit(backPic,(offset,offsety))
    pic = pics[move][int(frame)]
    screen.blit(pic,(isaac[0]-pic.get_width()//2,isaac[1]-pic.get_height()//2))            
    display.flip()


RIGHT = 0 
DOWN = 1  
UP = 2
LEFT = 3


pics = [] 
pics.append(makeMove("Isaac",7,9))      #DOWN  (S) 1 3
pics.append(makeMove("Isaac",1,3))      #LEFT  (A) 4 6 
pics.append(makeMove("Isaac",10,12))    #RIGHT (D) 7 9
pics.append(makeMove("Isaac",4,6))      #UP    (W)10 12

print(len(pics))
frame=0     
move=0      

isaac=[300,300]

myClock = time.Clock()

def menu():
    start=''
    running = True
    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
        # --------------------------------------------------
        
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        draw.rect(screen,(111,111,111),startRect) 
        screen.blit(ss,(0,0))

        if startRect.collidepoint(mx,my) and mb[0]==1:
            start='true'

        if start=='true':
            moveIsaac()
            drawScene() 
            #goodX, goodY = mouse.get_pos()      # input from the user & move good guy

            moveBadGuys(badGuys, isaac[0], isaac[1])
            checkHits(badGuys, isaac[0], isaac[1])
            drawScene1(screen, badGuys, isaac[0], isaac[1])
            myClock.tick(50)


        # --------------------------------------------------
        display.flip()
page = "menu"
while page != "exit":
    if page == "menu":
        page = menu()