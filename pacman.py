#PACMAN.PY
import pygame #Importing the pygame module
import random #Importing the random module
#--------------------------------------------------------------------------------
class Pacman: #Creating the Pacman class, which takes self, x and y coordinates, radius, colour of pacman and the speed
    def __init__(self, x, y, radius, colour, speed):
        self._x = x
        self._y = y
        self._radius = radius 
        self._colour = colour
        self._speed = speed

    def __str__(self): #This is a string representation of the object, which can be called to check the position and colour of the object
        return f"Pacman at ({self._x}, {self._y}) with colour {self._colour}"

    def draw(self, display): #This function will draw Pacman as a circle, it takes the parameters of self and display (self having colour, coordinates and radius)
        pygame.draw.circle(display, self._colour, (self._x, self._y), self._radius)

    def move_down(self, display_height): #The move down function essentially changes the coordinates based on the speed. So every frame, the coordinates change by the speed specified.
        self._y += self._speed
        if self._y > display_height - self._radius: #The following two lines of code mean that Pacman reappears at the top when he moves to the bottom. 
            self._y = 0 + self._radius #This is done to ensure that Pacman does not disappear off the screen.

    def move_up(self, display_height): #The movement functions work in the same way as the move down function, but for different directions.
        self._y -= self._speed
        if self._y < 0:  # Move to bottom if it goes beyond the top
            self._y = display_height - self._radius

    def move_left(self, display_width):
        self._x -= self._speed
        if self._x < 0:  # Move to right edge if it goes beyond the left
            self._x = display_width - self._radius

    def move_right(self, display_width):
        self._x += self._speed
        if self._x > display_width:
            self._x = 0 + self._radius

    def relocate(self, display_width, display_height): #This function relocates Pacman to a random position on the screen, by setting the x and y coordinates to random integers.
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
This file contains the Pacman class, which is used to create a Pacman object within the game.
The Pacman object has attributes such as x and y coordinates, radius, colour and speed.
The class contains methods such as draw, move_down, move_up, move_left, move_right, relocate
and getters for the x and y coordinates and radius.
The draw method is used to draw Pacman as a circle on the screen.
The move methods are used to move Pacman in different directions based on the speed specified.
The relocate method is used to relocate Pacman to a random position on the screen.
The getters are used to get the x and y coordinates and radius of the Pacman object.
'''
#--------------------------------------------------------------------------------