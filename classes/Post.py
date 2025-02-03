import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, username, location, description, comments: list, likes_counter=0):
        self.username = username
        self.location = location
        self.description = description
        self.comments = comments
        self.likes_counter = likes_counter


    def add_like(self):
        self.likes_counter += 1


    def add_comments(self, text):
        self.comments.append(text)


class ImagePost(Post):
    def __init__(self, username, location, description, comments: list, photo, likes_counter=0):
        self.photo = photo
        super().__init__(username, location, description, comments, likes_counter)


    def display(self):
        img_photo = pygame.image.load(self.photo)
        img_photo = pygame.transform.scale(img_photo, (POST_WIDTH, POST_HEIGHT))
        screen.blit(img_photo, (POST_X_POS, POST_Y_POS))


class TextPost(Post):
    def __init__(self, username, location, description, comments: list, text, likes_counter=0):
        self.text = text
        super().__init__(username, location, description, comments, likes_counter)


    def display(self):
        img_text = pygame.image.load(self.text)
        img_text = pygame.transform.scale(img_text, (POST_WIDTH, POST_HEIGHT))
        screen.blit(img_text, (POST_X_POS, POST_Y_POS))






    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



