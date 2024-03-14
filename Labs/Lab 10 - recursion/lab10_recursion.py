"""
This program contains recursive functions such as Recursive H, Stairs and a Recursive triangle function. When the program is run
a turtle function of Stair is immediatly called and prints out a stair of length 128.

CSCI150 Fall 2019 Lab 10

Name: Caroline Cutter
Section: <B>

Creativity:

    - I created the rec_count function that counts the number of repetitions an item is an a list
    - I added color change to the recursive_H fucntion
    - I created a recursive triangle function that creates an abstract picture with triangles
    
    
"""

#Imports
from turtle import *
import sys
from random import randint
from math import *


'''
Warming up Functions
'''


def length(a_list):
    '''
    Gives the length of a list using recursion
    
    Args:
        a_list: a list
    
    Returns:
        length of a_list using recursion

    '''
    if a_list == []:
        return 0
    else:
        return 1 + length(a_list[1:])



def rec_max(a_list):
    '''
    Finds the max value of a list using recursion
    
    Args:
        a_list: a list
    
    Returns:
        max value in a_list using recursion

    '''
    if len(a_list) == 1:
        return a_list[0]
    else:
        max_rest = rec_max(a_list[1:])
        if max_rest > a_list[0]:
            return max_rest
        else:
            return a_list[0]
        
 
 
'''
Creativity Functions
'''

def rec_count(a_list, item):
    '''
    Counts how many times an item appears in the list using recursion
    
    Args:
        a_list: a list
        item: item that is being counted in the list
    
    Returns:
        How many times item appears in a_list

    '''
    if a_list == []: #base case, when list is empty
        return 0
    else:
        if a_list[0] == item: #if item is in list, add one plus everything else
            return 1 + rec_count(a_list[1:], item)
        else: #if item is not in list, add 0 plus everything else
            return 0 + rec_count(a_list[1:], item)

    
def recursive_triangle(x, y, length):
    '''
    Draws a recursive triangle in python
    
    Args:
        x: x-coordinate
        y: y-coordinate
        length: desired length of largest triangle


    '''
    speed(0)
    color = [0, randint(1,100)/100, randint(1,100)/100]
    if length < 3:
        return None
    else:
        for i in range(3): 
            forward(length)
            pencolor(color)
            recursive_triangle(xcor(), ycor() , length/2)
            right(120)




'''
Recursive H Functions
'''
    

def draw_line(x1, y1, x2, y2, color):
    '''
    Draws a line
    
    Args:
        x1: beginning x-coordinate
        y1: beginning y-coordinate
        x2: ending x-coordinate
        y2: enging y-coordinate
        color: desired color of line
    '''
    pencolor(color)
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)



def draw_H(x_coord, y_coord, length, color):
    '''
    Draws an H with dot at the ends of the stems
    
    Args:
        x_coord: x-coordinate
        y_coord: y-coordinate
        length: desired length of H
        color: desired color of H
    '''

    draw_line(x_coord - length, y_coord, x_coord + length, y_coord, color)
    draw_line(x_coord - length, y_coord + length / 2, x_coord - length, y_coord - length / 2, color)
    draw_line(x_coord + length, y_coord + length /2, x_coord + length, y_coord - length / 2, color)



def recursive_H(x_coord, y_coord, length, num_recursion):
    '''
    Draws a recursive H
    
    Args:
        x_coord: x-coordinate
        y_coord: y-coordinate
        length: desired length of largest H
        num_recursions: number of recursions of recursive H
    '''
    speed(0)
    if num_recursion == 0:
        penup()
        goto(x_coord, y_coord)
        dot(5)
    else:
        draw_H(x_coord, y_coord, length, tuple([0, length/(length+10) , length/(length+5)]))
        
        num_recursion -= 1
        
        recursive_H(x_coord + length, y_coord + length/2, length / 2, num_recursion)
        recursive_H(x_coord + length, y_coord - length/2, length / 2, num_recursion)
        recursive_H(x_coord - length, y_coord + length/2, length / 2, num_recursion)
        recursive_H(x_coord - length, y_coord - length/2, length / 2, num_recursion)

        



'''
Stairs Functions
'''
def draw_square(x_coord, y_coord, length, color):
    '''
    Draws a square
    
    Args:
        x_coord: x-coordinate
        y_coord: y-coordinate
        length: desired length of sides of square
        color: desired color of square
    '''
    fillcolor(color)
    penup()
    goto(x_coord, y_coord)
    setheading(90)
    pendown()
    begin_fill()
    for i in range(4):
       forward(length)
       right(90)
    end_fill()
    
    


def stairs(x_coord, y_coord, length):
    '''
    Draws a staircase using recursion
    
    Args:
        x_coord: x-coordinate
        y_coord: y-coordinate
        length: desired length of largest square in stairs
        
    Returns:
        number of squares in the stairs
        
    '''
    speed(0)
    
    if length <= 3:
        return 0
    else:
        draw_square(x_coord, y_coord, length, tuple([0, length/(length+10), length/(length+5)]))
       
        squares = 1
        
        squares += stairs(x_coord + length, y_coord, length / 2)
        squares += stairs(x_coord, y_coord + length, length / 2)
       
       
        return squares
    
    



if __name__ == "__main__": 
        num_stairs = stairs(0, 0, 128)
        penup()
        goto(0, -15)
        write("Stairs with {} squares".format(num_stairs))



'''
This is a run statement that could be used if the user wanted the program to ask for the inputs of the stairs function.
Right now, the program has set inputs

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('usage: python3 lab10_recursion.py <x_coord> <y_coord> <length>')
    else:
        num_stairs = stairs(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))  
        penup()
        goto(int(sys.argv[1]), int(sys.argv[2]) - 15)
        write("Stairs with " + str(num_stairs) + " squares")
'''



