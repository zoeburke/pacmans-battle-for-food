#FOOD.PY
import pygame #Importing the pygame module
import random #Importing the random module to be used in the relocate function

#--------------------------------------------------------------------------------

class Food: #Creating the Food class, which takes self, x and y coordinates, radius and colour of the food
    def __init__(self, x, y, radius, colour):
        self._x = x
        self._y = y
        self._radius = radius
        self._colour = colour #Used an instance variable here instead of specifying the colour within the class so that the colour can be changed in the main file and allows for more flexibility.

    def __str__(self): #This is a string representation of the object, which can be called to check the position and colour of the object
        return f"Food at ({self._x}, {self._y}) with colour {self._colour}"

    def draw(self, display): #This function will draw the food as a circle, it takes the parameters of self and display (self having colour, coordinates and radius)
        pygame.draw.circle(display, self._colour, (self._x, self._y), self._radius)

    def relocate(self, display_width, display_height): #This function relocates the food to a random position on the screen, by setting the x and y coordinates to random integers.
        self._x = random.randint(self._radius, display_width - self._radius) #This is done to ensure that the food does not disappear off the screen.
        self._y = random.randint(self._radius, display_height - self._radius) 

    def get_x(self): #This function returns the x coordinate of the food
        return self._x

    def get_y(self): #This function returns the y coordinate of the food
        return self._y

    def get_radius(self): #This function returns the radius of the food
        return self._radius

#--------------------------------------------------------------------------------
#CODE SUMMARY
'''
This file has all of the code for the food class, which is used to create a food object within the game for the Pacman and Enemy to chase.
The food object has attributes such as x and y coordinates, radius and colour.
The class contains methods such as draw, relocate and getters for the x and y coordinates and radius.
The draw method is used to draw the food as a circle on the screen.
The relocate method is used to relocate the food to a random position on the screen.
The getters are used to get the x and y coordinates and radius of the food object.
'''

#--------------------------------------------------------------------------------