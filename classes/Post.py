import pygame
from buttons import Button
from constants import *

class TextPost:
    def __init__(self, text, color_text=(0, 0, 0), color_background=(255, 255, 255)):
        self.text = text
        self.color_text = color_text
        self.color_background = color_background

        # Создание шрифта для текста
        self.font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
        self.text_array = self.from_text_to_array(self.text)

        # Инициализация кнопок
        self.like_button = Button(LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS, LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT, "Like")
        self.comment_button = Button(COMMENT_BUTTON_X_POS, COMMENT_BUTTON_Y_POS, COMMENT_BUTTON_WIDTH, COMMENT_BUTTON_HEIGHT, "Comment")
        self.share_button = Button(SHARE_BUTTON_X_POS, SHARE_BUTTON_Y_POS, SHARE_BUTTON_WIDTH, SHARE_BUTTON_HEIGHT, "Share")

    def from_text_to_array(self, text):
        text_array = []
        text_to_edit = text
        if len(text) > 20:
            while len(text_to_edit) > 0:
                if len(text_to_edit) < LINE_MAX_LENGTH:
                    text_array.append(text_to_edit)
                    text_to_edit = ""
                else:
                    temp = text_to_edit[:LINE_MAX_LENGTH]
                    text_to_edit = text_to_edit[LINE_MAX_LENGTH:]
                    while temp and temp[-1] not in [' ', ',']:
                        temp = temp[:-1]
                    text_array.append(temp)
        else:
            text_array.append(text)
        return text_array

    def display(self, screen):
        # Отображаем фон поста
        pygame.draw.rect(screen, self.color_background, pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))

        # Отображаем текст (с разделением на строки, если нужно)
        for i, text_line in enumerate(self.text_array):
            text_surface = self.font.render(text_line, True, self.color_text)
            text_rect = text_surface.get_rect(center=(POST_X_POS + POST_WIDTH // 2, POST_Y_POS + 40 + i * TEXT_POST_FONT_SIZE))
            screen.blit(text_surface, text_rect)

        # Отображаем кнопки (лайк, комментарий, и шэр)
        self.like_button.draw(screen)
        self.comment_button.draw(screen)
        self.share_button.draw(screen)

    def check_button_click(self, mouse_pos):
        # Проверяем, был ли клик по кнопке лайка
        if self.like_button.button_in_mouse(mouse_pos):
            print("Like button clicked!")
            return "like"

        # Проверяем, был ли клик по кнопке комментариев
        if self.comment_button.button_in_mouse(mouse_pos):
            print("Comment button clicked!")
            return "comment"

        # Проверяем, был ли клик по кнопке шэра
        if self.share_button.button_in_mouse(mouse_pos):
            print("Share button clicked!")
            return "share"

        return None

    def handle_click(self, mouse_pos):
        action = self.check_button_click(mouse_pos)
        if action == "like":
            # Обработка лайка
            pass
        elif action == "comment":
            # Открыть окно для ввода комментария
            comment = self.user_from_comment_read()
            print(f"New comment: {comment}")
        elif action == "share":
            # Открыть окно для шэра
            print("Post shared!")

    def user_from_comment_read(self):
        """
        Имитация получения комментария от пользователя
        """
        pressed_enter = False
        new_comment = ""
        # В реальной ситуации, мы бы добавили код для обработки ввода
        return "This is a comment"





