import pygame
from constants import *
from classes.Post import TextPost
from buttons import Button
from helpers import screen

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Nitzagram")

    clock = pygame.time.Clock()

    # Создаем несколько объектов постов
    post1 = TextPost("This is a test post. It's a very long post that should wrap nicely on the screen.", color_text=(255, 255, 255), color_background=(0, 0, 0))
    post2 = TextPost("Another test post, this time with some different content.", color_text=(0, 0, 255), color_background=(255, 255, 255))

    posts = [post1, post2]
    current_post = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                post = posts[current_post]
                action = post.handle_click(mouse_pos)
                if action == "like":
                    # Добавить лайк
                    pass
                elif action == "comment":
                    # Открыть окно комментариев
                    pass
                elif action == "share":
                    # Поделиться постом
                    pass
                # Переход к следующему посту
                if current_post < len(posts) - 1:
                    current_post += 1
                else:
                    current_post = 0

        # Обновляем экран
        screen.fill(BLACK)
        posts[current_post].display(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

main()
