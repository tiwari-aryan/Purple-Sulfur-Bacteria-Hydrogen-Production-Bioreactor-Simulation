import pygame

pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans MS", 20)


class Hover:
    def __init__(self, x, y, radius, colour, text):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.text = my_font.render(text, False, (255, 255, 255))

    def is_hover(self, mouse_x, mouse_y):
        return (
            mouse_x <= self.x + self.radius
            and mouse_x >= self.x - self.radius
            and mouse_y <= self.y + self.radius
            and mouse_y >= self.y - self.radius
        )

    def draw(self, win, mouse_x, mouse_y):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)
        if self.is_hover(mouse_x, mouse_y):
            pygame.draw.circle(
                win,
                (255, 255, 255),
                (self.x, self.y),
                self.radius,
                width=self.radius - 3,
            )
            win.blit(self.text, (700, 750))
