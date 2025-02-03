import pygame

class Comment:
    """
    A class to represent a Comment on a Post.
    """
    def __init__(self, text, index):
        """
        Constructor to initialize the comment.

        :param text: str
            The text of the comment.
        :param index: int
            The index of the comment, used to position it vertically.
        """
        self.text = text
        self.index = index  # To manage the position of comments

    def display(self, screen, font, color=(255, 255, 255), line_height=30):
        """
        Display the comment on the screen.

        :param screen: pygame.Surface
            The surface to display the comment on (e.g., the game screen).
        :param font: pygame.font.Font
            The font to render the comment text.
        :param color: tuple
            The color of the text (default is white).
        :param line_height: int
            The vertical distance between each comment.
        """
        # Calculate the vertical position based on the index of the comment
        y_pos = 200 + self.index * line_height  # Adjust starting position (e.g., 200) as needed
        text_surface = font.render(self.text, True, color)
        screen.blit(text_surface, (50, y_pos))  # Adjust horizontal position (e.g., 50) as needed

    @staticmethod
    def user_from_comment_read():
        """
        This function opens a text input dialog and returns the typed comment.
        """
        # Assuming this function is for getting user input (you can replace it with your actual function)
        user_input = input("Enter your comment: ")  # You can replace this with your custom dialog
        return user_input
