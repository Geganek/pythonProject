import pygame

# Inicializace pygame
pygame.init()

WIDTH, HEIGHT = 1500,800
WINDOW_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)


import sys
import math
from strela import Strela
from pomocne_funkce import *
from tank import *










def palma(screen):
    # Načtení obrázku tanku
    palma = pygame.image.load("python-palma.png")
    screen.blit(palma, (300, 200))

vysrelene_srely = []



clock = pygame.time.Clock()
fps = FPS
fps_was = 0
# Vytvoření okna
pygame.display.set_caption("hra")

dopredu = pygame.K_w
dozadu = pygame.K_s

doprava = pygame.K_d
doleva = pygame.K_a

vystrel = pygame.K_SPACE

hrac1 = Tank([100,100], 0)



rychlost = 0






kulomet = pygame.K_LSHIFT
kulomet_str = False

k_rychlost = [20,0]



toceni = [0,0]







# Hlavní smyčka
running = True
while running:

    screen.fill(DARK_BROWN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.KEYDOWN:
            if event.key == dopredu:
                rychlost = 2
            if event.key == dozadu:
                rychlost = -2
            if event.key == doleva:
                toceni[0] = 0.04
            if event.key == doprava:
                toceni[1] = 0.04
            if event.key == kulomet:
                kulomet_str = True



            if event.key == vystrel and hrac1.charged >= chargebar_max:
                vysrelene_srely.append(hrac1.vystrel())


        if event.type == pygame.KEYUP:
            if event.key == dozadu:
                rychlost = 0
            if event.key == dopredu:
                rychlost = 0
            if event.key == doleva:
                toceni[0] = 0
            if event.key == doprava:
                toceni[1] = 0
            if event.key == kulomet:
                kulomet_str = False



    # Vykreslení modrého pozadí

    hrac1.pozice[0] += rychlost*math.cos(hrac1.smer)
    hrac1.smer += toceni[1] - toceni[0]
    hrac1.pozice[1] += rychlost * math.sin(hrac1.smer)
    for s in  vysrelene_srely:
        s.posun()
        s.nakresli(screen)
        if s.pozice[0] > 3000:
            vysrelene_srely.remove(s)
    if hrac1.pozice[0] < 0:
        hrac1.pozice[0] = 0
    if hrac1.pozice[1] < 0:
        hrac1.pozice[1] = 0
    if hrac1.pozice[0] > WIDTH - 60:
        hrac1.pozice[0] = WIDTH - 60
    if hrac1.pozice[1] > HEIGHT - 30:
        hrac1.pozice[1] = HEIGHT - 30

    if kulomet_str:
        if hrac1.charged >= chargebar_max/60:

            hrac1.charged -= chargebar_max/60

            if fps_was%3 == 0:
                  k_pozice = [hrac1.pozice[0] + 30, hrac1.pozice[1] + 15]
                  nova_strela = Strela(k_pozice, hrac1.smer,0)
                  vysrelene_srely.append(nova_strela)
        else:
            hrac1.charged = 0





    # pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(hrac1.pozice[0]-9,hrac1.pozice[1]-23,chargebar_max+6,11))
    # if charged < chargebar_max:
    #     charged += charge_increment
    # chargebar = pygame.Rect(hrac1.pozice[0]-6,hrac1.pozice[1]-20,charged,5)
    # if charged >= chargebar_max:
    #     pygame.draw.rect(screen,DARK_RED,chargebar)
    # else:
    #     pygame.draw.rect(screen,YELLOW,chargebar)


    # Vykreslení kámenem inspirovaného obrazce
    hrac1.nakresli(screen)



    palma(screen)









    # Aktualizace obrazovky
    pygame.display.flip()

    clock.tick(fps)

# Ukončení pygame
pygame.quit()
sys.exit()
