import barvy
import sys
import pygame
pygame.init()

sirka_obrazu = 800
viska_obrazu = 600
viska = 30
sirka = 60

screen = pygame.display.set_mode((sirka_obrazu,viska_obrazu))

up = pygame.K_w
down = pygame.K_s
left = pygame.K_a
right = pygame.K_d

gravitace = 2

pozice = [50,50]
rychlost = [0,0,0,0]

clock = pygame.time.Clock()
fps = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == up:
                rychlost[0] = 5
            if event.key == down:
                rychlost[1] = 5
            if event.key == left:
                rychlost[2] = 5
            if event.key == right:
                rychlost[3] = 5


        if event.type == pygame.KEYUP:
            if event.key == up:
                rychlost[0] = 0
            if event.key == down:
                rychlost[1] = 0
            if event.key == left:
                rychlost[2] = 0
            if event.key == right:
                rychlost[3] = 0




    screen.fill(barvy.WHITE)
    pozice[0] += rychlost[3]-rychlost[2]
    pozice[1] += (rychlost[1]+gravitace)-(rychlost[0]-gravitace)
    if pozice[0] < 0:
        pozice[0] =0
    if pozice[1] < 0:
        pozice[1] = 0
    if pozice[0] > sirka_obrazu-sirka:
        pozice[0] = sirka_obrazu - sirka
    if pozice[1] > viska_obrazu - viska:
        pozice[1] = viska_obrazu - viska
    pygame.draw.rect(screen,barvy.BLACK,(pozice[0],pozice[1],60,30))







    pygame.display.update()
    clock.tick(fps)














