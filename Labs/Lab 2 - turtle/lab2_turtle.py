"""
CSCI150 Fall 2019 Lab 2

Name: <Caroline Cutter>
Section: <B>


Creativity:

- I made a star function that randomly draw starfish in the bottom of my drawing
- I also added waves, a crab and sand by creating new functions called draw_waves(), crab() & draw_sand()
- I made my fish have fins by creating a fucntion called fish_fins() using the triangle function


"""

from turtle import *
from random import *


'''
Required functions
'''


#Equilateral Traingle Function

def triangle(x, y, length):
    '''
    Draws an equilateral traingle at specific coordinates with desired length
    
    Args:
        x: x-coordinate
        y: y-coordinate
        length: side length
    '''
    penup()
    goto(x,y)
    setheading(270)
    for i in range(3):
        pendown()
        forward(length)
        left(120)



#Polygon function
        
def polygon(x, y, sides, length, color):
    '''
    Draws and fills a polygon at specific coordinates with desired # of sides, side length and color
    
    Args:
        x: x-coordinate
        y: y-coordinate
        sides: # of sides
        length: side length
        color: desired color 
    '''
    penup()
    goto(x,y)
    setheading(0)
    begin_fill()
    for i in range(sides):
        pencolor(color)
        fillcolor(color)
        pendown()
        forward(length)
        left(360/sides)
    end_fill()
   
   
   
#Adds Random Circles  
   
def add_circles(numcircles,color):
    '''
    Draws circles with random sizes in random locations on the screen
    
    Args:
        numcircles: desired # of circles
        color: desired color
    '''
    pencolor(color)
    fillcolor(color)
    for i in range(numcircles):
        size = randint(2, 6)
        penup()
        #Y is between these random integers because I didn't want bubbles to be on sand or in waves
        goto(randint(-350,350), randint(-330,300))
        pendown()
        begin_fill()
        circle(size)
        end_fill()
        
   
   
    
'''
Extra Functions :)
'''



#Star Function
    
def star(length, color):
    '''
    Draws and fills a star
    
    Args:
        length: length of sides
        color: desired color
    '''
    setheading(60)
    fillcolor(color)
    begin_fill()
    for i in range(5):
        forward(length)
        right(144)
    end_fill()
    

 
#Draws Sand
    
def draw_sand(color):
    '''
    Draws and fills sand for my scene using circles
    
    Args:
        color: desired color
    '''
    pencolor(color)
    penup()
    goto(390,-375)
    setheading(90)
    for i in range(5):
        pendown()
        fillcolor(color)
        begin_fill()
        circle(95,180)
        end_fill()
        setheading(0)
        forward(40)
        setheading(90)



#Create Crab

def crab(color):
    '''
    Draws a crab in the bottom right corner of my picture
    
    Args:
        Color: desired color
    '''
    penup()
    pencolor(color)
    fillcolor(color)
    goto(290,-300)
    setheading(45)
    pendown()
    for i in range(3):
        forward(30)
        backward(30)
        right(45)
    setheading(225)
    for i in range(3):
        forward(30)
        backward(30)
        right(45)
    setheading(0)
    forward(10)
    setheading(90)
    begin_fill()
    circle(10)
    end_fill()
        
  
  
  
#Creates Starfish
def add_stars(numstars, color):
    '''
    Draws random stars in the bottom or my picture, used to make starfish
    
    Args:
        numstars: # of random stars
        color: desired color
    '''
    pencolor(color)
    fillcolor(color)
    for i in range(numstars):
        penup()
        goto(randint(-350,350), randint(-340,-300))
        pendown()
        begin_fill()
        star(15,color)
        end_fill()




 #Triangles with fins
        
def fish_fins(x, y, length):
    '''
    Draws an orange fish with a tail
    
    Args:
        x: x-coordinate
        y: y-coordinate
        length: side length of the fish
    '''
    pencolor("black")
    fillcolor("orange")
    begin_fill()
    triangle(x, y, length)
    end_fill()
    penup()
    goto(x, y-(length/2))
    begin_fill()
    setheading(150)
    for i in range(3):
        pendown()
        forward(length/2)
        left(120)
    end_fill()



#Upisde down triangle
    
def upside_triangle(x, y, length):
    '''
    Draws an upside down equilateral triangle (used for my draw_waves() function)
    
    Args:
        x: x-coordinate
        y: y-coordinate
        length: side length
    '''
    penup()
    goto(x,y)
    setheading(0)
    for i in range(3):
        pendown()
        forward(length)
        right(120)

    
    
#Waves
    
def draw_waves():
    '''
    Draws waves on the top of the picture using upside down triangles
    
    Args: None
    '''
    pencolor("light sky blue")
    penup()
    goto(-370,350)
    setheading(270)
    x=-350
    y=350
    for i in range(10):
        pendown()
        fillcolor("light sky blue")
        begin_fill()
        upside_triangle(x,y,72)
        end_fill()
        x = x+72


 
#Draw everything

def generate_picture():
    '''
    Draws my picture using the functions that I made!
    
    Args: None
    '''
    speed(50)
    bgcolor("turquoise2")
    draw_waves()
    draw_sand("Darkgoldenrod1")
    add_circles(15,"white smoke")
    crab("red3")
    add_stars(8, "deep pink")
    fish_fins(0, -160, 30)
    fish_fins(-220, 215, 36)
    fish_fins(-332, -175, 45)
    fish_fins(-130, 0, 15)
    fish_fins(127, 132, 27)
    fish_fins(228, 246, 42)
    fish_fins(215, -164, 36)
    polygon(-300, -308, 9, 14, "sienna")
    polygon(-150, -320, 8, 20, "sienna")
    polygon(0, -312, 7, 16, "sienna")
    polygon(145, -314, 6, 12, "sienna")
    polygon(200, -340, 5, 22, "sienna")
    polygon(-200, -347, 9, 13, "sienna")
    
