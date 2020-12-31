from pygame import *

screen = display.set_mode((1000,600))

#####loading

intro=image.load('gamePics/introScreen.jpg')
bg=image.load('gamePics/bg.png')

#####resizing

beginningScreen=transform.scale(intro,(1000,600))
bgScreen=transform.scale(bg,(1000,600))

def introScreen(): #draws the screen
    
    screen.blit(beginningScreen,(0,0))

def moveIsaac(): #actually moving the character
    
    global move, frame
    keys = key.get_pressed()

    newMove = -1
    if keys[K_DOWN]:
        newMove = DOWN
        isaac[1] += 3.5
    elif keys[K_LEFT]:
        newMove = LEFT
        isaac[0] -= 3.5
    elif keys[K_RIGHT]:
        newMove = RIGHT
        isaac[0] += 3.5
    elif keys[K_UP]:
        newMove = UP
        isaac[1] -= 3.5
    else:
        frame = 0

    if move == newMove:    
        frame = frame + 0.5
        if frame >= len(pics[move]):
            frame = 1
            
    elif newMove != -1:     
        move = newMove      
        frame = 1

def makeMove(name,start,end):
    
    move = []
    for i in range(start,end+1):
        move.append(image.load("%s/%s%03d.png" % (name,name,i)))
    
    return move

def drawScene(): #drawing the background
    
    screen.blit(bgScreen,(0,0))
    pic = pics[move][int(frame)]
    screen.blit(pic,(isaac[0]-pic.get_width()//2,isaac[1]-pic.get_height()//2))            
    display.flip()
    
def wallCollision(): #makes sure isaac doesnt go off screen
    
    if isaac[0]<=50:
        isaac[0]=50
    if isaac[0]>=950:
        isaac[0]=950
    if isaac[1]<=50:
        isaac[1]=50
    if isaac[1]>=540:
        isaac[1]=540
        
RIGHT = 0 
DOWN = 1  
UP = 2
LEFT = 3

pics = [] 
pics.append(makeMove("Isaac",7,9))      #DOWN  (S) 1 3
pics.append(makeMove("Isaac",1,3))      #LEFT  (A) 4 6 
pics.append(makeMove("Isaac",10,12))    #RIGHT (D) 7 9
pics.append(makeMove("Isaac",4,6))      #UP    (W)10 12

frame=0
move=0      

isaac=[500,300]

startRect=Rect(396,445,192,58)
roomRect=Rect(50,46,920,509)

game=False
running = True
myClock = time.Clock()

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    
    introScreen()

    if startRect.collidepoint(mx,my):
        if evnt.type==MOUSEBUTTONDOWN:
            game=True

    if game==True:
        
        moveIsaac()          
        drawScene()
        wallCollision()
        myClock.tick(50)

    display.flip()
quit()
