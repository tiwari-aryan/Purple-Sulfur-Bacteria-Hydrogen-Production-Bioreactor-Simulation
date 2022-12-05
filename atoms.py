import pygame
     
def CO_atoms(screen, WHITE, center_x, center_y, vel):
    for i in range(5):
        if center_x + i * 7 <= 375:
            pygame.draw.circle(screen, WHITE, (center_x + i * 7, center_y), 10)
        else:
            pygame.draw.circle(screen, WHITE, (center_x + i * 7 - 36, center_y), 10)
    if center_x >= 375:
        center_x = 146
    center_x += vel
    center_y += vel