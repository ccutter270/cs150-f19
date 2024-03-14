'''
PreLab 2
Wednesday, Sept 18th

'''

#Example Functions from turtle

    #Actual prelab is the drawing

from turtle import *
from random import randint

def square(length):
    """ Draw a square with sides of length """
    forward(length)
    right(90)
    forward(length)
    right(90)
    forward(length)
    right(90)
    forward(length)
    right(90)
    
def iterative_square(length):
    """ Draw a square with sides of length using a loop """
    for i in range(4):
        forward(length)
        right(90)

def simple_star():
    """ Draw a star """
    for i in range(36):
        forward(100)
        backward(100)
        right(10)

def asterisk_star(length, spokes):
    """ Draw an asterisk star with spokes number of spokes of length length """
    angle = 360/spokes
    for i in range(spokes):
        forward(length)
        backward(length)
        right(angle)        
        
def simple_spiral():
    """ Draw a spiral """
    for i in range(50):
        forward(i*5)
        right(55)
        
# A good example is side = 200 and angle = 89
def spiral(sides, angle):
    """ Draw spiral with sides steps and update of angle """
    for i in range(sides):
        forward(i*5)
        right(angle)
    
def rotating_circles(radius, num):
    """ Draw num rotating circles with radius """
    angle = 360/num
    for i in range(num):
        circle(radius)
        right(angle)

def scribble(num_lines):
    """ Randomly draw num_lines lines """
    for i in range(num_lines):
        x = randint(-100,100)
        y = randint(-100,100)
        goto(x,y)
        
def walk(num_steps, step_size):
    """ Random walk with num_steps steps of step_size """
    for i in range(num_steps):
        angle = randint(-90, 90)
        right(angle)
        forward(step_size)

def pretty_picture():
    """ Draw random stars """
    for i in range(10):
        # Get some random values
        spokes = randint(5, 30)
        length = randint(10, 60)
        angle = randint(-90,90)
        move = randint(20, 100)

        # Move randomly somewhere else
        right(angle)
        forward(move)
        
        # Draw a random star there
        asterisk_star(length, spokes)