'''
Midterm Practice Exam 1
'''

def swap_every_pair(string):
    new_word = ''
    for letter in range(0, len(string)-1, 2):
        new_word += string[letter+1] + string[letter]
    
    if len(string)%2 == 0:
        return new_word
    else:
        return (new_word + str(string[-1]))


print(swap_every_pair("abcdefg"))


    
from random import randint

def equalizer(file1, file2):
    file1 = []
    file2 = []
    with open(file1, "r") as file:
        for line in file:
            file1.append(line)
    with open(file2, "r") as file:
        for line in file:
            file2.append(line)
    
    number_switch = len(file1) - len(file2)
    if len(file1) == len(file2):
        print("No switch required:")
    elif number_switch > 0:
        for i in range(number_switch):
            print(str(file1.pop(randint(len(file1)))) + " swith to section 2")
    else:                 
        for i in range(-number_switch):
            print(str(file2.pop(randint(len(file2)))) + " swith to section 1")
        
        