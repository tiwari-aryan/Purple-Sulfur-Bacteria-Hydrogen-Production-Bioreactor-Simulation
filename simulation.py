# import the pygame module
import pygame
import time
from random import randint
from button import Button
from hover import Hover
from main import mass_predict
from atoms import *

pygame.init()

# Colours
BLACK = (0, 0, 0)
PURPLE = (79, 64, 131)
WHITE = (255, 255, 255)

# Define the background colour
# using RGB color coding.

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((1400, 800))

# Set the caption of the screen
pygame.display.set_caption("Bioreactor Simluation")

# Fill the background colour to the screen
screen.fill(BLACK)

# imp = pygame.image.load("BioReactor.png").convert()
imp = pygame.image.load("BioReactor.png").convert()
# Using blit to copy content from one surface to other
screen.blit(imp, (100, 10))

center_x = 146
center_y = 510
center_x1 = 475
center_y1 = 710
center_x2 = 572
center_y2 = 247
center_x3 = 807
center_y3 = 503

H2S = Hover(
    149, 500, 5, (200, 100, 100), "Hydrogen Sulfide that can be collected from sewage"
)
CO2 = Hover(475, 710, 5, (200, 100, 100), "Carbon Dioxide that acts as a carbon sink")
H2 = Hover(
    550,
    247,
    5,
    (200, 100, 100),
    "Hydrogen is produced and can be used for industrial purposes",
)
CH2 = Hover(
    776,
    218,
    5,
    (200, 100, 100),
    "Methaline is produced which is refined and used as a base for fuel",
)
BAC = Hover(
    440,
    480,
    5,
    (200, 100, 100),
    "Pfennig's Medium: Purple Sulfur Bacteria Performing Photosynthesis",
)
H2O = Hover(807, 493, 5, (200, 100, 100), "Water is produced and can be used")
CHARGE = Hover(
    446, 429, 5, (200, 100, 100), "Elecrtic Charges to help with bacterial metabolism"
)
S = Hover(
    840,
    649,
    5,
    (200, 100, 100),
    "Industrial Sulfur can be used for phosphate fertilizers",
)
REFINE = Hover(
    793, 345, 5, (200, 100, 100), "Methaline is refined with the help of chlorine"
)
FUEL = Hover(939, 328, 5, (200, 100, 100), "Dichloromethane for A1 Fuel")

H2S_mass = 2
CO2_mass = 1
lst = mass_predict(H2S_mass, CO2_mass)
button = Button(1170, 120, 30, 30, PURPLE, WHITE, H2S_mass)
# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True
population = 1
time_counter = 0
hour_counter = 1250
day = 0
vel = 0.3

# game loop

while running:
    screen.fill(BLACK)
    screen.blit(imp, (100, 10))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    bacteria_x = 418
    bacteria_y = 474
    for i in range(0, int(population // 2**15) + 1):
        pygame.draw.circle(screen, PURPLE, (bacteria_x, bacteria_y), 5)
        if bacteria_y <= 550:
            bacteria_x += 20
        if bacteria_x >= 735 and bacteria_y <= 534:
            bacteria_x = 474
            bacteria_y += 30

    # Hydrogen
    for i in range(5):
        if center_x + i * 46 <= 375:
            pygame.draw.circle(screen, WHITE, (center_x + i * 46, center_y), 10)
        else:
            pygame.draw.circle(screen, WHITE, (center_x + i * 46 - 229, center_y), 10)
        center_x += vel
        if center_x >= 375:
            center_x = 146

    # Carbon Dioxide
    for i in range(3):
        if center_y1 - i * 39 >= 593:
            pygame.draw.circle(screen, WHITE, (center_x1, center_y1 - i * 39), 10)
        else:
            pygame.draw.circle(screen, WHITE, (center_x1, center_y1 - i * 39 + 117), 10)
        center_y1 -= vel
        if center_y1 <= 593:
            center_y1 = 710

    # hydrogen out
    for i in range(3):
        if center_y2 - i * 33 >= 147:
            pygame.draw.circle(screen, WHITE, (center_x2, center_y2 - i * 33), 10)
        else:
            pygame.draw.circle(screen, WHITE, (center_x2, center_y2 - i * 33 + 100), 10)
        center_y2 -= vel
        if center_y2 <= 147:
            center_y2 = 247

    # Water out
    for i in range(5):
        if center_x3 + i * 33 <= 907:
            pygame.draw.circle(screen, WHITE, (center_x3 + i * 33, center_y3), 10)
        else:
            pygame.draw.circle(screen, WHITE, (center_x3 + i * 33 - 100, center_y3), 10)
        center_x3 += vel
        if center_x3 >= 907:
            center_x3 = 807

    H2S.draw(screen, mouse_x, mouse_y)
    CO2.draw(screen, mouse_x, mouse_y)
    H2.draw(screen, mouse_x, mouse_y)
    CH2.draw(screen, mouse_x, mouse_y)
    BAC.draw(screen, mouse_x, mouse_y)
    H2O.draw(screen, mouse_x, mouse_y)
    CHARGE.draw(screen, mouse_x, mouse_y)
    S.draw(screen, mouse_x, mouse_y)
    REFINE.draw(screen, mouse_x, mouse_y)
    FUEL.draw(screen, mouse_x, mouse_y)

    if time_counter >= hour_counter:
        population *= 2
        hour_counter += 1250

    if time_counter >= 10000:
        time_counter = 0
        hour_counter = 1250
        day += 0.5
        population -= population // 2**7

    time_counter += int(1 + vel * 10)
    print(population)

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.check() == True:
                if event.button == 1:  # Left button.
                    H2S_mass += 2
                    CO2_mass = int(H2S_mass / 2)
                    vel += 0.2
                    lst = mass_predict(H2S_mass, CO2_mass)
                elif event.button == 3:  # Right button.
                    H2S_mass -= 2
                    CO2_mass = int(H2S_mass / 2)
                    vel -= 0.2
                    lst = mass_predict(H2S_mass, CO2_mass)
    button.draw(screen)
    font = pygame.font.SysFont(None, 24)
    txt = font.render(str(H2S_mass), True, PURPLE)
    screen.blit(txt, (1250, 180))
    txt = font.render("Hydrogen Sulfide: ", True, PURPLE)
    screen.blit(txt, (1100, 180))
    txt = font.render("Carbon Dioxide: ", True, PURPLE)
    screen.blit(txt, (1100, 210))
    txt = font.render(str(CO2_mass), True, PURPLE)
    screen.blit(txt, (1250, 210))

    ## TABLE ##
    pygame.draw.rect(screen, WHITE, pygame.Rect(1100, 300, 90, 40))  # CH2
    txt = font.render("Methylene", True, PURPLE)
    screen.blit(txt, (1105, 315))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1200, 300, 90, 40))  # CH2
    txt = font.render(str(round(lst[3], 3)) + "g", True, PURPLE)
    screen.blit(txt, (1205, 315))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1100, 350, 90, 40))  # H2
    txt = font.render("Hyrdogen", True, PURPLE)
    screen.blit(txt, (1105, 365))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1200, 350, 90, 40))  # H2
    txt = font.render(str(round(lst[4], 3)) + "g", True, PURPLE)
    screen.blit(txt, (1205, 365))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1100, 400, 90, 40))  # S
    txt = font.render("Sulfur", True, PURPLE)
    screen.blit(txt, (1105, 405))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1200, 400, 90, 40))  # S
    txt = font.render(str(round(lst[5], 3)) + "g", True, PURPLE)
    screen.blit(txt, (1205, 405))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1100, 450, 90, 40))  # H2O
    txt = font.render("Water", True, PURPLE)
    screen.blit(txt, (1105, 455))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1200, 450, 90, 40))  # H2O
    txt = font.render(str(round(lst[6], 3)) + "g", True, PURPLE)
    screen.blit(txt, (1205, 455))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1100, 500, 90, 40))  # long name
    txt = font.render("NADP", True, PURPLE)
    screen.blit(txt, (1105, 505))
    pygame.draw.rect(screen, WHITE, pygame.Rect(1200, 500, 90, 40))  # long name
    txt = font.render(str(round(lst[7], 3)) + "g", True, PURPLE)
    screen.blit(txt, (1205, 505))

    # Title
    font = pygame.font.SysFont(None, 50)
    txt = font.render("Bioreactor Simulator", True, PURPLE)
    screen.blit(txt, (520, 40))
    txt = font.render("Day " + str(day), True, PURPLE)
    screen.blit(txt, (100, 40))
    pygame.display.flip()
