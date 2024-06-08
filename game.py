import pygame
import random
WIDTH, HEIGHT = (400,400)

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MP GAME")
clock = pygame.time.Clock()     ## For syncing the FPS

## Game loop
running = True

# Moving
position = {'x': 5, 'y': 55}
step = 0.1

def set_x_position(value):
    position['x'] = value

def set_y_position(value):
    position['y'] = value

going_rigt = True
going_down = True

LEFT_THRESHOLD = 0
RIGHT_THRESHOLD = 200
UP_THRESHOLD = 100 
DOWN_THRESHOLD = 200

PLAYER_WIDTH = 20

while running:

    # Drawing whole canvas
    pygame.draw.rect(screen, BLACK, (0, 0, 400, 400))

    horizontal_step = step if going_rigt else -step
    vertical_step = step if going_down else -step

    # Changing position
    new_x_position = position['x'] + horizontal_step
    new_y_position = position['y'] + vertical_step

    # Changing X direction
    # print(f"new_x_position: {new_x_position}")
    if new_x_position > RIGHT_THRESHOLD or new_x_position < LEFT_THRESHOLD:
        print(f"CHECK - 1")
        going_right = not going_rigt
    else:
        print(f"check - 2")

    # # Changing Y direction
    # print(f"new_y_position: {new_y_position}")
    # if new_y_position > DOWN_THRESHOLD or new_y_position < UP_THRESHOLD:
    #     going_down = not going_down

    set_x_position(new_x_position)
    # set_y_position(new_y_position)

    # Drawing
    pygame.draw.rect(screen, GREEN, (position['x'] - PLAYER_WIDTH, position['y'] - PLAYER_WIDTH, PLAYER_WIDTH, PLAYER_WIDTH))

    #1 Process input/events
    # clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():  # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()
