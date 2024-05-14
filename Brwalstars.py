import pygame
import sys
import math

## ahoj, tohle ti sem napsal tata

# Inicializace pygame
pygame.init()

# Velikost okna
WIDTH, HEIGHT = 1500,800
WINDOW_SIZE = (WIDTH, HEIGHT)

# Barvy
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
WHITE = (255, 255, 255)
DARK_WHITE = (128, 128, 128)


# Tmavé odstíny
DARK_BLUE = (0, 0, 128)
DARK_GREEN = (0, 128, 0)
DARK_YELLOW = (128, 128, 0)
DARK_RED = (128, 0, 0)
DARK_BLACK = (0, 0, 0)
DARK_WHITE = (128, 128, 128)
DARK_PURPLE = (128, 0, 128)
DARK_PINK = (255, 20, 147)
DARK_BROWN = (139, 69, 19)

# Základní odstíny
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)

# Světlé odstíny
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
LIGHT_YELLOW = (255, 255, 224)
LIGHT_RED = (255, 192, 203)
LIGHT_BLACK = (128, 128, 128)
LIGHT_WHITE = (255, 255, 255)
LIGHT_PURPLE = (221, 160, 221)
LIGHT_PINK = (255, 182, 193)
LIGHT_BROWN = (210, 105, 30)


def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

    # draw rectangle around the image

    # pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()), 2)


strela = pygame.image.load("z0pq38qb.png")
strela = pygame.transform.scale(strela, (36,9))


def vystreli(screen, s):
    # Načtení obrázku tanku

    screen.blit(strela, s)
def kulka(screen,k):
    pygame.draw.rect(screen,GRAY,pygame.Rect(k[0],k[1],10,5))

vysrelene_srely = []
vystrelene_kulky = []

def palma(screen):
    # Načtení obrázku tanku
    palma = pygame.image.load("python-palma.png")
    screen.blit(palma, (300, 200))






def nakresli_tank(screen, kamtocivim ):
    # Načtení obrázku tanku

    blitRotate(screen,tank,(x,y),(25,25),- kamtocivim / math.pi * 180)











clock = pygame.time.Clock()
fps = 60
fps_was = 0
# Vytvoření okna
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("hra")


tank = pygame.image.load("leopard2a9.png").convert()
tank.set_colorkey((255, 128, 255))

dopredu = pygame.K_w
dozadu = pygame.K_s

doprava = pygame.K_d
doleva = pygame.K_a

vystrel = pygame.K_SPACE
kulomet = pygame.K_LSHIFT
kulomet_str = False

y = 100
x = 100


rychlost = 0


s_rychlost = [20,0]
k_rychlost = [20,0]

kamtocumim = 0


toceni = [0,0]



charged = 0
charge_time = 1.5
charge_frames = charge_time*fps
chargebar_max = 60
charge_increment = chargebar_max/charge_frames


# Hlavní smyčka
running = True
while running:
    fps_was += 1

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


            if event.key == vystrel and charged >= chargebar_max:
                s_pozice = [x + 40, y + 18]
                vysrelene_srely.append(s_pozice)
                charged = 0



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

    kamtocumim += toceni[1] - toceni[0]
    x += rychlost*math.cos(kamtocumim)
    y += rychlost * math.sin(kamtocumim)
    for s in  vysrelene_srely:
        s[0] += s_rychlost[0]
        vystreli(screen, s)
        if s[0] > 3000:
            vysrelene_srely.remove(s)
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > WIDTH - 60:
        x = WIDTH - 60
    if y > HEIGHT - 30:
        y = HEIGHT - 30


    if kulomet_str:
        if charged >= chargebar_max/60:

            charged -= chargebar_max/60

            if fps_was%3 == 0:
                  k_pozice = [x + 30, y + 15]
                  vystrelene_kulky.append(k_pozice)
        else:
            charged = 0
    for k in  vystrelene_kulky:
        k[0] += k_rychlost[0]
        kulka(screen,k)
        if k[0] > 3000:
            vystrelene_kulky.remove(k)






    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(x-9,y-23,chargebar_max+6,11))
    if charged < chargebar_max:
        charged += charge_increment
    chargebar = pygame.Rect(x-6,y-20,charged,5)
    if charged >= chargebar_max:
        pygame.draw.rect(screen,DARK_RED,chargebar)
    else:
        pygame.draw.rect(screen,YELLOW,chargebar)


    # Vykreslení kámenem inspirovaného obrazce
    nakresli_tank(screen, kamtocivim=kamtocumim)
    print(kamtocumim)


    palma(screen)









    # Aktualizace obrazovky
    pygame.display.flip()

    clock.tick(fps)

# Ukončení pygame
pygame.quit()
sys.exit()
