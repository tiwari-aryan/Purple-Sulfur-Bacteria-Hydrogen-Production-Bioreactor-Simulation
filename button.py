import pygame


class Button(object):
    def __init__(self, x, y, width, height, text_color, background_color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.background_color = background_color

    def check(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, screen):
        font = pygame.font.SysFont(None, 24)
        pygame.draw.rect(screen, self.background_color, (self.rect), 0)
        pygame.draw.rect(screen, self.text_color, self.rect, 3)


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
            win.blit(self.text, (800, 750))
