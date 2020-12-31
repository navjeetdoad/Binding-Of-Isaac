from pygame import *

screen = display.set_mode((600,600))

def moveIsaac():
    
    global move, frame
    keys = key.get_pressed()

    
    newMove = -1
    if keys[K_DOWN]:
        newMove = DOWN
        isaac[1] += 2
    elif keys[K_LEFT]:
        newMove = LEFT
        isaac[0] -= 2
    elif keys[K_RIGHT]:
        newMove = RIGHT
        isaac[0] += 2
    elif keys[K_UP]:
        newMove = UP
        isaac[1] -= 2
    else:
        frame = 0

    if move == newMove:    
        frame = frame + 0.25 
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
    screen.fill((200,222,255))
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

running = True
myClock = time.Clock()

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        
    moveIsaac()          
    drawScene()
    
    myClock.tick(50)
    
quit()
