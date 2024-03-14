"""
This module contains the game "Memory" and the functions that are used to implement this game.
The user can play this game when the program is run. 

CSCI150 Fall 2019 Test Project 2

Name: Caroline Cutter
Section: <B>

"""

#Imports
from random import shuffle
from time import sleep, time




#Constants
LETTERS = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J', 'K', 'K', 'L', 'L', 'M', 'M', 'N', 'N', 'O', 'O', 'P', 'P', 'Q', 'Q', 'R', 'R', 'S', 'S', 'T', 'T', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'X', 'Y', 'Y', 'Z']
ROWS = 10
COLUMNS = 10




def secret_dictionary(letter_list):
    '''
    Takes a list of letters and creates a shuffled dictionary with keys being integers in assending order
    (starting from one) and the values being the letters
    
    Args:
        letter_list: a list of letters
    
    Returns:
        a dictioary of integers: letters, with the letters being in shuffled order
    '''
    shuffle(letter_list)
    secret_dict = {}
    i = 1
    for letter in letter_list:
        secret_dict[i] = letter
        i +=1
    return secret_dict






def working_dictionary(length):
    '''
    Creates a dictionary of integers of assending order with their values being that integer in string form
    
    Args:
        length: length of desired dictionary
    
    Returns:
        A dictionary with length of 'length' of integers with string values 
    '''
    working_dict = {}
    for i in range(length):
        working_dict[i+1] = str(i+1)
    return working_dict






def get_input():
    '''
    Prompts the user for an input (two numbers seperated by spaces) and turns it into a tuple of
    the two guesses in integer form
    
    Args:
        None
    
    Returns:
        a tuple of the guesses from the user
    '''
    answers = input('Guess two squares: ').split()
    
    return (int(answers[1]), int(answers[0]))
    





def display_board(dict1):
    '''
    Prints the Memory game board by taking a dictioary and printing out its values as a
    board with desired number of columns (columns constant - can change global)
    
    Args:
        dict1: a dictionary (for this program, the working_dict)
    '''
    for k, v in dict1.items():
        if int(k) % COLUMNS == 0:
            print(v.ljust(3, ' '), end='')
            print('\n')
        else:
            print(v.ljust(3, ' '), end='')
        





def already_correct(dict1, dict2, guess):
    '''
    Determines if the guess was already guessed correctly (used in valid_number)
    
    Args:
        dict1: a dictionary
        dict2: a dictionary
        guess: the users guess
        
    Returns:
        True if guess already guessed correctly, False if not already guessed correctly
    '''
    return dict1[guess] == dict2[guess]





def guessed_correct(guess1, guess2, dict1):
    '''
    Determines if the guess is correct
    
    Args:
        dict1: a dictionary
        guess1: the users guessed number
        guess1: the users other guessed number
        
    Returns:
        True if the guess was correct, False otherwise
    '''
    return dict1[guess1] == dict1[guess2]






def valid_number(answers, dict1, dict2):
    '''
    Determines wether the inputs that the user entered are valid for playing the game
    
    Args:
        answers: a tuple of answers (in integer form)
        dict1: a dictionary (in this game, the working dictionary)
        dict2: a dictionary (in this game, the secret dictionary)
    
    Returns:
        Returns False if the answers are not valid (i.e. they are the same number, they were already guessed,
        or they are out of range) and returns True if the are otherwise valid
    '''
    num1 = answers[0]
    num2 = answers[1]

    #If both guesses are the same number
    if num1 == num2:
        return False
    
    #If either number is not on the board
    if (num1 not in dict1) or (num2 not in dict1):
        return False

    #If either number was already guessed
    if already_correct(dict1, dict2, num1) or already_correct(dict1, dict2, num2):
        return False
    
    return True






def game_won(dict1, dict2):
    '''
    Determines if the game was won by seeing if both the dictionaries are the same
    
    Args:
        dict1: a dictionary
        dict2: a dictionary
    
    Returns:
        True if dict1 and dict2 are the same (aka game won) and False otherwise
    '''
    return dict1 == dict2   
    




def play_game():
    '''
    This is a game of Memory. This program will prompt you for two letters and the goal is to try
    to match all the letters up as fast and with as few guesses as possible.
    '''
    #Starting Variables
    guesses = 0
    start_time = time()
    num_tiles = ROWS * COLUMNS
    
    #Board Dictionaries
    working_dict = working_dictionary(num_tiles) 
    secret_dict = secret_dictionary(LETTERS[0:num_tiles])
    
    
    #Playing game - while game hasn't been run
    while not(game_won(working_dict, secret_dict)):
        #print out lines, display the board, get guesses
        print("\n"*100)
        display_board(working_dict)
    
        answers = get_input()
    
       #While guesses are not valid
        while not(valid_number(answers, working_dict, secret_dict)):
            print("Invalid number(s).")
            answers = get_input()
        

        #When the guess is valid
        
        guess1 = answers[0]
        guess2 = answers[1]
        
        #When guess is valid - "flip over"
        working_dict[guess1] = secret_dict[guess1]
        working_dict[guess2] = secret_dict[guess2]
   
        
        #If its not correct, display board for 2 seconds then "flip back" (doesn't "flip back" if correct) 
        if not(guessed_correct(guess1, guess2, secret_dict)):
            display_board(working_dict)
            sleep(2)        
            working_dict[guess1] = str(guess1)
            working_dict[guess2] = str(guess2)

        #Keep track of guesses
        guesses += 1

    
    #When game is won
    time_taken = time() - start_time
    print('It took you', str(guesses), "guesses and", str(round(time_taken)), 'seconds.')
        




if __name__ == '__main__':
    play_game()
    
 
   
   

    
    
    

    
        
    


 
 
 
   
   
   
   
   






































