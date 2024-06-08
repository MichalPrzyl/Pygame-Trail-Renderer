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
x_step = 0.05
y_step = 0.02

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
SQUARE_QUANTITY = 15

def add_square(new_x_position, new_y_position):
    squares.append({'position': {'x': new_x_position, 'y': new_y_position}})
    if len(squares) > SQUARE_QUANTITY:
        squares.pop(0)

iteration = 0
while running:
    iteration += 1
    # Drawing whole canvas
    pygame.draw.rect(screen, BLACK, (0, 0, 400, 400))
    print(f"{squares}")

    for square in squares:
        pygame.draw.rect(screen, 
                         GREEN,
                         (square['position']['x'], square['position']['y'], 
                         PLAYER_WIDTH, PLAYER_WIDTH))


    horizontal_step = x_step if going_right else -x_step
    vertical_step = y_step if going_down else -y_step

    # print(f"horizontal_step: {horizontal_step}")
    # Changing position
    new_x_position = position['x'] + horizontal_step
    new_y_position = position['y'] + vertical_step

    # Changing X direction
    # print(f"new_x_position: {new_x_position}")
    #
    # print(f"position['x']: {position['x']} - RIGHT_THRESHOLD: {RIGHT_THRESHOLD}")

    if position['x'] > RIGHT_THRESHOLD:
        going_right = False
    if position['x'] < LEFT_THRESHOLD + PLAYER_WIDTH:
        going_right = True

    if position['y'] > DOWN_THRESHOLD:
        going_down = False
    if position['y'] < UP_THRESHOLD + PLAYER_WIDTH:
        going_down = True
    # # Changing Y direction
    # print(f"new_y_position: {new_y_position}")
    # if new_y_position > DOWN_THRESHOLD or new_y_position < UP_THRESHOLD:
    #     going_down = not going_down

    set_x_position(new_x_position)
    set_y_position(new_y_position)

    if iteration % 5 == 0:
        add_square(new_x_position, new_y_position)

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
