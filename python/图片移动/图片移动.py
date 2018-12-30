import pygame
import sys

pygame.init()

size=width,heigth=600,400
speed=[-2,1]
bg=(0,0,0)

screen=pygame.display.set_mode(size)
pygame.display.set_caption("初次见面")

sysu=pygame.image.load("sysu.jpg")
position=sysu.get_rect()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    position=position.move(speed)

    if position.left<0 or position.right>width:
        sysu=pygame.transform.flip(sysu,True,False)

        speed[0]=-speed[0]

    if position.top<0 or position.bottom>heigth:
        speed[1]=-speed[1]

    screen.fill(bg)
    screen.blit(sysu,position)
    pygame.display.flip()
    pygame.time.delay(10)

