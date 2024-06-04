import pygame
import sys
import math
from strela import Strela
from pomocne_funkce import *
rychlost=2
toceni = 0.04
charge_time = 1.5
charge_frames = charge_time*FPS
chargebar_max = 60
charge_increment = chargebar_max/charge_frames

tank = pygame.image.load("leopard2a9.png").convert()
tank.set_colorkey((255, 128, 255))


class Tank:
    def __init__(self, pozice, smer, ):
        self.pozice = pozice
        self.smer = smer
        self.charged = 20
    def nakresli(self, screen):
        blitRotate(screen, tank, (self.pozice[0],self.pozice[1] ), (25, 25), - self.smer / math.pi * 180)
        pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(self.pozice[0]-9,self.pozice[1]-23,chargebar_max+6,11))
        if self.charged < chargebar_max:
            self.charged += charge_increment
        chargebar = pygame.Rect(self.pozice[0]-6,self.pozice[1]-20,self.charged,5)
        if self.charged >= chargebar_max:
            pygame.draw.rect(screen,DARK_RED,chargebar)
        else:
            pygame.draw.rect(screen,YELLOW,chargebar)






    def posun(self):
        # kod kterej zmeni pozici o smer kazdy frame
        self.pozice[0] += rychlost * math.cos(self.smer)
        self.pozice[1] += rychlost * math.sin(self.smer)
    def vystrel(self):
            s_pozice = [self.pozice[0] , self.pozice[1] ]
            nova_strela = Strela( s_pozice, self.smer,1)
            self.charged = 0
            return nova_strela
