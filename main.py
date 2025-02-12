#MAIN.PY
from pacman import Pacman
from enemy import Enemy
from food import Food
import pygame
import random

''' 
The above section imports the classes Pacman, Enemy and Food from their respective files. 
Pacman, Enemy, and Food are implemented as separate classes to ensure modularity.
This allows for easier debugging, testing, and modification of individual game components without affecting the rest of the code.
Each class handles its own data (position, movement, and drawing), following object-oriented programming principles.
It also imports the pygame module so we can use those features, and also the random mdoule to generate random numbers for the food and enemy
'''
#--------------------------------------------------------------------------------
pygame.init() # Initialise the pygame module

# Setup
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

# Creating a display window
display = pygame.display.set_mode(DISPLAY_SIZE)

# Characteristics of the display
black = (0, 0, 0)
clock = pygame.time.Clock() # Clock object to control the frame rate

# Creating Pacman
'''
Creating an instance of the Pacman class inputting the coordinates, radius, colour and speed of the pacman.
'''
pacman = Pacman(DISPLAY_WIDTH // 2, 50, 20,(252, 3, 198), 3) 

# Creating Enemy
'''
Creating an instance of the Enemy class inputting the coordinates, radius, colour and speed of the enemy.
'''
enemy = Enemy(250, 400, 20, (200, 75, 250), 1)

# Creating Food
'''
Creating an instance of the food class inputting the coordinates, radius and colour of the food.
'''
food = Food(random.randint(20, DISPLAY_WIDTH - 20), random.randint(20, DISPLAY_HEIGHT - 20), 10, (242, 216, 237))

#--------------------------------------------------------------------------------

# GAME LOOP
'''
This section of code is the game loop. It runs the game until the user quits the game. 
It also checks for user input through key presses and key releases to move the pacman in the desired direction.
First, we have to set run_game to True to run the game. We also have to set the direction of the pacman to False initially.
This is done to prevent the pacman from moving in multiple directions at the same time, and wait for user input.

'''
run_game = True
is_moving_down = False
is_moving_up = False
is_moving_left = False
is_moving_right = False

while run_game:
    display.fill(black) # Fill the display with black colour
    
    pacman.draw(display) # Draw Pacman
    enemy.draw(display)  # Draw the enemy
    food.draw(display)   # Draw the food
    
    for event in pygame.event.get(): # Check for events
        '''
        Event-driven programming is essential for interactive games because
        it allows the game to respond to user inputs (like key presses) and system events (like quitting the game).
        This approach ensures smooth gameplay, as actions occur based on events rather than a fixed sequence of commands.
        '''
        if event.type == pygame.QUIT: # If the user quits the game, set run_game to False
            run_game = False
        elif event.type == pygame.KEYDOWN: # If the user presses a key, check which key it is
            if event.key == pygame.K_DOWN: # If the key is the down key, set the direction of Pacman to down
                is_moving_down = True # Set the direction of the pacman to down
                '''
                The following lines of code ensure that Pacman can only move in one direction at a time. If these were
                not set to false, the controls would not work as anticipated and Pacman would be attempting to move
                in different directions at the same time.
                '''
                is_moving_up = False 
                is_moving_left = False
                is_moving_right = False
            if event.key == pygame.K_UP: # If the key is the up key, set the direction of Pacman to up
                is_moving_up = True # Set the direction of the pacman to up, and so on for the rest of these keys.
                is_moving_down = False #As above!
                is_moving_left = False
                is_moving_right = False
            if event.key == pygame.K_LEFT: # If the key is the left key, set the direction of Pacman to left
                is_moving_left = True
                is_moving_right = False
                is_moving_up = False
                is_moving_down = False
            if event.key == pygame.K_RIGHT: # If the key is the right key, set the direction of Pacman to right
                is_moving_right = True
                is_moving_left = False
                is_moving_up = False
                is_moving_down = False
        elif event.type == pygame.KEYUP: # If the user releases a key, check which key it is
            if event.key == pygame.K_DOWN: # If the key is the down key, set the direction of Pacman to False
                is_moving_down = False
            if event.key == pygame.K_UP: # If the key is the up key, set the direction of Pacman to False
                is_moving_up = False
            if event.key == pygame.K_LEFT: # If the key is the left key, set the direction of Pacman to False
                is_moving_left = False
            if event.key == pygame.K_RIGHT: # If the key is the right key, set the direction of Pacman to False
                is_moving_right = False
        '''
        The above section unsures that Pacman stops moving when the player releases the key specified. 
        '''
#--------------------------------------------------------------------------------
    # IMPLEMENTING MOVEMENT AND COLLISIONS
    '''
    The below section of code implements the functions defined in pacman.py, enemy.py and food.py to 
    move Pacman, move the enemy and check for collisions between Pacman, the enemy and the food.
    '''
    
    #Pacman
    if is_moving_down: 
        pacman.move_down(DISPLAY_HEIGHT) 
    if is_moving_up:
        pacman.move_up(DISPLAY_HEIGHT)
    if is_moving_left:
        pacman.move_left(DISPLAY_WIDTH)
    if is_moving_right:
        pacman.move_right(DISPLAY_WIDTH)

    #Enemy
    '''
    This section of code ensures that the enemy follows the food by moving towards it whereever its position is.
    '''
    if enemy.get_x() < food.get_x(): # If the enemy is to the left of the food, move right
        enemy.move("RIGHT", DISPLAY_WIDTH, DISPLAY_HEIGHT) #Display width and height are passed as arguments to ensure the enemy does not go off the screen
    elif enemy.get_x() > food.get_x(): # If the enemy is to the right of the food, move left
        enemy.move("LEFT", DISPLAY_WIDTH, DISPLAY_HEIGHT)
    if enemy.get_y() < food.get_y(): # If the enemy is above the food, move down
        enemy.move("DOWN", DISPLAY_WIDTH, DISPLAY_HEIGHT)
    elif enemy.get_y() > food.get_y(): # If the enemy is below the food, move up
        enemy.move("UP", DISPLAY_WIDTH, DISPLAY_HEIGHT)

    #Collisions
    '''
    This section of code checks for collisions between Pacman, the enemy and the food. 
    If Pacman collides with the food, Pacman and the food are relocated to a random position on the screen.
    This is done by calling the relocate method from the Pacman and Food classes.
    We use getters to get the x and y coordinates of the circles and see are they overlapping.
    Collision detection is based on the distance formula: (x1 - x2)^2 + (y1 - y2)^2 < (r1 + r2)^2.
    This checks if the distance between two objects is less than the sum of their radii, indicating an overlap (i.e., a collision).
    '''
    
    if (pacman.get_x() - food.get_x())**2 + (pacman.get_y() - food.get_y())**2 < (pacman.get_radius() + food.get_radius())**2:
        pacman.relocate(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        food.relocate(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    if (enemy.get_x() - food.get_x())**2 + (enemy.get_y() - food.get_y())**2 < (enemy.get_radius() + food.get_radius())**2:
        enemy.relocate(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        food.relocate(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    if (enemy.get_x() - pacman.get_x())**2 + (enemy.get_y() - pacman.get_y())**2 < (enemy.get_radius() + pacman.get_radius())**2:
        enemy.relocate(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        pacman.relocate(DISPLAY_WIDTH, DISPLAY_HEIGHT)

    pygame.display.update() # Update the display so the changes are visible
    clock.tick(60) # Set the frame rate to 60 frames per second

pygame.quit() # Quit the game
quit() # Exit the program
#These are both used so that the game quits and the program also exits when the user closes the game window.

#--------------------------------------------------------------------------------
#CODE SUMMARY
'''

The main.py file is the main file that runs the game. It imports the classes from other files, and then uses these within the main game. 
We start by importing the pygame module and the random module, so that all the pygame functionality can be used along with the random number generation.
We then import the classes from the other files (pacman.py, enemy.py and food.py)
The window is set up using DISPLAY_WIDTH and DISPLAY_HEIGHT
A clock object is created to control the frame rate of the game
We create instances of the Pacman, Enemy and Food classes, passing in the required parameters
We set the run_game variable to True to run the game, and set the direction of the pacman to False initially
We then enter the game loop, which runs until the user quits the game.

'''

#--------------------------------------------------------------------------------