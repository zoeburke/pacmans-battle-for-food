#ENEMY.PY
import pygame #Importing the pygame module
import random #Importing the random module to be used in the relocate function
#--------------------------------------------------------------------------------
class Enemy: #Creating the Enemy class, which takes self, x and y coordinates, radius, colour of the enemy and the speed
    def __init__(self, x, y, radius, colour, speed):
        self._x = x
        self._y = y
        self._radius = radius
        self._colour = colour
        self._speed = speed
        
    def __str__(self): #This is a string representation of the object, which can be called to check the position and colour of the object
        return f"Enemy at ({self._x}, {self._y}) with colour {self._colour}"
    
    def draw(self, display): #This function will draw the enemy as a circle, it takes the parameters of self and display (self having colour, coordinates and radius)
        pygame.draw.circle(display, self._colour, [self._x, self._y], self._radius)

    def move(self, direction, display_width=None, display_height=None): #This function moves the enemy based on the direction specified and the speed of the enemy
        if direction == "UP": #If the direction is up, the y coordinate decreases by the speed
            self._y -= self._speed 
            if self._y - self._radius < 0:  # Move to bottom if it goes beyond the top 
                self._y = self._radius  
        elif direction == "DOWN": #If the direction is down, the y coordinate increases by the speed
            self._y += self._speed
            if display_height and self._y + self._radius > display_height: # Move to top if it goes beyond the bottom
                self._y = display_height - self._radius
        elif direction == "LEFT": #If the direction is left, the x coordinate decreases by the speed
            self._x -= self._speed 
            if self._x - self._radius < 0: # Move to right edge if it goes beyond the left
                self._x = self._radius
        elif direction == "RIGHT": #If the direction is right, the x coordinate increases by the speed
            self._x += self._speed
            if display_width and self._x + self._radius > display_width: # Move to left edge if it goes beyond the right
                self._x = display_width - self._radius 
                
    def relocate(self, display_width, display_height): #This function relocates the enemy to a random position on the screen, by setting the x and y coordinates to random integers.
        self._x = random.randint(self._radius, display_width - self._radius)
        self._y = random.randint(self._radius, display_height - self._radius)
    
    '''
    The functions below are getters, which return the coordinates and radius so that they can be used within the main file.
    '''
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_radius(self):
        return self._radius

#--------------------------------------------------------------------------------
#CODE SUMMARY
'''
We created this file to contain the Enemy class, which is used to create an enemy object. 
The enemy object has attributes such as x and y coordinates, radius, colour and speed.
The class contains methods such as draw, move, relocate and getters for the x and y coordinates and radius.
The draw method is used to draw the enemy as a circle on the screen.
The move method is used to move the enemy in a specified direction with a specified speed.
The relocate method is used to relocate the enemy to a random position on the screen.
The getters are used to get the x and y coordinates and radius of the enemy object.
'''
#--------------------------------------------------------------------------------