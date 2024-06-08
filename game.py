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
position = {'x': 75, 'y': 55}
x_step = 0.09
y_step = 0.04

def set_x_position(value):
    position['x'] = value

def set_y_position(value):
    position['y'] = value

going_right = True
going_down = True

LEFT_THRESHOLD = 0
RIGHT_THRESHOLD = 400
UP_THRESHOLD = 0 
DOWN_THRESHOLD = 400

PLAYER_WIDTH = 20

squares = []
SQUARE_QUANTITY = 150

def add_square(new_x_position, new_y_position, r, g, b):
    squares.append(
        {'position': 
         {
             'x': new_x_position, 
             'y': new_y_position
         },
         'color': (r, g, b)})
    if len(squares) > SQUARE_QUANTITY:
        squares.pop(0)

iteration = 0


color_r = 210 
color_r_going_up = True

color_g = 150
color_g_going_up = True

color_b = 90 
color_b_going_up = True

COLOR_CHANGE_STEP = 0.06

while running:
    iteration += 1
    # Drawing whole canvas
    pygame.draw.rect(screen, BLACK, (0, 0, 400, 400))

    horizontal_step = x_step if going_right else -x_step
    vertical_step = y_step if going_down else -y_step

    new_x_position = position['x'] + horizontal_step
    new_y_position = position['y'] + vertical_step

    if position['x'] > RIGHT_THRESHOLD:
        going_right = False
    if position['x'] < LEFT_THRESHOLD + PLAYER_WIDTH:
        going_right = True

    if position['y'] > DOWN_THRESHOLD:
        going_down = False
    if position['y'] < UP_THRESHOLD + PLAYER_WIDTH:
        going_down = True

    if iteration % 60 == 0:
        add_square(new_x_position, new_y_position, color_r, color_g, color_b)

    set_x_position(new_x_position)
    set_y_position(new_y_position)

    if color_r > 252:
        color_r_going_up = False
    if color_r < 2:
        color_r_going_up = True

    if color_g > 252:
        color_g_going_up = False
    if color_g < 2:
        color_g_going_up = True

    if color_b > 252:
        color_b_going_up = False
    if color_b < 2:
        color_b_going_up = True

    color_r_step = COLOR_CHANGE_STEP if color_r_going_up else -COLOR_CHANGE_STEP
    color_g_step = COLOR_CHANGE_STEP if color_g_going_up else -COLOR_CHANGE_STEP
    color_b_step = COLOR_CHANGE_STEP if color_b_going_up else -COLOR_CHANGE_STEP
            
    color_r += color_r_step
    color_g += color_g_step
    color_b += color_b_step

    # Drawing trail
    for square in squares:
        pygame.draw.rect(screen, 
                         (square['color'][0], 
                          square['color'][1], 
                          square['color'][2]),
                         (square['position']['x'] - PLAYER_WIDTH,
                          square['position']['y'] - PLAYER_WIDTH, 
                         PLAYER_WIDTH, PLAYER_WIDTH))

    # Drawing player
    pygame.draw.rect(screen, (color_r, color_g,color_b), (position['x'] - PLAYER_WIDTH, position['y'] - PLAYER_WIDTH, PLAYER_WIDTH, PLAYER_WIDTH))

    #1 Process input/events
    # clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():  # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()
