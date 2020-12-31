#FAISAL AHMED - PERIOD 9 MR MCKENZIE 
#NAVJEET DOAD - PERIOD 7 MR MACONOVIK 
from pygame import *
from math import*
from random import* 

screen = display.set_mode((1000,750))
display.set_caption("Binding Of Isaac Rebirthed Again")#sets the title for pyc file
icon=image.load('enemy1.png') 
icon=transform.scale(icon,(100,100))
display.set_icon(icon)#sets icon for pyc file
print("SPACE to PICK UP POWERUPS - ARROW KEYS TO SHOOT - WASD TO MOVE \n ORBIT POWERUP - KEY O \n LASER POWERUP - RIGHT SHIFT \n LEFT SHIFT AND MOUSE CLICK FOR BOMB \n PRESS BACKARROW TO EXIT INSTRUCTIONS AND MENU SCREEN")
#####loading 

intro=image.load('gamePics/introScreen.jpg')
bg=image.load('gamePics/bg.png')
hrect=image.load('rect.png')
map2=image.load('map2.png')
level3=image.load('room4.jpg')
bossmap=image.load('bossmap.png')
lc=image.load('lc.png')
ins=image.load('instructions.png')
inspic=image.load('rules.png')
rock=image.load('rock.png')
pup=image.load('pu.png')
# bullets 
bull=image.load("bullet.png")
eBull=image.load("Blood.png")
#enemy
eye=image.load("en/enb.png")
#powerups
pspeed=image.load("speed.png")
strength=image.load("strength.png")
orbit=image.load("orbit.png")
laser=image.load("laser.png")
homing=image.load("homing.png")
#powerup popups
speedy=image.load("speedy.png")
strengthy=image.load("strengthy.png")
orbity=image.load("orbity.png")
lasery=image.load("lasery.png")

#retry screen
restartbutton=image.load("restartbutton.png")
exitbutton=image.load("exit.png")
retryscreen=image.load("retry screen.png")
death=image.load('retry screen.png')

powerups=image.load('powerups.png')

arrow1=image.load('up.png')
arrow2=image.load('right.png')
arrow3=image.load('down.png')
arrow4=image.load('arrow.png')

room1opp=image.load('room1.png')
room2opp=image.load('room2.png')
room3opp=image.load('roompu.png')
br1opp=image.load('roomboss.png')

bombpic=image.load('bomb.png')
explosion=image.load('explosionspot.png')
none=image.load('emptybombs.png')

map=image.load('map.png')

#deathscreen 
dead1=image.load('enemy1.png')
dead2=image.load('enemy2.png')
dead3=image.load('enemy3.png')

#hearts 
heart=image.load('hearts/full.png')
threeq=image.load('hearts/threeq.png')
half=image.load('hearts/half.png')
quart=image.load('hearts/q.png')
empty=image.load('hearts/empty.png')

#pu Activation 
key1=image.load('puActivate/pu1.png')
key2=image.load('puActivate/pu2.png')
key3=image.load('puActivate/pu3.png')
key4=image.load('puActivate/pu4.png')

end=image.load('win.png')
#####resizing

beginningScreen=transform.scale(intro,(1000,750))
bgScreen=transform.scale(bg,(1000,600))
end=transform.scale(end,(1000,800))

map2=transform.scale(map2,(1000,600))
level3=transform.scale(level3,(1000,600))
lc=transform.scale(lc,(1000,600))
ins=transform.scale(ins,(1000,750))
inspic=transform.scale(inspic,(600,400))
rock=transform.scale(rock,(50,50))
pup=transform.scale(pup,(1000,600))
bull=transform.scale(bull,(10,10))
eBull=transform.scale(eBull,(30,50))
pspeed=transform.scale(pspeed,(75,75))
strength=transform.scale(strength,(75,75))
orbit=transform.scale(orbit,(75,75))
laser=transform.scale(laser,(75,75))
homing=transform.scale(homing,(75,75)) 
speedy=transform.scale(speedy,(400,400))
strengthy=transform.scale(strengthy,(400,400))
orbity=transform.scale(orbity,(400,400))
lasery=transform.scale(lasery,(400,400))
bossmap=transform.scale(bossmap,(1000,600))

hrect=transform.scale(hrect,(1000,150))
powerups=transform.scale(powerups,(300,50))

arrow1=transform.scale(arrow1,(100,100))
arrow2=transform.scale(arrow2,(100,100))
arrow3=transform.scale(arrow3,(100,100))
arrow4=transform.scale(arrow4,(100,100))

room1opp=transform.scale(room1opp,(300,400))
room2opp=transform.scale(room2opp,(300,400))
room3opp=transform.scale(room3opp,(300,400))
br1opp=transform.scale(br1opp,(300,400))

bombpic=transform.scale(bombpic,(100,100))
explosion=transform.scale(explosion,(100,100))
none=transform.scale(none,(75,75))

restartbutton=transform.scale(restartbutton,(150,150))
exitbutton=transform.scale(exitbutton,(150,150))
death=transform.scale(death,(400,400))
dead1=transform.scale(dead1,(95,60))
dead2=transform.scale(dead2,(95,60))
dead3=transform.scale(dead3,(95,60))

heart=transform.scale(heart,(25,25))
threeq=transform.scale(threeq,(25,25))
half=transform.scale(half,(25,25))
quart=transform.scale(quart,(25,25))
empty=transform.scale(empty,(25,25))

#####variables

startRect = Rect(396,575,192,58)
roomRect = Rect(50,46,920,509) 
insRect=Rect(397,659,136,38)
mapRect=Rect(197,659,136,38)

rockr=Rect(600,300,50,50)
rockr2=Rect(300,300,50,50)
retryRect=Rect(800,400,150,150)
exitRect=Rect(50,400,150,150)

sx=randint(100,450)
sy=randint(300,500)
powerupRect=Rect(sx,sy,75,75) 
stenemyRect=Rect(sx,100,50,50)
stx=randint(450,900) #picks a random location on the screen for the stationary enemies 
sty=randint(300,500)
powerup2Rect=Rect(stx,sty,75,75)
stenemyRect2=Rect(stx,100,50,50)

hits=['true','true','true']
hitsl2=['true','true','true','true']

bullets=[]
orbbull=[]
orbBull2=[]
orbBull3=[]
orbBull4=[]
orbBull5=[]
orbBull6=[]
orbBull7=[]
orbBull8=[]
b2=[]
b3=[]
b4=[]

stlist=[]
bombNum=4

enemybull=[] 
enemybull2=[]
enemybull3=[]
ebullRot =[]
enemyDirection=False 
counter=0
levelcounter=0
ang=90
angle=0
health=100
clear=False 
l1=True 
l2=False
l3=False 
pu=False 
pu2=False 
br=False 
endB=False 
speed=10
s=False 
strengthbool=False 
speedinc=0
strengthinc=0
kPressed=False 
frameb=0
enemybullDirection=False 
orbool=False 
lasbool=False

retry=False 
bombh=False 
#timers for powerups
angleS=0
inc=0
Oinc=0
Sinc=0
STinc=0 
counterr=0

l2c=0 
l3c=0
brc=0 

#bomb stuff
omx=0
omy=0
enemyspeed=5
bombtimer=0 
frameB=0

#map values 
mapx=0
mapy=0

#clearing the levels
clearl2=False 
clearl3=False 
clearbr=False

oppbr=0
oppl3=0

laserSelect=False 
orbselect=False 
speedselect=False 
strengthselect=False 

#coutner put in place to show the key message 
key1counter=0 
key2counter=0 
key3counter=0 
key4counter=0 

#statioanry enemy healths 
stationaryhealth=100
stationaryhealth2=100 
stationaryhealth3=100
stationaryhealth4=100 

stationaryhealth5=100 
stationaryhealth6=100
stationaryhealth7=100 

stenemyRect5=Rect(200,100,50,50) 
stenemyRect6=Rect(700,100,50,50)

stenemyRect7=Rect(500,enemyspeed,50,50)
#miniboss 
bosshp=300
minibossRect=Rect(510,225,75,75)
##### START OF FUNCTIONS #########

### MENU ITEMS ##### 

def introScreen(): #draws the screen
    screen.blit(beginningScreen,(0,0))
def instructions(): 
    #blits instructions 
    screen.blit(ins,(0,0))
    screen.blit(inspic,(200,200))
def mapp():
    #blits the mapp in case its called
    screen.blit(map,(200,200))

###### MOVING THE CHARACTERS AND ENEMIES ############
def moveIsaac():
    #actually moving the character
    global move, frame, ang,speedselect

    x=isaac[0]
    y=isaac[1]
    bullets = []
    b2=[]
    b3=[]
    b4=[]
    myClock = time.Clock()
    mx,my=mouse.get_pos() 
    keys = key.get_pressed()
    newMove = -1
    if keys[K_s]:
        newMove = DOWN
        ang=180 
        if speedselect==True and Sinc<=301:  #if the speed powerup is activated, it moves the player 5 more pixels than normal
            isaac[1] += (speed+5)
        if speedselect==False or Sinc>301: #otherwise, it just moves 5 pixels at a time 
            isaac[1] += speed

        #changes direction of the way isaac is facing based on which arrow key you press (for bullets) 
        #changes angle as well, to be used lateron for the bullets 
        if keys[K_DOWN]:  
            newMove = DOWN
            ang=180
        elif keys[K_UP]:
            newMove = UP
            ang=0
        elif keys[K_RIGHT]:
            newMove = RIGHT
            ang=90
        elif keys[K_LEFT]:
            newMove = LEFT
            ang=270

    elif keys[K_w]:
        newMove = UP
        ang=0
        if speedselect==True and Sinc<=301:
            isaac[1] -= (speed+5)
        if speedselect==False or Sinc>301: 
            isaac[1]-=speed
        if keys[K_DOWN]:
            newMove = DOWN
            ang=180
        elif keys[K_UP]:
            newMove = UP
            ang=0
        elif keys[K_RIGHT]:
            newMove = RIGHT
            ang=90
        elif keys[K_LEFT]:
            newMove = LEFT
            ang=270
    elif keys[K_d]:
        newMove = RIGHT
        ang=90
        if speedselect==True and Sinc<=301: 
            isaac[0] += (speed+5)
        if speedselect==False or Sinc>301: 
            isaac[0] += speed 
        if keys[K_DOWN]:
            newMove = DOWN
            ang=180
        elif keys[K_UP]:
            newMove = UP
            ang=0
        elif keys[K_RIGHT]:
            newMove = RIGHT
            ang=90
        elif keys[K_LEFT]:
            newMove = LEFT
            ang=270
    elif keys[K_a]:
        newMove = LEFT
        ang=270
        if speedselect==True and Sinc<=301: 
            isaac[0] -= (speed+5)
        if speedselect==False or Sinc>301: 
            isaac[0] -= speed
        if keys[K_DOWN]:
            newMove = DOWN
            ang=180
        elif keys[K_UP]:
            newMove = UP
            ang=0
        elif keys[K_RIGHT]:
            newMove = RIGHT
            ang=90
        elif keys[K_LEFT]:
            newMove = LEFT
            ang=270

    #changes direction of isaac based on arrow key, but doesnt move the character (for bullets) 
    elif keys[K_DOWN]:
        newMove = DOWN
        ang=180
    elif keys[K_UP]:
        newMove = UP
        ang=0
    elif keys[K_RIGHT]:
        newMove = RIGHT
        ang=90
    elif keys[K_LEFT]:
        newMove = LEFT
        ang=270
    else:
        frame = 0
    if move == newMove:    
        frame = frame + 0.5
        if frame >= len(pics[move]):
            frame = 1            
    elif newMove != -1:     
        move = newMove      
        frame = 1
    return ang 

def moveBadGuys(x,y):
#moves the bad guys based on where you are 
    global clear,l1,l2,l2c,hits,hitsl2

    #for level 1/2 , checks if the character is a suitable distance away from the enemies, and the enmeies move which ever way you go by 5 pixels each 
    if l1==True: 
        for guy in level1Enemies:
            if hits[(level1Enemies.index(guy))]!='clear': #only moves the character if it's alive 
                if x > guy[0] +5:
                    guy[0]+=5                    
                elif x < guy[0]-5:   
                    guy[0]-=5        
                if y > guy[1] +5:
                    guy[1]+=5
                elif y < guy[1]-5:
                    guy[1]-=5
    if l2==True and l2c>=100: 
        for guy in level2Enemies:
            if hitsl2[(level2Enemies.index(guy))]!='clear':
                if isaac[0] > guy[0] +5:
                    guy[0]+=5                    
                elif isaac[0] < guy[0]-5:   
                    guy[0]-=5        
                if isaac[1] > guy[1] +5:
                    guy[1]+=5
                elif isaac[1] < guy[1]-5:
                    guy[1]-=5


def makeMove(name,start,end):
    #determines which move you made, outputting the according sprite s
    move = []
    for i in range(start,end+1):
        move.append(image.load("%s/%s%03d.png" % (name,name,i)))
    return move


##### COLLISIONS WITH WALLS AND ROCKS####### 

def wallCollision(): #makes sure isaac doesnt go off screen
    global l1,l2,isaac,l3
 #if the characater tries going out side of the screen, it just returns the charater to the opposite side of the map
    if isaac[1] <= 50:             
        isaac=[isaac[0],535]
    if isaac[0] >= 950: 
        isaac=[60,isaac[1]]
    if isaac[0] <= 50:
        isaac=[940,isaac[1]]
    if isaac[1] >= 540:
        isaac=[isaac[0],60]

def rockCollisions():
    #checks to see if you're colliding with any rock 
    global rockr,rockr2,br,l1 
### ROCK COLLISIONS #####
    #instead of using pathfinding which was more difficult for us, we just found the x and y values of each of the corners 
    #founds the ranges for each of the sides after that for each rock, 
    #checked if the player was colliding with that rrange
    #if so, it added or subtracted 10 pixels in the direction he was moving 
    if l1==True: 
        if isaac[0]==rockr[0] and 330>=isaac[1]>=290:
            isaac[0]-=10
        if 650==isaac[0] and 330>=isaac[1]>=290:
            isaac[0]+=10
        if 340==isaac[1] and 650>=isaac[0]>=600:
            isaac[1]+=10
        if 280==isaac[1] and 650>=isaac[0]>=600:
            isaac[1]-=10

        if isaac[0]==rockr2[0] and 330>=isaac[1]>=290:
            isaac[0]-=10
        if 350==isaac[0] and 330>=isaac[1]>=290:
            isaac[0]+=10
        if 340==isaac[1] and 350>=isaac[0]>=300:
            isaac[1]+=10
        if 280==isaac[1] and 350>=isaac[0]>=300:
            isaac[1]-=10
    if br==True: 
        if rockr[0]==isaac[0] and 330>=isaac[1]>=290:
            isaac[0]-=10
        if 650==isaac[0] and 330>=isaac[1]>=290:
            isaac[0]+=10
        if 325==isaac[1] and 650>=isaac[0]>=600:
            isaac[1]+=10
        if 275==isaac[1] and 650>=isaac[0]>=600:
            isaac[1]-=10

        if rockr2[0]==isaac[0] and 330>=isaac[1]>=290:
            isaac[0]-=10
        if 350==isaac[0] and 330>=isaac[1]>=290:
            isaac[0]+=10
        if 325==isaac[1] and 350>=isaac[0]>=300:
            isaac[1]+=10
        if 275==isaac[1] and 350>=isaac[0]>=300:
            isaac[1]-=10

        if rockr[0]==isaac[0] and 430>=isaac[1]>=390:
            isaac[0]-=10
        if 650==isaac[0] and 430>=isaac[1]>=390:
            isaac[0]+=10
        if 425==isaac[1] and 650>=isaac[0]>=600:
            isaac[1]+=10
        if 375==isaac[1] and 650>=isaac[0]>=600:
            isaac[1]-=10

        if rockr2[0]==isaac[0] and 430>=isaac[1]>=390:
            isaac[0]-=10
        if 350==isaac[0] and 430>=isaac[1]>=390:
            isaac[0]+=10
        if 425==isaac[1] and 350>=isaac[0]>=300:
            isaac[1]+=10
        if 375==isaac[1] and 350>=isaac[0]>=300:
            isaac[1]-=10

        if rockr[0]==isaac[0] and 230>=isaac[1]>=190:
            isaac[0]-=10
        if 650==isaac[0] and 230>=isaac[1]>=190:
            isaac[0]+=10
        if 225==isaac[1] and 650>=isaac[0]>=600:
            isaac[1]+=10
        if 175==isaac[1] and 650>=isaac[0]>=600:
            isaac[1]-=10

        if rockr2[0]==isaac[0] and 230>=isaac[1]>=190:
            isaac[0]-=10
        if 350==isaac[0] and 230>=isaac[1]>=190:
            isaac[0]+=10
        if 225==isaac[1] and 350>=isaac[0]>=280:
            isaac[1]+=10
        if 175==isaac[1] and 350>=isaac[0]>=280:
            isaac[1]-=10

            ######### COLLISIONS ############

def checkHits(goodX, goodY):
    #checks if you've been hit yet 
    global health,running,enemybull,enemybull2,pu,l3,br,ebullRot,hitsl2,STinc,strengthselect,strengthbool

    ## LEVEL 1 And 2 COLLISIONS#####
    #goes through every one of the enemies in the enemy list and uses the distance formula to check if the character is touching with one of them
    #if so, it returns it to its designated spot
    #takes away 5 health each time

    if l1==True:
        for i, guy in enumerate(level1Enemies):
            if ((goodX-guy[0])**2 + (goodY-guy[1])**2)**0.5 < 20:
                guy[0], guy[1] = i*500,0
                health-=5

    if l2==True:
        if hitsl2[0]!='clear' or hitsl2[1]!='clear' or hitsl2[2]!='clear' or hitsl2[3]!='clear':
            if ((goodX-level2Enemies[0][0])**2 + (goodY-level2Enemies[0][1])**2)**0.5 < 20:
                level2Enemies[0][0],level2Enemies[0][1]=180,105
                health-=5
            if ((goodX-level2Enemies[1][0])**2 + (goodY-level2Enemies[1][1])**2)**0.5 < 20:
                level2Enemies[1][0],level2Enemies[1][1]=825,105
                health-=5
            if ((goodX-level2Enemies[2][0])**2 + (goodY-level2Enemies[2][1])**2)**0.5 < 20:
                level2Enemies[2][0],level2Enemies[2][1]=180,500
                health-=5
            if ((goodX-level2Enemies[3][0])**2 + (goodY-level2Enemies[3][1])**2)**0.5 < 20:
                level2Enemies[3][0],level2Enemies[3][1]=825,500
                health-=5

    #### powerups/ level3/ boss room
    #goes through each bullet in their designated bullet lists, and uses the distance formula to check if the bullet and the player is touching 
    #if so, takes away 10 health
    if pu==True: 
        for i,bullet in enumerate(enemybull):
            if ((goodX-bullet[0])**2 + (goodY-bullet[1])**2)**0.5 < 20:
                health-=10
                enemybull.remove(bullet)
        for i,bullet in enumerate(enemybull2):
            if ((goodX-bullet[0])**2 + (goodY-bullet[1])**2)**0.5 < 20:
                health-=10
                enemybull2.remove(bullet)
    if pu2==True: 
        for i,bullet in enumerate(enemybull):
            if ((goodX-bullet[0])**2 + (goodY-bullet[1])**2)**0.5 < 20:
                health-=10
                enemybull.remove(bullet)
        for i,bullet in enumerate(enemybull2):
            if ((goodX-bullet[0])**2 + (goodY-bullet[1])**2)**0.5 < 20:
                health-=10
                enemybull2.remove(bullet)

    if l3==True: 
        for i,bullet in enumerate(ebullRot):
            if ((goodX-bullet[0])**2 + (goodY-bullet[1])**2)**0.5 < 20:
                health-=10
                ebullRot.remove(bullet)
    if br==True: 
        for i,bullet in enumerate(enemybull):
            if ((goodX-bullet[0])**2 + (goodY-bullet[1])**2)**0.5 < 20:
                health-=10
                enemybull.remove(bullet)
        for i,bullet in enumerate(enemybull2):
            if ((goodX-bullet[0])**2 + (goodY-bullet[1])**2)**0.5 < 20:
                health-=10
                enemybull2.remove(bullet)
        for i,bullet in enumerate(enemybull3):
            if ((goodX-bullet[0])**2 + (goodY-bullet[1])**2)**0.5 < 20:
                health-=10
                enemybull3.remove(bullet)

def checkbhits(bull,b2,b3,b4):
    #checks if you're bullets have hit an enemy yet 
    global l1,l2,l3,hits,bosshp,hitsl2
    global stationaryhealth,stationaryhealth2,stationaryhealth3,stationaryhealth4,stationaryhealth5,stationaryhealth6,stationaryhealth7

    if l1==True: 
        # there's a list with 3 settings to it, if the value is at true, it shows the fully enemy. 
        #once shot, it changes the value to False, taking it's size down to only its head, 
        #again if it's shot it becomes an eyeball, then finally it is wiped out fully 

        #everytime you shoot the enemy, it returns it to its designated shot 
        #collisions are detected the same way as the checkhits function 

        #checks if each of the bullet lists have made contact with the enemy
        if len(bull)!=0: 
            for b in bull[:]: 
                for i, guy in enumerate(level1Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*500,0
                        if hits[i]=='true':
                            hits[i]='False'
                        elif hits[i]=='False':
                            hits[i]='3'
                        elif hits[i]=='3':
                            hits[i]='clear'
        if len(b2)!=0: 
            for b in b2[:]: 
                for i, guy in enumerate(level1Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*500,0
                        if hits[i]=='true':
                            hits[i]='False'
                        elif hits[i]=='False':
                            hits[i]='3'
                        elif hits[i]=='3':
                            hits[i]='clear'
        if len(b3)!=0: 
            for b in b3[:]: 
                for i, guy in enumerate(level1Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*500,0
                        if hits[i]=='true':
                            hits[i]='False'
                        elif hits[i]=='False':
                            hits[i]='3'
                        elif hits[i]=='3':
                            hits[i]='clear'
        if len(b4)!=0: 
            for b in b4[:]:  
                for i, guy in enumerate(level1Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*500,0
                        if hits[i]=='true':
                            hits[i]='False'
                        elif hits[i]=='False':
                            hits[i]='3'
                        elif hits[i]=='3':
                            hits[i]='clear'
 
    if l2==True: 
        #collisions with enemeies and bullets are the same as level 1, but uses a different list for the hit checkers 
        if len(orbbull)!=0: 
            for b in orbbull[:]: 
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'
        if len(orbBull2)!=0: 
            for b in orbBull2[:]: 
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'
        if len(orbBull3)!=0: 
            for b in orbBull3[:]: 
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'
        if len(orbBull4)!=0: 
            for b in orbBull4[:]:  
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'
        if len(orbBull5)!=0: 
            for b in orbBull5[:]: 
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'
        if len(orbBull6)!=0: 
            for b in orbBull6[:]: 
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'
        if len(orbBull7)!=0: 
            for b in orbBull7[:]: 
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'
        if len(orbBull8)!=0: 
            for b in orbBull8[:]:  
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'

        if len(bull)!=0: 
            for b in bull[:]: 
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'
        if len(b2)!=0: 
            for b in b2[:]: 
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'
        if len(b3)!=0: 
            for b in b3[:]: 
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'
        if len(b4)!=0: 
            for b in b4[:]:  
                for i, guy in enumerate(level2Enemies):
                    if ((b[0]-guy[0])**2 + (b[1]-guy[1])**2)**0.5 < 20:
                        guy[0], guy[1] = i*200,0
                        if hitsl2[i]=='true':
                            hitsl2[i]='False'
                        elif hitsl2[i]=='False':
                            hitsl2[i]='3'
                        elif hitsl2[i]=='3':
                            hitsl2[i]='clear'
    if br==True: 

        ##there is a rect set to each of the enemies in this level 
        #for each of the bullet lists for regular bullets, it iterates through each list 
        #checking if the bullets in each list have made contact with the rect (for each of the rects)
        #if so, it takes off 3 hp from that enemy shot
        #checks if the last item in the orbit bullet list has collided with the enemy, as opposed to going through the whole list
        if len(bull)!=0: 
            for b in bull[:]: 
                if stenemyRect5.collidepoint(b[0],b[1]):
                    stationaryhealth5-=3
        if len(b2)!=0: 
            for b in b2[:]: 
                if stenemyRect5.collidepoint(b[0],b[1]):
                    stationaryhealth5-=3
        if len(b3)!=0: 
            for b in b3[:]: 
                if stenemyRect5.collidepoint(b[0],b[1]):
                    stationaryhealth5-=3
        if len(b4)!=0: 
            for b in b4[:]:  
                if stenemyRect5.collidepoint(b[0],b[1]):
                    stationaryhealth5-=3        
        if len(orbbull)!=0: 
            if stenemyRect5.collidepoint(orbbull[-1][0],orbbull[-1][1]):
                stationaryhealth5-=1
        if len(orbBull2)!=0: 
            if stenemyRect5.collidepoint(orbBull2[-1][0],orbBull2[-1][1]):
                stationaryhealth5-=1
        if len(orbBull3)!=0:  
            if stenemyRect5.collidepoint(orbBull3[-1][0],orbBull3[-1][1]):
                stationaryhealth5-=1
        if len(orbBull4)!=0: 
            if stenemyRect5.collidepoint(orbBull4[-1][0],orbBull4[-1][1]):
                stationaryhealth5-=1
        if len(orbBull5)!=0: 
            if stenemyRect5.collidepoint(orbBull5[-1][0],orbBull5[-1][1]):
                stationaryhealth5-=1
        if len(orbBull6)!=0: 
            if stenemyRect5.collidepoint(orbBull6[-1][0],orbBull6[-1][1]):
                stationaryhealth5-=1
        if len(orbBull7)!=0: 
            if stenemyRect5.collidepoint(orbBull7[-1][0],orbBull7[-1][1]):
                stationaryhealth5-=1
        if len(orbBull8)!=0:  
            if stenemyRect5.collidepoint(orbBull8[-1][0],orbBull8[-1][1]):
                stationaryhealth5-=1
        if len(bull)!=0: 
            for b in bull[:]: 
                if stenemyRect6.collidepoint(b[0],b[1]):
                    stationaryhealth6-=3
        if len(b2)!=0: 
            for b in b2[:]: 
                if stenemyRect6.collidepoint(b[0],b[1]):
                    stationaryhealth6-=3
        if len(b3)!=0: 
            for b in b3[:]: 
                if stenemyRect6.collidepoint(b[0],b[1]):
                    stationaryhealth6-=3
        if len(b4)!=0: 
            for b in b4[:]:  
                if stenemyRect6.collidepoint(b[0],b[1]):
                    stationaryhealth6-=3        
        if len(orbbull)!=0: 
            if stenemyRect6.collidepoint(orbbull[-1][0],orbbull[-1][1]):
                stationaryhealth6-=3
        if len(orbBull2)!=0: 
            if stenemyRect6.collidepoint(orbBull2[-1][0],orbBull2[-1][1]):
                stationaryhealth6-=3
        if len(orbBull3)!=0:  
            if stenemyRect6.collidepoint(orbBull3[-1][0],orbBull3[-1][1]):
                stationaryhealth6-=3
        if len(orbBull4)!=0: 
            if stenemyRect6.collidepoint(orbBull4[-1][0],orbBull4[-1][1]):
                stationaryhealth6-=3
        if len(orbBull5)!=0: 
            if stenemyRect6.collidepoint(orbBull5[-1][0],orbBull5[-1][1]):
                stationaryhealth6-=3
        if len(orbBull6)!=0: 
            if stenemyRect6.collidepoint(orbBull6[-1][0],orbBull6[-1][1]):
                stationaryhealth6-=3
        if len(orbBull7)!=0: 
            if stenemyRect6.collidepoint(orbBull7[-1][0],orbBull7[-1][1]):
                stationaryhealth6-=3
        if len(orbBull8)!=0:  
            if stenemyRect6.collidepoint(orbBull8[-1][0],orbBull8[-1][1]):
                stationaryhealth6-=3
        stenemyRect7=Rect(500,enemyspeed,50,50)#creates new rect for player based on where you are 
        if len(bull)!=0: 
            for b in bull[:]: 
                if stenemyRect7.collidepoint(b[0],b[1]):
                    stationaryhealth7-=3
        if len(b2)!=0: 
            for b in b2[:]: 
                if stenemyRect7.collidepoint(b[0],b[1]):
                    stationaryhealth7-=3
        if len(b3)!=0: 
            for b in b3[:]: 
                if stenemyRect7.collidepoint(b[0],b[1]):
                    stationaryhealth7-=3
        if len(b4)!=0: 
            for b in b4[:]:  
                if stenemyRect7.collidepoint(b[0],b[1]):
                    stationaryhealth7-=3        
        if len(orbbull)!=0: 
            if stenemyRect7.collidepoint(orbbull[-1][0],orbbull[-1][1]):
                stationaryhealth7-=3
        if len(orbBull2)!=0: 
            if stenemyRect7.collidepoint(orbBull2[-1][0],orbBull2[-1][1]):
                stationaryhealth7-=3
        if len(orbBull3)!=0:  
            if stenemyRect7.collidepoint(orbBull3[-1][0],orbBull3[-1][1]):
                stationaryhealth7-=3
        if len(orbBull4)!=0: 
            if stenemyRect7.collidepoint(orbBull4[-1][0],orbBull4[-1][1]):
                stationaryhealth7-=3
        if len(orbBull5)!=0: 
            if stenemyRect7.collidepoint(orbBull5[-1][0],orbBull5[-1][1]):
                stationaryhealth7-=3
        if len(orbBull6)!=0: 
            if stenemyRect7.collidepoint(orbBull6[-1][0],orbBull6[-1][1]):
                stationaryhealth7-=3
        if len(orbBull7)!=0: 
            if stenemyRect7.collidepoint(orbBull7[-1][0],orbBull7[-1][1]):
                stationaryhealth7-=3
        if len(orbBull8)!=0:  
            if stenemyRect7.collidepoint(orbBull8[-1][0],orbBull8[-1][1]):
                stationaryhealth7-=3
  
    if pu==True: 
        #the powerup level collisions work in the same way as the boss room with a rect set to each enemy location
        if len(bull)!=0: 
            for b in bull[:]: 
                if stenemyRect.collidepoint(b[0],b[1]):
                    stationaryhealth-=3
        if len(b2)!=0: 
            for b in b2[:]: 
                if stenemyRect.collidepoint(b[0],b[1]):
                    stationaryhealth-=3
        if len(b3)!=0: 
            for b in b3[:]: 
                if stenemyRect.collidepoint(b[0],b[1]):
                    stationaryhealth-=3
        if len(b4)!=0: 
            for b in b4[:]:  
                if stenemyRect.collidepoint(b[0],b[1]):
                    stationaryhealth-=3      
        #checks if the last item in the orbit bullet list has collided with the enemy, as opposed to going through the whole list  
        if len(orbbull)!=0: 
            if stenemyRect.collidepoint(orbbull[-1][0],orbbull[-1][1]):
                stationaryhealth-=5
        if len(orbBull2)!=0: 
            if stenemyRect.collidepoint(orbBull2[-1][0],orbBull2[-1][1]):
                stationaryhealth-=5
        if len(orbBull3)!=0:  
            if stenemyRect.collidepoint(orbBull3[-1][0],orbBull3[-1][1]):
                stationaryhealth-=5
        if len(orbBull4)!=0: 
            if stenemyRect.collidepoint(orbBull4[-1][0],orbBull4[-1][1]):
                stationaryhealth-=5
        if len(orbBull5)!=0: 
            if stenemyRect.collidepoint(orbBull5[-1][0],orbBull5[-1][1]):
                stationaryhealth-=5
        if len(orbBull6)!=0: 
            if stenemyRect.collidepoint(orbBull6[-1][0],orbBull6[-1][1]):
                stationaryhealth-=5
        if len(orbBull7)!=0: 
            if stenemyRect.collidepoint(orbBull7[-1][0],orbBull7[-1][1]):
                stationaryhealth-=5
        if len(orbBull8)!=0:  
            if stenemyRect.collidepoint(orbBull8[-1][0],orbBull8[-1][1]):
                stationaryhealth-=5
        if len(bull)!=0: 
            for b in bull[:]: 
                if stenemyRect2.collidepoint(b[0],b[1]):
                    stationaryhealth2-=3
        if len(b2)!=0: 
            for b in b2[:]: 
                if stenemyRect2.collidepoint(b[0],b[1]):
                    stationaryhealth2-=3
        if len(b3)!=0: 
            for b in b3[:]: 
                if stenemyRect2.collidepoint(b[0],b[1]):
                    stationaryhealth2-=3
        if len(b4)!=0: 
            for b in b4[:]:  
                if stenemyRect2.collidepoint(b[0],b[1]):
                    stationaryhealth2-=3   
        #checks if the last item in the orbit bullet list has collided with the enemy, as opposed to going through the whole list     
        if len(orbbull)!=0: 
            if stenemyRect2.collidepoint(orbbull[-1][0],orbbull[-1][1]):
                stationaryhealth2-=1
        if len(orbBull2)!=0: 
            if stenemyRect2.collidepoint(orbBull2[-1][0],orbBull2[-1][1]):
                stationaryhealth2-=1
        if len(orbBull3)!=0:  
            if stenemyRect2.collidepoint(orbBull3[-1][0],orbBull3[-1][1]):
                stationaryhealth2-=1
        if len(orbBull4)!=0: 
            if stenemyRect2.collidepoint(orbBull4[-1][0],orbBull4[-1][1]):
                stationaryhealth2-=1
        if len(orbBull5)!=0: 
            if stenemyRect2.collidepoint(orbBull5[-1][0],orbBull5[-1][1]):
                stationaryhealth2-=1
        if len(orbBull6)!=0: 
            if stenemyRect2.collidepoint(orbBull6[-1][0],orbBull6[-1][1]):
                stationaryhealth2-=1
        if len(orbBull7)!=0: 
            if stenemyRect2.collidepoint(orbBull7[-1][0],orbBull7[-1][1]):
                stationaryhealth2-=1
        if len(orbBull8)!=0:  
            if stenemyRect2.collidepoint(orbBull8[-1][0],orbBull8[-1][1]):
                stationaryhealth2-=1

    if pu2==True: 
        if len(bull)!=0: 
            for b in bull[:]: 
                if stenemyRect.collidepoint(b[0],b[1]):
                    stationaryhealth3-=3
        if len(b2)!=0: 
            for b in b2[:]: 
                if stenemyRect.collidepoint(b[0],b[1]):
                    stationaryhealth3-=3
        if len(b3)!=0: 
            for b in b3[:]: 
                if stenemyRect.collidepoint(b[0],b[1]):
                    stationaryhealth3-=3
        if len(b4)!=0: 
            for b in b4[:]:  
                if stenemyRect.collidepoint(b[0],b[1]):
                    stationaryhealth3-=3  

        #checks if the last item in the orbit bullet list has collided with the enemy, as opposed to going through the whole list      
        if len(orbbull)!=0: 
            if stenemyRect.collidepoint(orbbull[-1][0],orbbull[-1][1]):
                stationaryhealth3-=5
        if len(orbBull2)!=0: 
            if stenemyRect.collidepoint(orbBull2[-1][0],orbBull2[-1][1]):
                stationaryhealth3-=5
        if len(orbBull3)!=0:  
            if stenemyRect.collidepoint(orbBull3[-1][0],orbBull3[-1][1]):
                stationaryhealth3-=5
        if len(orbBull4)!=0: 
            if stenemyRect.collidepoint(orbBull4[-1][0],orbBull4[-1][1]):
                stationaryhealth3-=5
        if len(orbBull5)!=0: 
            if stenemyRect.collidepoint(orbBull5[-1][0],orbBull5[-1][1]):
                stationaryhealth3-=5
        if len(orbBull6)!=0: 
            if stenemyRect.collidepoint(orbBull6[-1][0],orbBull6[-1][1]):
                stationaryhealth3-=5
        if len(orbBull7)!=0: 
            if stenemyRect.collidepoint(orbBull7[-1][0],orbBull7[-1][1]):
                stationaryhealth3-=5
        if len(orbBull8)!=0:  
            if stenemyRect.collidepoint(orbBull8[-1][0],orbBull8[-1][1]):
                stationaryhealth3-=5
        if len(bull)!=0: 
            for b in bull[:]: 
                if stenemyRect2.collidepoint(b[0],b[1]):
                    stationaryhealth4-=3
        if len(b2)!=0: 
            for b in b2[:]: 
                if stenemyRect2.collidepoint(b[0],b[1]):
                    stationaryhealth4-=3
        if len(b3)!=0: 
            for b in b3[:]: 
                if stenemyRect2.collidepoint(b[0],b[1]):
                    stationaryhealth4-=3
        if len(b4)!=0: 
            for b in b4[:]:  
                if stenemyRect2.collidepoint(b[0],b[1]):
                    stationaryhealth4-=3     
        #checks if the last item in the orbit bullet list has collided with the enemy, as opposed to going through the whole list   
        if len(orbbull)!=0: 
            if stenemyRect2.collidepoint(orbbull[-1][0],orbbull[-1][1]):
                stationaryhealth4-=5
        if len(orbBull2)!=0: 
            if stenemyRect2.collidepoint(orbBull2[-1][0],orbBull2[-1][1]):
                stationaryhealth4-=5
        if len(orbBull3)!=0:  
            if stenemyRect2.collidepoint(orbBull3[-1][0],orbBull3[-1][1]):
                stationaryhealth4-=5
        if len(orbBull4)!=0: 
            if stenemyRect2.collidepoint(orbBull4[-1][0],orbBull4[-1][1]):
                stationaryhealth4-=5
        if len(orbBull5)!=0: 
            if stenemyRect2.collidepoint(orbBull5[-1][0],orbBull5[-1][1]):
                stationaryhealth4-=5
        if len(orbBull6)!=0: 
            if stenemyRect2.collidepoint(orbBull6[-1][0],orbBull6[-1][1]):
                stationaryhealth4-=5
        if len(orbBull7)!=0: 
            if stenemyRect2.collidepoint(orbBull7[-1][0],orbBull7[-1][1]):
                stationaryhealth4-=5
        if len(orbBull8)!=0:  
            if stenemyRect2.collidepoint(orbBull8[-1][0],orbBull8[-1][1]):
                stationaryhealth4-=5
    if l3==True: 
        #checks if each of the bullet in each of the bullet list are colliding with the minibossRect 
        if len(bull)!=0: 
            for b in bull[:]: 
                if minibossRect.collidepoint(b[0],b[1]):
                    bosshp-=1
        if len(b2)!=0: 
            for b in b2[:]: 
                if minibossRect.collidepoint(b[0],b[1]):
                    bosshp-=1
        if len(b3)!=0: 
            for b in b3[:]: 
                if minibossRect.collidepoint(b[0],b[1]):
                    bosshp-=1
        if len(b4)!=0: 
            for b in b4[:]:  
                if minibossRect.collidepoint(b[0],b[1]):
                    bosshp-=1      

        #checks if the last item in the orbit bullet list has collided with the enemy, as opposed to going through the whole list
        if len(orbbull)!=0: 
            if minibossRect.collidepoint(orbbull[-1][0],orbbull[-1][1]):
                bosshp-=1
        if len(orbBull2)!=0: 
            if minibossRect.collidepoint(orbBull2[-1][0],orbBull2[-1][1]):
                bosshp-=1
        if len(orbBull3)!=0:  
            if minibossRect.collidepoint(orbBull3[-1][0],orbBull3[-1][1]):
                bosshp-=1
        if len(orbBull4)!=0: 
            if minibossRect.collidepoint(orbBull4[-1][0],orbBull4[-1][1]):
                bosshp-=1
        if len(orbBull5)!=0: 
            if minibossRect.collidepoint(orbBull5[-1][0],orbBull5[-1][1]):
                bosshp-=1
        if len(orbBull6)!=0: 
            if minibossRect.collidepoint(orbBull6[-1][0],orbBull6[-1][1]):
                bosshp-=1
        if len(orbBull7)!=0: 
            if minibossRect.collidepoint(orbBull7[-1][0],orbBull7[-1][1]):
                bosshp-=1
        if len(orbBull8)!=0:  
            if minibossRect.collidepoint(orbBull8[-1][0],orbBull8[-1][1]):
                bosshp-=1
  
##### WEAPONARY AND BULLETS AND POWERUPS #########  
def enemybullets(): 
    #moves the bullets for the enemies 
    global counter,enemybull,enemybull2,enemybull3,enemyspeed,enemyDirection,br,l3,ebullRot,ang
    global stationaryhealth5,stationaryhealth6,stationaryhealth7,oppl3 
    if l3==True: 
        distx=isaac[0]-510 #finds distance between the enemy and you for the x and y values 
        disty=isaac[1]-225
        dist=hypot(distx,disty) #uses the two distances and finds the hypot of that triangle 
        ang=atan2(disty,distx)#uses the two distances and finds the angle, using atan2 
        xx=15*cos(ang)#15 would be the speed of the bullet travelling, being multiplied by the sin and cos values, to get the x and y value of the bullet point
        yy=15*sin(ang)
        counter+=1 
        if counter==10: #adds a new bullet every time the counter turns to 10 
            ebullRot.append([510,225,xx,yy])
            counter=0

    if br==True: 
        if oppl3>=100: #oppl3 counter is to wait for the enemies to come after 100 have gone by 
            counter+=1 
            if counter==15: # every time the counter reaches 15, it adds a new bullet 
                if stationaryhealth5>0:
                    enemybull.append([200,100]) # loca tion of first stationary enemy 
                if stationaryhealth6>0:
                    enemybull3.append([700,100]) #location of second stationary enemy
                if enemyDirection==False: # this allows the bullet to go down wards when the enemy is moving down
                    if stationaryhealth7>0: 
                        enemybull2.append([500,enemyspeed]) #location of the moving enemy, enemy speed being thechanging y value 
                if enemyDirection==True:  #when the enemy has reached the bottom of the screen, value is set to true to go back up 
                    if stationaryhealth7>0: 
                        enemybull2.append([500,enemyspeed]) #
                counter=0
            if stationaryhealth7>0: 
                if enemyDirection==False: #if direction is false, the enemy constantly moves down 
                    if enemyspeed<=500: 
                        enemyspeed+=5
                        if enemyspeed==500:
                            enemyDirection=True #once the y value has reached 500, the direction is sset to true
                if enemyDirection==True: # if it is true, then the enemy moves back up the screen 
                    if enemyspeed>=10:
                        enemyspeed-=5 
                        if enemyspeed==10:
                            enemyDirection=False #if it is = to 10, then the enemy goes down, following this loop
def bu(ang):    
    #nmoves your own bullets 
    global bullets,b2,b3,b4,kPressed 
    x=isaac[0]
    y=isaac[1]
    myClock = time.Clock()
    mx,my=mouse.get_pos() 
    keys = key.get_pressed()

    #the ang value changes based on where you're facing, for example up is 0 down is 180 
    #it finds the cos and sin value for that condition, and then adds 4 values to a list (x,y,cosval,sinval)
    #seperate bullet list is made for each of the directions, so they dont intervene with one another 
    if keys[K_UP] and ang==0 and kPressed==True:
        vx = cos(ang) 
        vy = sin(ang)
        bullets.append([x,y,vx,vy]) 
        kPressed=False #kPressed is set to false each time, so you can only shoot once
    if keys[K_DOWN] and ang==180 and kPressed==True: 
        vx = cos(ang)
        vy = sin(ang)
        b2.append([x,y,vx,vy])
        kPressed=False 
    if keys[K_LEFT] and ang==270 and kPressed==True:
        vx = cos(ang)
        vy = sin(ang)
        b3.append([x,y,vx,vy])
        kPressed=False 
    if keys[K_RIGHT] and ang==90 and kPressed==True:
        vx = cos(ang)
        vy = sin(ang)
        b4.append([x,y,vx,vy])
        kPressed=False 
    #goes through each of the bullet lists and adds on the appropriate value to its movement, and removes bullet from list in case it goes offscreen
    for b in bullets[:]:
        b[0]+=0
        b[1]-=10 #subtracts 10 from y value when pressed up
        if b[1] < 50 or min(b) < -100:                                   
            bullets.remove(b)
    for b in b3[:]: 
        b[0]-=10 #subtracts 10 from x value each time when pressed left
        b[1]+=0
        if b[0] < 50 or min(b) < -100:
            b3.remove(b)
    for b in b4[:]:
        b[0]+=10 #adds 10 to x value each time when pressed right
        b[1]+=0
        if b[0] > 950 or min(b) < -100:
            b4.remove(b)
    for b in b2[:]:
        b[0]+=0
        b[1]+=10 #adds 10 to y value each time when pressed down 
        if b[1] > 550 or min(b) < -100:
            b2.remove(b) 
    return bullets,b2,b3,b4    
      

def powerup2():
    #power up for the orbit powerup 
    global angle
    keys=key.get_pressed() 
    x=isaac[0] 
    y=isaac[1]
    radius=100#radius set to 100 
    if keys[K_o]:
        theta = radians(angle) #angle continuously increases as you hold down the O button, allowing the bullets to keep rotating 
        vx = radius*cos(theta) 
        vy = radius*sin(theta)
        ox = radius*sin(theta) #reverses the coordinates around
        oy = radius*cos(theta)

        #adds on 8 bullets, 4 of which have normal (cos,sin) coordinates, while other 4 have (sin,cos) coordinate instead 
        #reversing sin and cos just allowed for the bullets to be placed at a distance between 
        orbbull.append([x,y,vx,vy]) 
        orbBull2.append([x,y,vx,vy])
        orbBull3.append([x,y,ox,oy])
        orbBull4.append([x,y,ox,oy])
        orbBull5.append([x,y,ox,oy])
        orbBull6.append([x,y,ox,oy])
        orbBull7.append([x,y,vx,vy])
        orbBull8.append([x,y,vx,vy])
    if len(orbbull)>=1:
        #adds on the x and y values in a positive direction so the bullet goes clockwise in a 360 degree motion
        orbbull[-1][0]+=orbbull[-1][2]
        orbbull[-1][1]+=orbbull[-1][3]
        screen.blit(bull,(orbbull[-1][0],orbbull[-1][1])) 
        #subtracts y and x values so the bullet can go counter clockwise fully 
        orbBull2[-1][0]-=orbBull2[-1][2]
        orbBull2[-1][1]-=orbBull2[-1][3]
        screen.blit(bull,(orbBull2[-1][0],orbBull2[-1][1])) 
        #adds x but subtracts y, to allow it to move clockwise, but at a distance away from the first orbull list with y value above player 
        orbBull3[-1][0]+=orbBull3[-1][2]
        orbBull3[-1][1]-=orbBull3[-1][3]
        screen.blit(bull,(orbBull3[-1][0],orbBull3[-1][1])) 
        #subtracts x but adds y, to make it go clockwise, but y value is below player
        orbBull4[-1][0]-=orbBull4[-1][2]
        orbBull4[-1][1]+=orbBull4[-1][3]
        screen.blit(bull,(orbBull4[-1][0],orbBull4[-1][1]))
        #subtracts both x and y value to make orbit go counter clockwise, with y value below player
        orbBull5[-1][0]-=orbBull5[-1][2]
        orbBull5[-1][1]-=orbBull5[-1][3]
        screen.blit(bull,(orbBull5[-1][0],orbBull5[-1][1]))
        #adds on x and y positively to make sure the bullets can go clockwise
        orbBull6[-1][0]+=orbBull6[-1][2]
        orbBull6[-1][1]+=orbBull6[-1][3]
        screen.blit(bull,(orbBull6[-1][0],orbBull6[-1][1]))  
        #goes counterclock but y value is added below 
        orbBull7[-1][0]-=orbBull7[-1][2]
        orbBull7[-1][1]+=orbBull7[-1][3]
        screen.blit(bull,(orbBull7[-1][0],orbBull7[-1][1]))
        #goes clockwise, with the y value starting on the top of the player 
        orbBull8[-1][0]+=orbBull8[-1][2]
        orbBull8[-1][1]-=orbBull8[-1][3]
        screen.blit(bull,(orbBull8[-1][0],orbBull8[-1][1]))

        display.flip() 
    angle+=10 #adds angle by 10 each time 
    
def powerup3(x,y): 
    #powerup for the laser 
    global hitsl2,l2,l3,bosshp
    global stationaryhealth,stationaryhealth2,stationaryhealth5,stationaryhealth6,stationaryhealth7
    dx=0
    dy=0 
    mx,my=mouse.get_pos()
    keys=key.get_pressed() 
    if keys[K_RSHIFT]:
    #####Checking collides with the enemies and lowering health

    #LASER MATH STUFF# 
    #finds the distance to the end of the screen 
    #finds hypot of that value, and the x/y value depending on which way you're facing 
    #uses a for loop to go through each pixel, drawing a circle on each of those pixels on the hypot
    #collisions for enemies are same as in the function designated to it 
        if move==UP:
            yy=-isaac[1]+50 #just the distance to the end of the screen, depending on the way you're facing so it doesnt go offs creen 
            dist=hypot(isaac[0],yy)
            for i in range(int(dist)):
                dy=int(isaac[1]+i/dist*yy)  
                draw.circle(screen,red,(isaac[0],dy),5)
                if l2==True:#checks for the collisions using the distance formula
                    for i, guy in enumerate(level2Enemies):
                        if ((isaac[0]-guy[0])**2 + (dy-guy[1])**2)**0.5 < 20:
                            guy[0], guy[1] = i*200,0
                            #moves on to the next type of enemy 
                            if hitsl2[i]=='true':
                                hitsl2[i]='False'
                            elif hitsl2[i]=='False':
                                hitsl2[i]='3'
                            elif hitsl2[i]=='3':
                                hitsl2[i]='clear'
                                
                if l3==True: 
                    if minibossRect.collidepoint(isaac[0],dy):
                        bosshp-=0.5
                if pu==True: 
                    if stenemyRect.collidepoint(isaac[0],dy): 
                        stationaryhealth-=0.1
                    if stenemyRect2.collidepoint(isaac[0],dy): 
                        stationaryhealth2-=0.1
                if br==True: 
                    if stenemyRect5.collidepoint(isaac[0],dy): 
                        stationaryhealth5-=0.1
                    if stenemyRect6.collidepoint(isaac[0],dy): 
                        stationaryhealth6-=0.1
                    if stenemyRect7.collidepoint(isaac[0],dy): 
                        stationaryhealth7-=.1
                        
        if move==DOWN:
            yy=550-isaac[1]
            dist=hypot(isaac[0],yy)
            for i in range(int(dist)):
                dy=int(isaac[1]+i/dist*yy)  
                draw.circle(screen,red,(isaac[0],dy),5)
                if l2==True:
                    for i, guy in enumerate(level2Enemies):
                        if ((isaac[0]-guy[0])**2 + (dy-guy[1])**2)**0.5 < 20:
                            guy[0], guy[1] = i*200,0
                            if hitsl2[i]=='true':
                                hitsl2[i]='False'
                            elif hitsl2[i]=='False':
                                hitsl2[i]='3'
                            elif hitsl2[i]=='3':
                                hitsl2[i]='clear'
                if l3==True: 
                    if minibossRect.collidepoint(isaac[0],dy):
                        bosshp-=0.5
                if pu==True: 
                    if stenemyRect.collidepoint(isaac[0],dy): 
                        stationaryhealth-=0.1
                    if stenemyRect2.collidepoint(isaac[0],dy): 
                        stationaryhealth2-=0.1
                if br==True: 
                    if stenemyRect5.collidepoint(isaac[0],dy): 
                        stationaryhealth5-=0.1
                    if stenemyRect6.collidepoint(isaac[0],dy): 
                        stationaryhealth6-=0.1
                    if stenemyRect7.collidepoint(isaac[0],dy): 
                        stationaryhealth7-=.1
        if move==RIGHT:
            xx=950-isaac[0]
            dist=hypot(xx,isaac[1])
            for i in range(int(dist)):
                dx=int(isaac[0]+i/dist*xx)  
                draw.circle(screen,red,(dx,isaac[1]),5)
                if l2==True:
                    for i, guy in enumerate(level2Enemies):
                        if ((dx-guy[0])**2 + (isaac[1]-guy[1])**2)**0.5 < 20:
                            guy[0], guy[1] = i*200,0
                            if hitsl2[i]=='true':
                                hitsl2[i]='False'
                            elif hitsl2[i]=='False':
                                hitsl2[i]='3'
                            elif hitsl2[i]=='3':
                                hitsl2[i]='clear'
                if l3==True: 
                    if minibossRect.collidepoint(dx,isaac[1]):
                        bosshp-=0.5
                if pu==True: 
                    if stenemyRect.collidepoint(dx,isaac[1]): 
                        stationaryhealth-=0.1
                    if stenemyRect2.collidepoint(dx,isaac[1]): 
                        stationaryhealth2-=0.1
                if br==True: 
                    if stenemyRect5.collidepoint(dx,isaac[1]): 
                        stationaryhealth5-=0.1
                    if stenemyRect6.collidepoint(dx,isaac[1]): 
                        stationaryhealth6-=0.1
                    if stenemyRect7.collidepoint(dx,isaac[1]): 
                        stationaryhealth7-=.1
        if move==LEFT:
            xx=-isaac[0]+50
            dist=hypot(xx,isaac[1])
            for i in range(int(dist)):
                dx=int(isaac[0]+i/dist*xx)  
                draw.circle(screen,red,(dx,isaac[1]),5)
                if l2==True:
                    for i, guy in enumerate(level2Enemies):
                        if ((dx-guy[0])**2 + (isaac[1]-guy[1])**2)**0.5 < 20:
                            guy[0], guy[1] = i*200,0
                            if hitsl2[i]=='true':
                                hitsl2[i]='False'
                            elif hitsl2[i]=='False':
                                hitsl2[i]='3'
                            elif hitsl2[i]=='3':
                                hitsl2[i]='clear'
                if l3==True: 
                    if minibossRect.collidepoint(dx,isaac[1]):
                        bosshp-=0.5
                if pu==True: 
                    if stenemyRect.collidepoint(dx,isaac[1]): 
                        stationaryhealth-=0.1
                    if stenemyRect2.collidepoint(dx,isaac[1]): 
                        stationaryhealth2-=0.1
                if br==True: 
                    if stenemyRect5.collidepoint(dx,isaac[1]): 
                        stationaryhealth5-=0.1
                    if stenemyRect6.collidepoint(dx,isaac[1]): 
                        stationaryhealth6-=0.1
                    if stenemyRect7.collidepoint(dx,isaac[1]): 
                        stationaryhealth7-=.1
    ##########################################################
    return dx,dy
def powerup4(): 
    #shield powerup 
    global isaac,angleS,shield 
    draw.circle(screen,(0,255,0),(isaac[0],isaac[1]),100,1) #draws the actual shield itself 
    for i in range(360):
        theta = radians(i)
        vx = 100*cos(theta) #finds the cos and sin value for each point on this circle
        vy = 100*sin(theta)
        stlist.append((isaac[0]+vx,isaac[1]+vy)) #adds it to a lsit 
        for i, guy in enumerate(ebullRot): # checks if the last item in the last has collided yet, with each bullet
            if ((stlist[-1][0]-guy[0])**2 + (stlist[-1][1]-guy[1])**2)**0.5 < 20:
                ebullRot.remove(guy)
        for i, guy in enumerate(enemybull2):
            if ((stlist[-1][0]-guy[0])**2 + (stlist[-1][1]-guy[1])**2)**0.5 < 20:
                enemybull2.remove(guy)
        for i, guy in enumerate(enemybull):
            if ((stlist[-1][0]-guy[0])**2 + (stlist[-1][1]-guy[1])**2)**0.5 < 20:
                enemybull.remove(guy)
        for i, guy in enumerate(enemybull3):
            if ((stlist[-1][0]-guy[0])**2 + (stlist[-1][1]-guy[1])**2)**0.5 < 20:
                enemybull3.remove(guy)
        for i,guy in enumerate(level2Enemies): 
            if ((stlist[-1][0]-guy[0])**2 + (stlist[-1][1]-guy[1])**2)**0.5 < 20:
                guy[0],guy[1]=i*200,0
    angleS+=1

def bomb():
    #explodingthe bomb and such 
    global bombh,omx,omy,bombtimer,frameB,bombNum
    global bosshp,stationaryhealth,stationaryhealth2,stationaryhealth3,stationaryhealth4,stationaryhealth5,stationaryhealth6,stationaryhealth7,enemyspeed
    mx,my=mouse.get_pos() 
    mb=mouse.get_pressed() 
    keys=key.get_pressed() 
    if keys[K_LSHIFT]:
        #making the circle for the aim on the bomb
        draw.circle(screen,(255,0,0),(mx,my),10,1)
        x=mx-isaac[0]
        y=my-isaac[1]
        dist=hypot(x,y) #finds hypot from where you are to where you're pointing 
        for i in range(int(dist)):
            dx=int(isaac[0]+i/dist*x)
            dy=int(isaac[1]+i/dist*y)  
            draw.circle(screen,(255,0,0),(dx,dy),1) #draws a line to that area point to that location 
        if click: 
            bombtimer=0 #counts up to until it will explode 
            frameB=0
            bombNum-=1
            bombh=True #bombh checks if you've pressed for a bomb 
            omx,omy=mx,my #omx and omy values set to place that bomb in that spot you clicked 
    if bombNum>=0:
        if bombh==True: 
            bombtimer+=1
            newRect=Rect(omx-50,omy-50,300,300) #sets up the radius for the blast 
            if bombtimer>=30: 
                frameB+=1 
                if frameB<=15: 
                    screen.blit(bombs[frameB],(omx-50,omy-50))
                    #just checking for hits on each enemy and
                    #subtracting the damage amount from the health
                    #checks if the enemy is within said radius 
                    for i, guy in enumerate(level1Enemies):
                        if newRect.collidepoint(guy[0],guy[1]): 
                            guy[0], guy[1] = i*500,0
                            if hits[i]=='true':
                                hits[i]='False'
                            elif hits[i]=='False':
                                hits[i]='3'
                            elif hits[i]=='3':
                                hits[i]='clear'
                    for i, guy in enumerate(level2Enemies):
                        if newRect.collidepoint(guy[0],guy[1]): 
                            guy[0], guy[1] = i*200,0
                            if hitsl2[i]=='true':
                                hitsl2[i]='False'
                            elif hitsl2[i]=='False':
                                hitsl2[i]='3'
                            elif hitsl2[i]=='3':
                                hitsl2[i]='clear'
                    if minibossRect.colliderect(newRect):
                        bosshp-=3
                    if pu==True: 
                        if stenemyRect.colliderect(newRect):
                            stationaryhealth-=3
                        if stenemyRect2.colliderect(newRect):
                            stationaryhealth2-=3
                    if pu2==True:
                        if stenemyRect.colliderect(newRect):
                            stationaryhealth3-=3
                        if stenemyRect2.colliderect(newRect):
                            stationaryhealth4-=3
                    if br==True: 
                        if stenemyRect.colliderect(newRect):
                            stationaryhealth5-=3
                        if stenemyRect2.colliderect(newRect):
                            stationaryhealth6-=3
                        stenemyRect7=Rect(500,enemyspeed,50,50)
                        if stenemyRect7.colliderect(newRect):
                            stationaryhealth7-=3
                    ###########################
#drawing the actual enemyDirection 
def drawS(bullets,b2,b3,b4): #drawing everything on to the screen basically 
    #we're sorry for all the globals 
    global laserSelect,orbselect,speedselect,strengthselect,key1counter,key2counter,key3counter,key4counter,key5counter
    global strengthbool,s,orbool,lasbool,speedinc,Oinc,inc,Sinc,STinc,strengthinc
    global running,l1,l2,l3,clear,br,pu,pu2,isaac,framee
    global l3c,brc,clearl3,clearbr,oppl3,oppbr  
    global level1Enemies,level2Enemies,enemybull2,enemybull,enemybull3,enemyDirection,enemybullDirection,hits,enemyspeed
    global frameb,ebullRot,counter,levelcounter
    global counterr,retry,bombNum,mapx,mapy,l2c,hitsl2,clearl2,framel2,health,bosshp,map
    global stationaryhealth,stationaryhealth2,stationaryhealth3,stationaryhealth4,stationaryhealth5,stationaryhealth6,stationaryhealth7
    global bombtimer,omx,omy,endB
    keys=key.get_pressed()
    mx,my=mouse.get_pos() 
    screen.blit(hrect,(0,600))    
    for i in range(4): 
        draw.rect(screen,(255,0,0),(100+i*100,650,75,75),5)
    screen.blit(powerups,(200,600))
    if l1==True: 
        screen.blit(bgScreen,(0,0))
        screen.blit(rock,(rockr))
        screen.blit(rock,(rockr2))
        framee+=1 
        if framee==3:
            framee=0 
        if counterr>=100 and health>0:
            for i in range(len(hits)):
                #changing the enemy based on the number of times
                #it has been hit (full enemy, head and the eye) and emptying the list
                #once the enemies are dead
                if hits[i]=='true':
                    screen.blit(epics[framee],level1Enemies[i])
                elif hits[i]=='False':
                    screen.blit(epics2[framee],level1Enemies[i])
                elif hits[i]=='3':
                    screen.blit(eye,level1Enemies[i])
                if hits[0]=='clear' and hits[1]=='clear'and  hits[2]=='clear' :
                    level1Enemies=[]
                    clear=True 
        if clear ==True: 
            screen.blit(arrow1,(450,100))
            screen.blit(arrow2,(750,250))
        
        if isaac[0]>=950 and 345>=isaac[1]>=255 and clear==True: #changing the screen once Isaac exits the doors
            l1=False
            l2=True 
        if isaac[1]<=50  and 450<=isaac[0]<=545 and clear==True: 
            pu=True 
            l1=False 
    if l2==True:  
        screen.blit(map2,(0,0))
        framel2+=1
        if framel2==5:
            framel2=0
        if l2c>=100 and health>0: 
            for i in range(len(hitsl2)):
                #changing the enemy based on the number of times
                #it has been hit (full enemy, head and the eye) and emptying the list
                #once the enemies are dead
                if hitsl2[i]=='true':
                    screen.blit(enempics[framel2],level2Enemies[i])
                elif hitsl2[i]=='False':
                    screen.blit(enempicsHead[framel2],level2Enemies[i])
                elif hitsl2[i]=='3':
                    screen.blit(eye,level2Enemies[i])
                if hitsl2[0]=='clear' and hitsl2[1]=='clear'and  hitsl2[2]=='clear' and hitsl2[3]=='clear':
                    level2Enemies=[]
                    clearl2=True 
        if clearl2==True: 
            screen.blit(arrow1,(450,100))
            screen.blit(arrow3,(450,400))
        if isaac[1]>=540 and 450<=isaac[0]<=545 and clearl2==True: #changing the screen once Isaac exits the doors, and levels have been cleared
            l2=False 
            pu2=True 
        if isaac[1]<=50 and 450<=isaac[0]<=545 and clearl2==True : 
            br=True
            l2=False
        if isaac[0]<=50 and 345>=isaac[1]>=255:
            l2=False
            l1=True  
    if pu2==True: 
        screen.blit(pup,(0,0))
        if health>0: 
            if stationaryhealth3>0:
                #changing the colour of the powerup rect once all
                #the enemies are killed in that certain room
                draw.rect(screen,(255,0,0),(powerupRect[0]-50,75,stationaryhealth3,10)) 
                draw.rect(screen,(0,0,0),(powerupRect[0]-50,75,stationaryhealth3,10),5)
            if stationaryhealth4>0:
                draw.rect(screen,(255,0,0),(powerup2Rect[0]-50,175,stationaryhealth4,10))
                draw.rect(screen,(0,0,0),(powerup2Rect[0]-50,175,stationaryhealth4,10),5)
            frameb+=1
            if frameb==3:
                frameb=0
                if len(enemybull)<=5: 
                    if stationaryhealth3>0: #only adds bullets and blits the enemies and bullets if the health is over 0 
                        enemybull.append([powerupRect[0],100])
                if len(enemybull2)<=5: 
                    if stationaryhealth4>0: 
                        enemybull2.append([powerup2Rect[0],100])
            if stationaryhealth3>0: 
                screen.blit(stenemy[frameb],(powerupRect[0],100))
            if stationaryhealth4>0:
                screen.blit(stenemy[frameb],(powerup2Rect[0],100))
            if stationaryhealth3>0:
                for i in range(len(enemybull)):
                    enemybull[i][0]+=0
                    enemybull[i][1]+=6 #moves the bullet downwards 
                    screen.blit(eBull,(enemybull[i][0],enemybull[i][1]))
                for i in enemybull[:]: 
                    if i[1]>=500: #if it goes below the screen, it's removed 
                        enemybull.remove(i)
            if stationaryhealth4: 
                for i in range(len(enemybull2)):
                    enemybull2[i][0]+=0
                    enemybull2[i][1]+=6
                    screen.blit(eBull,(enemybull2[i][0],enemybull2[i][1]))
                for i in enemybull2[:]: 
                    if i[1]>=500: 
                        enemybull2.remove(i)
            if lasbool==False: 
                if stationaryhealth3>0: 
                    draw.rect(screen,(255,0,0),powerupRect,0)
                if stationaryhealth3<=0: 
                    draw.rect(screen,(0,255,0),powerupRect,0)
                draw.rect(screen,(255,255,255),powerupRect,5)
                if powerupRect.collidepoint(isaac[0],isaac[1]): 
                    draw.rect(screen,(255,0,255),powerupRect,5) 
                screen.blit(laser,powerupRect)
            if orbool==False: 
                if stationaryhealth4>0: 
                    draw.rect(screen,(255,0,0),powerup2Rect,0)
                if stationaryhealth4<=0: 
                    draw.rect(screen,(0,255,0),powerup2Rect,0)
                draw.rect(screen,(255,255,255),powerup2Rect,5)
                if powerup2Rect.collidepoint(isaac[0],isaac[1]): 
                    draw.rect(screen,(255,0,255),powerup2Rect,5)
                screen.blit(orbit,powerup2Rect)
            if powerupRect.collidepoint(isaac[0],isaac[1]): 
                if stationaryhealth3<=0: 
                    enemybull=[]
                    if keys[32]: #if you press on the laser powerup, it adds it to the powerup toolbar 
                        screen.blit(lasery,(300,100))
                        lasbool=True  
            if powerup2Rect.collidepoint(isaac[0],isaac[1]): 
                if stationaryhealth4<=0:
                    enemybull2=[]
                    if keys[32]: 
                        screen.blit(orbity,(300,100))
                        orbool=True 
        if isaac[1]<=50:
            l2=True
            pu2=False
    if pu==True: 
        screen.blit(pup,(0,0))
        if health>0: 
            if stationaryhealth>0: 
                draw.rect(screen,(255,0,0),(powerupRect[0]-50,75,stationaryhealth,10))
                draw.rect(screen,(0,0,0),(powerupRect[0]-50,75,stationaryhealth,10),5)
            if stationaryhealth2>0:
                draw.rect(screen,(255,0,0),(powerup2Rect[0]-50,175,stationaryhealth2,10))
                draw.rect(screen,(0,0,0),(powerup2Rect[0]-50,175,stationaryhealth2,10),5)
            frameb+=1
            if frameb==3:
                frameb=0
            #blits and appends bullets if the enemy has not been killed yet 
                if len(enemybull)<=5: 
                    if stationaryhealth>0: 
                        enemybull.append([powerupRect[0],100])
                if len(enemybull2)<=5:
                    if stationaryhealth2>0:
                        enemybull2.append([powerup2Rect[0],100])
            if stationaryhealth>0: 
                screen.blit(stenemy[frameb],(powerupRect[0],100))
            if stationaryhealth2>0: 
                screen.blit(stenemy[frameb],(powerup2Rect[0],100))
            if stationaryhealth>0:
                for i in range(len(enemybull)):
                    enemybull[i][0]+=0
                    enemybull[i][1]+=6 #moves their bullets down wards 
                    screen.blit(eBull,(enemybull[i][0],enemybull[i][1]))
                for i in enemybull[:]:  
                    if i[1]>=500: 
                        enemybull.remove(i)
            if stationaryhealth2>0: 
                for i in range(len(enemybull2)):
                    enemybull2[i][0]+=0
                    enemybull2[i][1]+=6
                    screen.blit(eBull,(enemybull2[i][0],enemybull2[i][1]))
                for i in enemybull2[:]: 
                    if i[1]>=500: 
                        enemybull2.remove(i)
            if s==False: 
                if stationaryhealth>0:
                    draw.rect(screen,(255,0,0),powerupRect,0)
                if stationaryhealth<=0: 
                    draw.rect(screen,(0,255,0),powerupRect,0)
                draw.rect(screen,(255,255,255),powerupRect,5)
                if powerupRect.collidepoint(isaac[0],isaac[1]): 
                    draw.rect(screen,(255,0,255),powerupRect,5)
                screen.blit(pspeed,powerupRect)
            if strengthbool==False: 
                if stationaryhealth2>0: 
                    draw.rect(screen,(255,0,0),powerup2Rect,0)
                if stationaryhealth2<=0: 
                    draw.rect(screen,(0,255,0),powerup2Rect,0)
                draw.rect(screen,(255,255,255),powerup2Rect,5)
                if powerup2Rect.collidepoint(isaac[0],isaac[1]): 
                    draw.rect(screen,(255,0,255),powerup2Rect,5)
                screen.blit(strength,powerup2Rect)
            if powerupRect.collidepoint(isaac[0],isaac[1]) and stationaryhealth<=0: 
                enemybull=[]
                if keys[32]: 
                    screen.blit(speedy,(300,100))
                    draw.rect(screen,(255,0,0),(375,370,200,10))
                    s=True 
                    if speedinc<=60: #animation for the green bar which shows you the increase in speed you just got 
                        speedinc+=5
                        draw.rect(screen,(0,255,0),(575,370,speedinc,10))
                    else: 
                        draw.rect(screen,(0,255,0),(575,370,speedinc,10))            
            if powerup2Rect.collidepoint(isaac[0],isaac[1]) and stationaryhealth2<=0: 
                enemybull2=[]
                if keys[32]: 
                    screen.blit(strengthy,(300,100))
                    draw.rect(screen,(255,0,0),(375,370,200,10))
                    strengthbool=True 
                    if strengthinc<=60:
                        strengthinc+=5 #shows you the increase in strength you got from the animation given 
                        draw.rect(screen,(0,255,0),(575,370,strengthinc,10))
                    else: 
                        draw.rect(screen,(0,255,0),(575,370,strengthinc,10))  
        if isaac[1]>=540:
            pu=False
            l1=True 
        if isaac[0]>=950 and clearl2==True: 
            pu=False 
            br=True 
    if l3==True: 
        myClock=time.Clock() 
        screen.blit(level3,(0,0))
        if health>0: 
            #draws different colored rects for the bosses health, based on how much it has left 
            if 200<=bosshp<=300: 
                draw.rect(screen,(0,255,0),(400,100,bosshp,10))
            if 100<=bosshp<=200:
                draw.rect(screen,(255,255,0),(400,100,bosshp,10))
            if 30<=bosshp<=100: 
                draw.rect(screen,(255,111,0),(400,100,bosshp,10))
            if 0<=bosshp<=30: 
                draw.rect(screen,red,(400,100,bosshp,10))
            if bosshp>0 and oppbr>=100: 
                draw.rect(screen,(0),(400,100,300,10),4)
                framee+=1
                if framee==6:
                    framee=0
                    myClock.tick(25)
                screen.blit(enempics[framee],(510,225))
                for i in ebullRot[:]: 
                    i[0]+=i[2]#adds vx value 
                    i[1]+=i[3]#adds vy value 
                    screen.blit(eBull,(int(i[0]),int(i[1])))
                    if i[1]>=540 or i[1]<=50 or i[0]>=950 or i[0]<=50: 
                        ebullRot.remove(i)#removed from screen if it goes out 
            if bosshp<=0: 
                clearl3=True #level is cleared when health is below 0 
                ebullRot=[] #list of bullets is emptied 
            if clearl3==True: 
                screen.blit(arrow2,(750,250))
        if isaac[0]<=50 and 265<=isaac[1]<=350:
            br=True 
            l3=False 
        if isaac[0]>=950 and 265<=isaac[1]<=350 and clearl3==True:
            endB=True 
            l3=False 
    if br==True: 
        #blits the rocks and map 
        screen.blit(bossmap,(0,0))
        screen.blit(rock,rockr)
        screen.blit(rock,(rockr[0],rockr[1]-100))
        screen.blit(rock,(rockr[0],rockr[1]+100))
        screen.blit(rock,rockr2)
        screen.blit(rock,(rockr2[0],rockr2[1]-100))
        screen.blit(rock,(rockr2[0],rockr2[1]+100))
        if health>0: 
            if stationaryhealth5>0: 
                draw.rect(screen,(255,0,0),(175,100,stationaryhealth5,10))
                draw.rect(screen,(0,0,0),(175,100,stationaryhealth5,10),5)
            if stationaryhealth6>0: 
                draw.rect(screen,(255,0,0),(675,150,stationaryhealth6,10))
                draw.rect(screen,(0,0,0),(675,150,stationaryhealth6,10),5)
            if oppl3>=100: 
                frameb+=1 
                if frameb==3: 
                    frameb=0
                if stationaryhealth5>0: 
                    for i in range(len(enemybull)):
                        enemybull[i][0]+=0
                        enemybull[i][1]+=8#bullet goes down 8 pixels each time for the statioanry enemies 
                        screen.blit(eBull,(enemybull[i][0],enemybull[i][1]))
                    for i in enemybull[:]: 
                        if i[1]>=500: 
                            enemybull.remove(i)#removed when goes off sfcreen
                if stationaryhealth6>0: 
                    for i in range(len(enemybull3)):
                        enemybull3[i][0]+=0
                        enemybull3[i][1]+=8
                        screen.blit(eBull,(enemybull3[i][0],enemybull3[i][1]))
                    for i in enemybull3[:]: 
                        if i[1]>=500: 
                            enemybull3.remove(i)
                if stationaryhealth5>0: 
                    screen.blit(stenemy[frameb],(200,100))
                if stationaryhealth6>0: 
                    screen.blit(stenemy[frameb],(700,100))

                if stationaryhealth7>0: 
                    stenemyRect7=Rect(500,enemyspeed,50,50) #draws a new rectangle based on enemy position 
                    draw.rect(screen,(255,0,0),(stenemyRect7[0],enemyspeed,stationaryhealth7,10))
                    draw.rect(screen,(0,0,0),(stenemyRect7[0],enemyspeed,stationaryhealth7,10),5)
                    for i in range(len(enemybull2)):
                        if enemyDirection==False: #checks which direction the bullet is going if enemy is going down 
                            if enemybullDirection==False: #if its false, the bullet goes left in a zigzag way 
                                enemybull2[i][0]-=10
                                enemybull2[i][1]+=10
                                if enemybull2[i][0]==300:
                                    enemybullDirection=True#if its true, it goes right and continues to pattern 
                            if enemybullDirection==True : 
                                    enemybull2[i][0]+=10
                                    enemybull2[i][1]+=10
                                    if enemybull2[i][0]==600: 
                                        enemybullDirection=False 
                        if enemyDirection==True: #checks which direction the bullet is going if the nemy is going up
                            if enemybullDirection==False: 
                                enemybull2[i][0]-=10
                                enemybull2[i][1]-=10
                                if enemybull2[i][0]<=300:
                                    enemybullDirection=True
                            if enemybullDirection==True : 
                                    enemybull2[i][0]+=10
                                    enemybull2[i][1]-=10
                                    if enemybull2[i][0]==600: 
                                        enemybullDirection=False
                        screen.blit(eBull,(enemybull2[i][0],enemybull2[i][1]))
                    for i in enemybull2[:]: 
                        if i[1]>=500: 
                            enemybull2.remove(i)#removes when it goes off screen 
                    screen.blit(stenemy[frameb],(500,enemyspeed))
                if stationaryhealth6<=0 and stationaryhealth7<=0 and stationaryhealth5<=0: #empties list when they die 
                    enemybull=[]
                    enemybull2=[]
                    enemybull3=[]
                    clearbr=True 
        if clearbr==True: 
            screen.blit(arrow2,(750,250))
        if isaac[1]>=540 and 455<=isaac[0]<=550:
            l2=True
            br=False
        if isaac[0]<=50 and 265<=isaac[1]<=350:
            pu=True 
            br=False 
        if isaac[0]>=950 and 265<=isaac[1]<=350 and clearbr==True:
            l3=True 
            br=False 
    if health>0:
        #if you're alive, it blits the bullets and lets you move 
        for b in bullets:
            screen.blit(bull,(int(b[0]),int(b[1])))
        for b in b2:
            screen.blit(bull,(int(b[0]),int(b[1])))
        for b in b3:
            screen.blit(bull,(int(b[0]),int(b[1])))
        for b in b4:
            screen.blit(bull,(int(b[0]),int(b[1])))
        pic = pics[move][int(frame)]
        screen.blit(pic,(isaac[0]-pic.get_width()//2,isaac[1]-pic.get_height()//2))

    #counters are used to show the picture of who you're facing at the start of each level 
    counterr+=1
    if l1==True and counterr<=30:
        screen.blit(room1opp,(350,100))

    if l2==True:
        l2c+=1
        if l2c<=30:
            screen.blit(room2opp,(350,100))
    if l3==True: 
        oppbr+=1
        if oppbr<=50: 
            screen.blit(br1opp,(350,100))
    if br==True: 
        oppl3+=1 
        if oppl3<=50: 
            screen.blit(room3opp,(350,100))
    #dying stuff
    if health<=0: 
        screen.blit(death,(300,100))
        if l1==True: 
            screen.blit(dead1,(520,245)) #blits the enemy which killed you each time 
        if l2==True or l3==True: 
            screen.blit(dead2,(520,245))
        if pu==True or pu2==True or br==True : 
            screen.blit(dead3,(520,245))
        screen.blit(restartbutton,(800,400))
        screen.blit(exitbutton,(50,400))
        if exitRect.collidepoint(mx,my) and mb[0]==1: 
            running=False#exits the game 
        if retryRect.collidepoint(mx,my) and mb[0]==1: 
            retry=True #calls the retry button which resets the whole game 
        if retry==True:

        #resets all the variables back to its original state  
            hits=['true','true','true']
            hitsl2=['true','true','true','true']

            bullets=[]
            orbbull=[]
            orbBull2=[]
            orbBull3=[]
            orbBull4=[]
            orbBull5=[]
            orbBull6=[]
            orbBull7=[]
            orbBull8=[]
            b2=[]
            b3=[]
            b4=[]

            stlist=[]
            bombNum=4

            enemybull=[] 
            enemybull2=[]
            enemybull3=[]
            ebullRot =[]
            enemyDirection=False 
            counter=0
            levelcounter=0
            ang=90
            angle=0
            health=100
            clear=False 
            l1=True 
            l2=False
            l3=False 
            pu=False 
            pu2=False 
            br=False 
            speed=10
            s=False 
            strengthbool=False 
            speedinc=0
            strengthinc=0
            kPressed=False 
            frameb=0
            enemybullDirection=False 
            orbool=False 
            lasbool=False

            retry=False 
            bombh=False 
            #timers for powerups
            angleS=0
            inc=0
            Oinc=0
            Sinc=0
            STinc=0 
            counterr=0

            l2c=0 
            l3c=0
            brc=0 

            #bomb stuff
            omx=0
            omy=0
            enemyspeed=5
            bombtimer=0 
            frameB=0

            mapx=0
            mapy=0

            clearl2=False 
            clearl3=False 
            clearbr=False

            oppbr=0
            oppl3=0

            laserSelect=False 
            orbselect=False 
            speedselect=False 
            strengthselect=False 

            key1counter=0 
            key2counter=0 
            key3counter=0 
            key4counter=0 
            key5counter=0 

            stationaryhealth=100
            stationaryhealth2=100 
            stationaryhealth3=100
            stationaryhealth4=100 

            stationaryhealth5=100 
            stationaryhealth6=100
            stationaryhealth7=100 

            #miniboss 
            bosshp=300
            bosshp=300
            framee=0
            framel2=0     

            isaac = [500,300]
            level1Enemies = [[0,0], [500,0], [1000,0]]    # 6 x,y pairs 
            level2Enemies = [[180,105], [825,105], [180,500],[825,500]]    # 6 x,y pairs 
        return running
#TOOL BAR STUFFFFFFFFFFFFFFF
    #shows how many bombs you have left 
    for i in range(bombNum): 
        screen.blit(bombpic,(600+i*100,650)) 
    if bombNum<=0: 
        for i in range(4): 
            screen.blit(none,(600+i*100,650)) 

    #health works the same way for each if statement, decreasing the hearts by your health level 
    if health>=80:
        screen.blit(heart,(50,25)) #blits the whole hearts you have remaining 
        screen.blit(heart,(75,25))
        screen.blit(heart,(100,25))
        screen.blit(heart,(125,25))
        if health>95:
            screen.blit(heart,(150,25)) #blits the full heart if you have over a certain amount
        if 90<health<=95: 
            screen.blit(half,(150,25)) #blits half of the heart
        if 85<health<=90: 
            screen.blit(quart,(150,25)) #blits quarter
        if 80<health<=85: 
            screen.blit(empty,(150,25))#blits empty heart when that health range is done 
    if health>=60:
        screen.blit(heart,(50,25))
        screen.blit(heart,(75,25))
        screen.blit(heart,(100,25))
        screen.blit(empty,(150,25))
        if health>75:
            screen.blit(heart,(125,25))
        if 70<health<=75: 
            screen.blit(half,(125,25))
        if 65<health<=70: 
            screen.blit(quart,(125,25))
        if 60<health<=65: 
            screen.blit(empty,(125,25))
    if health>=40:
        screen.blit(heart,(50,25))
        screen.blit(heart,(75,25))
        screen.blit(empty,(125,25))
        screen.blit(empty,(150,25))
        if health>55:
            screen.blit(heart,(100,25))
        if 50<health<=55: 
            screen.blit(half,(100,25))
        if 45<health<=50: 
            screen.blit(quart,(100,25))
        if 40<health<=45: 
            screen.blit(empty,(100,25))
    if health>=20:
        screen.blit(heart,(50,25))
        screen.blit(empty,(100,25))
        screen.blit(empty,(125,25))
        screen.blit(empty,(150,25))
        if health>35:
            screen.blit(heart,(75,25))
        if 30<health<=35: 
            screen.blit(half,(75,25))
        if 25<health<=30: 
            screen.blit(quart,(75,25))
        if 20<health<=25: 
            screen.blit(empty,(75,25))
    if health>=0:
        screen.blit(empty,(75,25))
        screen.blit(empty,(100,25))
        screen.blit(empty,(125,25))
        screen.blit(empty,(150,25))
        if health>15:
            screen.blit(heart,(50,25))
        if 10<health<=15: 
            screen.blit(threeq,(50,25))
        if 5<health<=10: 
            screen.blit(half,(50,25))
        if 0<health<=5: 
            screen.blit(quart,(50,25))
    if health==0: 
        screen.blit(empty,(50,25))
        screen.blit(empty,(75,25))
        screen.blit(empty,(100,25))
        screen.blit(empty,(125,25))
        screen.blit(empty,(150,25))

    ##################DETERMING IF AND WHEN THE POWERUP IS ACCESSED############
            ##### CODE IS SAME FOR ALL POWERUPS ####
    if lasbool==True:
        draw.rect(screen,(255,255,255),(100,650,75,75))
        screen.blit(laser,(100,650))#blits the powerup popupmessage
        key1counter+=1 
        if key1counter<=60: 
            screen.blit(key1,(125,250))#blits the powerup pop for 60 seconds, telling which key to press to activate
        if keys[K_1]: #if the according key is pressed, value is set to true 
            laserSelect=True 
        if laserSelect==True:
            inc+=.5#inc variable determines how fast the powerup will go by 
            #draws a triangle for each part of the rectangle for the powerup 
            #inc is subtracted by 38 or 113 or 188 or 263 each time to get the inc as a number from 1-75 (width and height)

            if inc<=38: #38 since half of the width is 38, and this deals with the top right quadrant triangle
                draw.polygon(screen,(255,0,0),[(138,688),(138,650),(138+inc,650)]) #starts from the middle, goes to the top of the rectangle, last point is to the top right part of the rectangle, inc is added on to the x value each time
            if 113>=inc>=38: #next triang
                draw.polygon(screen,(255,0,0),[(138,688),(138,650),(175,650)])#blits the triangle just drawn once again 
                #starts at the middle and the top right corner, and changes the y value gradually so it reaches the bottom right corner 
                draw.polygon(screen,(255,0,0),[(138,688),(175,650),(175,650+(inc-38))])
            if 188>=inc>=113:
                #blits triangles already drawn
                draw.polygon(screen,(255,0,0),[(138,688),(138,650),(175,650)])
                draw.polygon(screen,(255,0,0),[(138,688),(175,650),(175,725)])
                #starts at the middle and bottom right corner, going all the way to the bottom left corner, subtracting inc by 113 to get it as a number from 1-75
                draw.polygon(screen,(255,0,0),[(138,688),(175,725),(175-(inc-113),725)])
            if 263>=inc>=188:
                #blits triangles already drawn 
                draw.polygon(screen,(255,0,0),[(138,688),(138,650),(175,650)])
                draw.polygon(screen,(255,0,0),[(138,688),(175,650),(175,725)])
                draw.polygon(screen,(255,0,0),[(138,688),(175,725),(100,725)])
                #starts at the middle,and bottom left, going up to the top left 
                draw.polygon(screen,(255,0,0),[(138,688),(100,725),(100,725-(inc-188))])
            if 301>=inc>=263:
                #blits triangles already drawn 
                draw.polygon(screen,(255,0,0),[(138,688),(138,650),(175,650)])
                draw.polygon(screen,(255,0,0),[(138,688),(175,650),(175,725)])
                draw.polygon(screen,(255,0,0),[(138,688),(175,725),(100,725)])
                draw.polygon(screen,(255,0,0),[(138,688),(100,725),(100,650)])
                #goes from middle to top left, subtracting inc by 263 to get the number as 1-38 (half of a triangle), until it reaches the full middle
                draw.polygon(screen,(255,0,0),[(138,688),(100,650),(100+(inc-263),650)])
            if inc>=301: #when it completes, it draws a red rect 
                draw.rect(screen,(255,0,0),(100,650,75,75))

                        ############POLYGON SYSTEM WORKS THE SAME WAY FOR ALL POWERUP RECTANGLES, X VALUE IS CHANGED ACCORDING TO LOCATION OF THE RECTANGLE ONLY ############
    if orbool==True:
        draw.rect(screen,(255,255,255),(200,650,75,75))
        screen.blit(orbit,(200,650))
        key2counter+=1
        if key2counter<=60: 
            screen.blit(key2,(125,250))
        if keys[K_2]: 
            orbselect=True 
        if orbselect==True: 
            Oinc+=1
            if Oinc<=38: 
                draw.polygon(screen,(255,0,0),[(238,688),(238,650),(238+Oinc,650)])
            if 113>=Oinc>=38: 
                draw.polygon(screen,(255,0,0),[(238,688),(238,650),(275,650)])
                draw.polygon(screen,(255,0,0),[(238,688),(275,650),(275,650+(Oinc-38))])
            if 188>=Oinc>=113:
                draw.polygon(screen,(255,0,0),[(238,688),(238,650),(275,650)])
                draw.polygon(screen,(255,0,0),[(238,688),(275,650),(275,725)])
                draw.polygon(screen,(255,0,0),[(238,688),(275,725),(275-(Oinc-113),725)])
            if 263>=Oinc>=188:
                draw.polygon(screen,(255,0,0),[(238,688),(238,650),(275,650)])
                draw.polygon(screen,(255,0,0),[(238,688),(275,650),(275,725)])
                draw.polygon(screen,(255,0,0),[(238,688),(275,725),(200,725)])
                draw.polygon(screen,(255,0,0),[(238,688),(200,725),(200,725-(Oinc-188))])
            if 301>=Oinc>=263:
                draw.polygon(screen,(255,0,0),[(238,688),(238,650),(275,650)])
                draw.polygon(screen,(255,0,0),[(238,688),(275,650),(275,725)])
                draw.polygon(screen,(255,0,0),[(238,688),(275,725),(200,725)])
                draw.polygon(screen,(255,0,0),[(238,688),(200,725),(200,650)])
                draw.polygon(screen,(255,0,0),[(238,688),(200,650),(200+(Oinc-263),650)])
            if Oinc>=301: 
                draw.rect(screen,(255,0,0),(200,650,75,75))
    if s==True:
        draw.rect(screen,(255,255,255),(300,650,75,75))
        screen.blit(pspeed,(300,650))
        key3counter+=1
        if key3counter<=60: 
            screen.blit(key3,(125,250))
        if keys[K_3]: 
            speedselect=True 
        if speedselect==True: 
            Sinc+=.5
            if Sinc<=38: 
                draw.polygon(screen,(255,0,0),[(338,688),(338,650),(338+Sinc,650)])
            if 113>=Sinc>=38: 
                draw.polygon(screen,(255,0,0),[(338,688),(338,650),(375,650)])
                draw.polygon(screen,(255,0,0),[(338,688),(375,650),(375,650+(Sinc-38))])
            if 188>=Sinc>=113:
                draw.polygon(screen,(255,0,0),[(338,688),(338,650),(375,650)])
                draw.polygon(screen,(255,0,0),[(338,688),(375,650),(375,725)])
                draw.polygon(screen,(255,0,0),[(338,688),(375,725),(375-(Sinc-113),725)])
            if 263>=Sinc>=188:
                draw.polygon(screen,(255,0,0),[(338,688),(338,650),(375,650)])
                draw.polygon(screen,(255,0,0),[(338,688),(375,650),(375,725)])
                draw.polygon(screen,(255,0,0),[(338,688),(375,725),(300,725)])
                draw.polygon(screen,(255,0,0),[(338,688),(300,725),(300,725-(Sinc-188))])
            if 301>=Sinc>=263:
                draw.polygon(screen,(255,0,0),[(338,688),(338,650),(375,650)])
                draw.polygon(screen,(255,0,0),[(338,688),(375,650),(375,725)])
                draw.polygon(screen,(255,0,0),[(338,688),(375,725),(300,725)])
                draw.polygon(screen,(255,0,0),[(338,688),(300,725),(300,650)])
                draw.polygon(screen,(255,0,0),[(338,688),(300,650),(300+(Sinc-263),650)])
            if Sinc>=301: 
                draw.rect(screen,(255,0,0),(300,650,75,75))
    if strengthbool==True:
        draw.rect(screen,(255,255,255),(400,650,75,75))
        screen.blit(strength,(400,650))
        key4counter+=1
        if key4counter<=60: 
            screen.blit(key4,(125,250))
        if keys[K_4]: 
            strengthselect=True 
        if strengthselect==True: 
            STinc+=1
            if STinc<=38: 
                draw.polygon(screen,(255,0,0),[(438,688),(438,650),(438+STinc,650)])
            if 113>=STinc>=38: 
                draw.polygon(screen,(255,0,0),[(438,688),(438,650),(475,650)])
                draw.polygon(screen,(255,0,0),[(438,688),(475,650),(475,650+(STinc-38))])
            if 188>=STinc>=113:
                draw.polygon(screen,(255,0,0),[(438,688),(438,650),(475,650)])
                draw.polygon(screen,(255,0,0),[(438,688),(475,650),(475,725)])
                draw.polygon(screen,(255,0,0),[(438,688),(475,725),(475-(STinc-113),725)])
            if 263>=STinc>=188:
                draw.polygon(screen,(255,0,0),[(438,688),(438,650),(475,650)])
                draw.polygon(screen,(255,0,0),[(438,688),(475,650),(475,725)])
                draw.polygon(screen,(255,0,0),[(438,688),(475,725),(400,725)])
                draw.polygon(screen,(255,0,0),[(438,688),(400,725),(400,725-(STinc-188))])
            if 301>=STinc>=263:
                draw.polygon(screen,(255,0,0),[(438,688),(438,650),(475,650)])
                draw.polygon(screen,(255,0,0),[(438,688),(475,650),(475,725)])
                draw.polygon(screen,(255,0,0),[(438,688),(475,725),(400,725)])
                draw.polygon(screen,(255,0,0),[(438,688),(400,725),(400,650)])
                draw.polygon(screen,(255,0,0),[(438,688),(400,650),(400+(STinc-263),650)])
            if STinc>=301: 
                draw.rect(screen,(255,0,0),(400,650,75,75))

    ####### DEALING WITH THE MAP RATIOS #############
    map=transform.scale(map,(250,75)) #draws map in the upper hand corner 
    screen.blit(map,(700,50)) #blits it 
    if l1==True: 
        ratio=20 #sets the ratio for 20 for the y value
        #ratio was found by dividing the  height of the room/height of each individual square on the minimap 

        #divides the x and y value of you're character by the ratio, to scale it down to the size of the square
        #the +700 and +75 etc values at the end, are just put the circle on to the area of the actual map in accorrdance to the level 
        mapx=int((isaac[0]/15)+700)#different for x 
        mapy=int((isaac[1]/ratio)+75)
        draw.circle(screen,(0,255,0),(mapx,mapy),5) #draws it on the according box 
    if l2==True: 
        ratio=20
        mapx=int((isaac[0]/15)+760)
        mapy=int((isaac[1]/ratio)+75)
        draw.circle(screen,(0,255,0),(mapx,mapy),5)
    if br==True: 
        ratio=20
        mapx=int((isaac[0]/15)+760)
        mapy=int((isaac[1]/ratio)+50)
        draw.circle(screen,(0,255,0),(mapx,mapy),5)
    if pu2==True: 
        ratio=20
        mapx=int((isaac[0]/15)+760)
        mapy=int((isaac[1]/ratio)+100)
        draw.circle(screen,(0,255,0),(mapx,mapy),5)
    if pu==True: 
        ratio=20
        mapx=int((isaac[0]/15)+700)
        mapy=int((isaac[1]/ratio)+50)
        draw.circle(screen,(0,255,0),(mapx,mapy),5)
    if l3==True: 
        ratio=20
        mapx=int((isaac[0]/15)+825)
        mapy=int((isaac[1]/ratio)+50)
        draw.circle(screen,(0,255,0),(mapx,mapy),5)
#############################################################

    ##### LEVEL CLEAR STUFF ############ 
    if clear==True and l1==True : 
        levelcounter+=1
        if levelcounter<=50: # when you clear the room, it blits the level complete scene for 50 increments each time (for each level down below as well)
            screen.blit(lc,(0,0))
    if l2==True and clearl2==False: 
        levelcounter=0 
    if clearl2==True: 
        levelcounter+=1
        if levelcounter<=50:
            screen.blit(lc,(0,0))
    if l3==True and clearl3==True: 
        l3c+=1 
        if l3c<=50: 
            screen.blit(lc,(0,0))
    if br==True and clearbr==True: 
        brc+=1 
        if brc<=50:
            screen.blit(lc,(0,0))

    if bombtimer<=30 and bombNum>=0:#when you intitally release the bomb, it keeps it at the bomb pic until it explodes for a set while 
        screen.blit(bombpic,(omx-50,omy-50))
    if endB==True: 
        screen.blit(end,(0,0)) #when you reach the end of the game, blits the game over screen 
    return running 
    display.flip() 


###### END OF FUNCTIONZZZZZZZZZZ#####
RIGHT = 0 
DOWN = 1  
UP = 2
LEFT = 3

pics = [] 
pics.append(makeMove("Isaac",7,9))     
pics.append(makeMove("Isaac",1,3))     
pics.append(makeMove("Isaac",10,12))  
pics.append(makeMove("Isaac",4,6))    

#adding all the sprites to their according list for their levels
epics=[]
for i in range(3):
    epics.append(image.load("en//enemy" + str(i) + ".png"))

epics2=[]
for i in range(3):
    epics2.append(image.load("en//en"+str(i)+".png"))

enempics=[]
for i in range(6): 
    enempics.append(image.load("en2//enem"+str(i)+".png"))

enempicsHead=[] 
for i in range(6): 
    enempicsHead.append(image.load("en2//head"+str(i)+".png"))

stenemy=[]
for i in range(3): 
    stenemy.append(image.load("enStationary//en"+str(i)+".png"))

bombs=[] 
for i in range(16): 
    bombs.append(image.load("bombs//bombs"+str(i)+".png"))


frame = 0
framee=0
framel2=0 
move = 0      

isaac = [500,300]
level1Enemies = [[0,0], [500,0], [1000,0]]    # 6 x,y pairs 
level2Enemies = [[180,105], [825,105], [180,500],[825,500]]    # 6 x,y pairs 
red = 255, 0, 0
game = False
instr=False
mappic=False
running = True
start=True 

exitRect1=Rect(730,270,165,80)
myClock = time.Clock()

while running:
    click=False 
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type==KEYDOWN: 
            kPressed=True #only if the key is pressed down, value is set to true 
        if evnt.type==MOUSEBUTTONDOWN:
            click=True #only if the mouse is held down, value is set to true 
    mb=mouse.get_pressed() 
    mx,my=mouse.get_pos()
    keys=key.get_pressed() 
    if start==True: 
        introScreen()
        if exitRect1.collidepoint(mx,my): 
            if evnt.type==MOUSEBUTTONDOWN: 
                running=False
        if startRect.collidepoint(mx,my): 
            if evnt.type==MOUSEBUTTONDOWN:
                game=True#starts the game 
                start=False 
    if insRect.collidepoint(mx,my) and mb[0]==1:
        instr=True
    if instr==True:
        instructions() 
        if keys[K_LEFT]:
            introScreen()
            instr=False 
    if mapRect.collidepoint(mx,my) and mb[0]==1:
        mappic=True
    if mappic==True:
        mapp() 
        if keys[K_LEFT]:
            introScreen()
            mappic=False 
    if game==True:
#calling all the functions
        ang=moveIsaac()
        b,b2,b3,b4=bu(ang)         
        if counterr>=100 and health>0:
            moveBadGuys(isaac[0], isaac[1])
        enemybullets() 
        drawS(b,b2,b3,b4)
        checkHits(isaac[0], isaac[1])
        if lasbool==True and inc<=301 and laserSelect==True: 
            powerup3(isaac[0],isaac[1])
        checkbhits(b,b2,b3,b4) 
        wallCollision()
        if orbool==True and Oinc<=301 and orbselect==True: 
            powerup2() 
        if STinc<=301 and strengthselect==True and strengthbool==True: 
            powerup4() 
        bomb() 
        rockCollisions()
        myClock.tick(50)


    display.flip()
quit()
#end 
