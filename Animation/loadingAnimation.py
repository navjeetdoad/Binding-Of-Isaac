from pygame import *

screen = display.set_mode((1000,600))
#####loading
intro=image.load('introScreen.jpg')
load=image.load('loadingScreen.jpg')
bg=image.load('bg.png')
#####resizing
beginningScreen=transform.scale(intro,(1000,600))
loadScreen=transform.scale(load,(1000,600))
bgScreen=transform.scale(bg,(1000,600))

##isaac1=image.load('Isaac/isaac001.png')
##isaac2=image.load('Isaac/isaac002.png')
##isaac3=image.load('Isaac/isaac003.png')
##isaac4=image.load('Isaac/isaac004.png')
##isaac5=image.load('Isaac/isaac005.png')
##isaac6=image.load('Isaac/isaac006.png')
##isaac7=image.load('Isaac/isaac007.png')
##isaac8=image.load('Isaac/isaac008.png')
##isaac9=image.load('Isaac/isaac009.png')
##isaac10=image.load('Isaac/isaac010.png')
##isaac11=image.load('Isaac/isaac011.png')
##isaac12=image.load('Isaac/isaac012.png')
##
##isaac001=transform.scale(isaac1,(200,200))
##isaac002=transform.scale(isaac2,(200,200))
##isaac003=transform.scale(isaac3,(200,200))
##isaac004=transform.scale(isaac4,(200,200))
##isaac005=transform.scale(isaac5,(200,200))
##isaac006=transform.scale(isaac6,(200,200))
##isaac007=transform.scale(isaac7,(200,200))
##isaac008=transform.scale(isaac8,(200,200))
##isaac009=transform.scale(isaac9,(200,200))
##isaac010=transform.scale(isaac10,(200,200))
##isaac011=transform.scale(isaac11,(200,200))
##isaac012=transform.scale(isaac12,(200,200))

def introScreen():
    
    screen.blit(beginningScreen,(0,0))

def moveIsaac():
    
    global move, frame
    keys = key.get_pressed()

    newMove = -1
    if keys[K_DOWN]:
        newMove = DOWN
        isaac[1] += 4
    elif keys[K_LEFT]:
        newMove = LEFT
        isaac[0] -= 4
    elif keys[K_RIGHT]:
        newMove = RIGHT
        isaac[0] += 4
    elif keys[K_UP]:
        newMove = UP
        isaac[1] -= 4
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

def drawScene():
    
    screen.blit(bgScreen,(0,0))
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

frame=0
move=0      

isaac=[500,300]

startRect=Rect(396,445,192,58)

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
        myClock.tick(50)
        
    display.flip()
quit()
