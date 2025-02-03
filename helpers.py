import pygame
from constants import *  # Все константы импортированы из constants.py

# Инициализация экрана с размерами из constants.py
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)

def from_text_to_array(text):
    """
    Разбивает текст на строки, которые помещаются на экране.
    :param text: строка текста
    :return: список строк, которые помещаются на экран
    """
    text_array = []
    text_to_edit = text
    # Если текст длиннее максимальной длины строки
    if len(text) > LINE_MAX_LENGTH:
        while len(text_to_edit) > 0:
            if len(text_to_edit) < LINE_MAX_LENGTH:
                text_array.append(text_to_edit)
                text_to_edit = ""
            else:
                temp = text_to_edit[:LINE_MAX_LENGTH]
                text_to_edit = text_to_edit[LINE_MAX_LENGTH:]
                while not (temp[-1] == ' ' or temp[-1] == ','):  # Проверяем, не обрезать ли слово
                    text_to_edit = temp[-1] + text_to_edit
                    temp = temp[:-1]
                text_array.append(temp)
    else:
        text_array.append(text)
    return text_array

def mouse_in_button(button, mouse_pos):
    """
    Проверяет, находится ли клик мыши внутри кнопки.
    :param button: объект Button
    :param mouse_pos: кортеж (x, y) координат мыши
    :return: boolean
    """
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True
    return False

def draw_comment_text_box():
    """
    Рисует текстовое поле для ввода комментария.
    Используется цвет из constants.py для фона.
    """
    pygame.draw.rect(screen, BLACK, pygame.Rect(COMMENT_BUTTON_X_POS, COMMENT_BUTTON_Y_POS, 300, 20))  # Серый цвет
    pygame.draw.rect(screen, WHITE, pygame.Rect(COMMENT_BUTTON_X_POS + 1, COMMENT_BUTTON_Y_POS + 1, 298, 18))
    pygame.display.flip()

def read_comment_from_user():
    """
    Читает комментарий, который вводит пользователь.
    :return: строка с введенным комментарием
    """
    pressed_enter = False
    new_comment = ""
    draw_comment_text_box()  # Рисуем поле для ввода комментария
    while not pressed_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                draw_comment_text_box()  # Перерисовываем поле при каждом изменении
                if event.key == pygame.K_RETURN:
                    pressed_enter = True  # Заканчиваем ввод
                elif event.key == pygame.K_BACKSPACE and new_comment:
                    new_comment = new_comment[:-1]  # Удаляем последний символ
                else:
                    new_comment += event.unicode  # Добавляем символ
                font2 = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE, bold=False)  # Убедитесь, что файл шрифта доступен
                img2 = font2.render(new_comment, True, BLACK)
                screen.blit(img2, (COMMENT_BUTTON_X_POS + 1, COMMENT_BUTTON_Y_POS + 1))
                pygame.display.update()
    return new_comment

def center_text(num_of_rows, text_to_display, row_number):
    """
     Центрирует текст на экране.
     :param num_of_rows: int, количество строк
     :param text_to_display: строка, текст для отображения
     :param row_number: номер строки текста на экране
     :return: кортеж с координатами (x, y)
     """
    horizontal_margin = (POST_HEIGHT - num_of_rows * TEXT_POST_FONT_SIZE) // 2
    text_rect = text_to_display.get_rect()
    text_rect.x = ((POST_WIDTH - text_rect.width) // 2) + 20  # Центрирование по оси X
    text_rect.y = (POST_Y_POS + horizontal_margin + row_number * TEXT_POST_FONT_SIZE)  # Центрирование по оси Y
    return text_rect



