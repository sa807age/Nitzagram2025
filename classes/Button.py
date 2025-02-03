import pygame

class Button:
    """
    A class used to represent a Button on the screen
    """
    def __init__(self, x_pos, y_pos, width, height, action=None):
        """
        Constructor

        :param x_pos: int
            Position of the top left corner of the button in X axis
        :param y_pos: int
            Position of the top left corner of the button in Y axis
        :param width: int
            Width of button in pixels
        :param height: int
            Height of button in pixels
        :param action: function
            A function that is called when the button is clicked
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.action = action

    def draw(self, screen, color=(255, 255, 255)):
        """
        Draw the button on the screen.

        :param screen: pygame.Surface
            The surface to draw the button on (e.g., the game screen).
        :param color: tuple
            The color of the button (default is white).
        """
        pygame.draw.rect(screen, color, (self.x_pos, self.y_pos, self.width, self.height))

    def button_in_mouse(self, mouse_pos):
        """
        Check if the mouse click is within the bounds of the button.

        :param mouse_pos: tuple
            The (x, y) position of the mouse click.
        :return: bool
            True if the click is within the button, False otherwise.
        """
        if self.x_pos <= mouse_pos[0] <= self.x_pos + self.width and self.y_pos <= mouse_pos[1] <= self.y_pos + self.height:
            return True
        return False

    def click_action(self, mouse_pos):
        """
        Trigger the button action if clicked.

        :param mouse_pos: tuple
            The (x, y) position of the mouse click.
        """
        if self.button_in_mouse(mouse_pos):
            if self.action:
                self.action()  # Call the action function if it's defined


