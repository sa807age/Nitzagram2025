import pygame

class Button:
    def __init__(self, x_pos, y_pos, width, height, text="Button"):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.font = pygame.font.SysFont('chalkduster.ttf', 20)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.x_pos + 10, self.y_pos + 5))

    def button_in_mouse(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)





