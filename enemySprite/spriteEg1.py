# spriteEg1.py
# A sprite just refers is a 2D object in a game, usually a character
# A spritesheet is a sheet of all of the frames of animation that a character
# uses in a game to walk or perform actions.
#
# To achieve simple animation in python we simply
# display the frames of the picture in order.

from pygame import *

init()
size = width, height = 800, 600
screen = display.set_mode(size)
running = True
myClock = time.Clock()

frame = 0
pics = []
for i in range(9):
    pics.append(image.load("ryu\\ryu" + str(i) + ".png"))
    

while running:
    for evnt in event.get(): 
        if evnt.type == QUIT:
            running = False

    screen.fill((150,220,150))
    screen.blit(pics[frame],(100,100))
    frame += 1
    if frame == 9: frame = 0
    display.flip()
    myClock.tick(10)
    
quit()
