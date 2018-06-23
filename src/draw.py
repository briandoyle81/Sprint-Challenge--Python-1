import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [245, 245, 245]
PADDLE_COLOR = [179,120,211]
BLOCK_COLOR = [0,0,0]
BALL_COLOR = [210,105,30]

# TODO: random RGB color generator for Blocks to be Destroyed
def rgb_color():
   return [random.randint(150, 255),random.randint(150, 255),random.randint(150, 255)]
    


def debug_create_objects(object_list):
    
    kinetic = GameBall(1, object_list, 
                                    SCREEN_SIZE, # bounds
                                    # randomized starting position 
                                    Vector2(random.randint(30, SCREEN_SIZE[0] - 10), random.randint(10, SCREEN_SIZE[1] - 10)),
                                    # velocity
                                    # Two random numbers between -2 and 2 -- Why would you randomize the velocity?
                                    Vector2(-8, 8), # was `4*random.random() - 2`
                                    BALL_COLOR, # color
                                    10) # radius
    object_list.append(kinetic)

    for i in range(5):
        block=StrongBlock(3, Vector2(20 + i * 80, 20), 40, 40, BLOCK_COLOR)
        object_list.append(block)
    # for i in range(5):
    #     block=StrongBlock(3, Vector2(60 + i * 80, 60), 40, 40, BLOCK_COLOR)
    #     object_list.append(block)
    # for i in range(5):
    #     block=StrongBlock(3, Vector2(20 + i * 80, 100), 40, 40, BLOCK_COLOR)
    #     object_list.append(block)
    # for i in range(5):
    #     block=StrongBlock(3, Vector2(60 + i * 80, 140), 40, 40, BLOCK_COLOR)
    #     object_list.append(block)
    # for i in range(5):
    #     block=StrongBlock(3, Vector2(20 + i * 80, 180), 40, 40, BLOCK_COLOR)
    #     object_list.append(block)
    # for i in range(5):
    #     block=StrongBlock(3, Vector2(60 + i * 80, 220), 40, 40, BLOCK_COLOR)
    #     object_list.append(block)
            

    paddle = Paddle(Vector2(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]-50),
                         200, 
                         20, 
                         PADDLE_COLOR)
    object_list.append(paddle)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
 
    while len(object_list) > 2: # TODO:  Create more elegant condition for loop
        right = False
        left = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
            # print(object_list[1].position[0])
            # object_list[1].position[0] += 1
            # print(object_list[1].position[0])
            pass
            
            
            
        if keys[pygame.K_RIGHT]:
            right = True
            # Do something
            # print(object_list[0]) # ball.GameBall object x 8
            # print(object_list[1]) # block.KineticBlock object x 1
            # print(object_list[2]) # block.KineticBlock object x 1
            # print(len(object_list)) # 10... 1 ball, 1 user block, 8 blocks to destroy
            # print(object_list[1].position[0])
            # object_list[1].position[0] -= 1
            # print(object_list[1].position[0])
            # TODO: Figure out how to implement super().update() .. like in OOP-Toy            
            pass

        for object in object_list:
            object.update(left= left, right=right, pygame = pygame, object_list = object_list)
            object.check_collision()
 
        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
