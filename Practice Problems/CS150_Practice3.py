'''
Practice Problems 3
Monday, Sept 23
'''

from random import randint


ALPHABET = 'abcdefghijklmnopqrstuvwxyz '

'''
#Problem 1 - Use string methods

#a
    "boolean".upper()
#b
    "CO2 H2O".find("2")
#c (shows the range in second part)
    temp = "CO2 H2O"
    temp.find("2", temp.find("2") + 1) 
#d
    "Boolean".islower()
#e
    "MoNDaY".lower().upper()
#f
    " Monday".lstrip()
    
'''

#Problem 2 - Which digits

digits = "0123456789"
 
 
#a - digits[:5] = 0,1,2,3,4
      
#b - digits[5:] = 5,6,7,8,9
    
#c - digits[::2] = 0,2,4,6,8
    
#d - digits[1::2] = 1,3,5,7,9
    
#e - digits[-5:-3] =  5,6 (second is exlusive)
    

# Problem 3 -print last half of string

def last_half(string):
    length = len(string)
    return string[(length/2):]

#Problem 4 - Insert noise (insert A between each character of a string)

def insert_noise(string):
    result = ''
    for letter in string:
        result = result + letter + 'a'
    return result


#Problem 5 - insert randomn letter between characters in a string


def insert_noise2(string):
    result = ''
    for letter in string:
        result = result + letter + ALPHABET[randint(0,26)]
    return result
    
    
#Problem 6 -exlude the last random letter, only random between characters in string

def insert_noise3(string):
    result = ''
    for letter in string:
        result = result + letter + ALPHABET[randint(0,26)]
    return result[:-1]


    
    
    
    
    