import pygame

from pygame.math import Vector2
from pygame import Rect

class Block:
    """
    Base class for square or rectangular object
    """

    def __init__(self, position, width, height, color):
        # Create a rectangle centered around the x and y
        self.position = position
        self.width = width
        self.height = height
        self.rectangle = pygame.Rect(
                                    position.x - (width/2),
                                    position.y - (height/2),
                                    width,
                                    height)
        self.color = color
        self.touched_by_ball = False


    def update(self, **kwargs):
        self.touched_by_ball = False

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass

class RegularBlock(KineticBlock):
    def __init__(self, position, width, height, color, object_list):
        self.object_list = object_list
        super().__init__(position, width, height, color)
        self.hit = 0
    
    def check_collision(self):
        if self.touched_by_ball == True:
            self.object_list.remove(self)

class RainbowBlock(RegularBlock):
    def __init__(self, position, width, height, color, object_list):
        self.object_list = object_list
        super().__init__(position, width, height, color, object_list)

    def check_collision(self):
        if self.touched_by_ball == True:
            self.hit += 1
            if self.hit == 1:
                self.color = [100, 100, 100]
            if self.hit == 2:
                self.color = [0, 0, 0]
            if self.hit == 3:
                self.color = [255, 255, 0 ]
            if self.hit == 4:
                self.color = [255, 0, 255]
            if self.hit >= 5:
                self.object_list.remove(self)

# The above allows the Rainbow Block to take a certain number of hits before vanishing
# I was making this way too complicated. I tried using self.should_draw but it wasn't working so I figured the base Block has a self.touched_by_ball, so maybe I ought to use that.
# Then maybe I could count whether it got hit and then change color once before removing. Not working 100% but I feel very close. 
# Ok, finally working. I decided to count up instead of down, which helped. I also renamed the method to refer to the check_collision from ball.py. Not sure if that was what did the trick as I did a lot of things at the same time.

class Paddle(KineticBlock):
    def __init__(self, position, width, height, color):
        super().__init__(position, width, height, color)

    def update(self, **kwargs):
        self.rectangle = pygame.Rect(
                                self.position.x - (self.width/2),
                                self.position.y - (self.height/2),
                                self.width,
                                self.height)
        self.rectangle = pygame.Rect(
                                self.position.x - (self.width/2),
                                self.position.y - (self.height/2),
                                self.width,
                                self.height)
        super().update()

