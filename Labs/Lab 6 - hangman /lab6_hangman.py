"""
CSCI150 Fall 2019 Lab 6

Name: Caroline Cutter
Section: <B>

Creativity:
    - I added the picture for the number of guesses. I set the first picture as the losing picture so if the user loses then the
    'dead' hangman will display. If the number of wrong guesses is greater than the number of figures, then the complete (but not 'dead')
    hangman is displayed.
    - I also added an error checker on the guess input, so if it is not a lowercase single letter in the alphabet, then it will
    keep reprompting the user until it is a valid input
"""

#Imports
from random import choice


#Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'       

FIGURES = [
r"""
|-----|
|     X
|    \|/
|     |
|    / \
""",
r"""
|-----|
|     
|    
|     
|     
""",
r"""
|-----|
|     O
|    
|     
|    
""",
r"""
|-----|
|     O
|     |
|     
|     
""",
r"""
|-----|
|     O
|    \|
|     
|     
""",

r"""
|-----|
|     O
|    \|/
|     
|     
""",
r"""
|-----|
|     O
|    \|/
|     |
|     
""",
r"""
|-----|
|     O
|    \|/
|     |
|    /
""",
r"""
|-----|
|     O
|    \|/
|     |
|    / \
"""
]


#Funtions

def read_words(filename):
    '''
    Reads a file and creates a list of words from that files
    
    Args:
        filename: file to be read
    
    Returns:
        list of words from parameter filename
    '''
    words = []
    with open(filename, "r") as file:
        for word in file:
            words.append(word.strip())
    return words      



def set_to_string(set1):
    '''
    Takes letters from a set and creates a string with each letter capitalized and seperated by spaces
    
    Args:
        set1: set of ketters to be transformed into string
    
    Returns:
        Letters in parameter set1 as a string of letters capitilized and seperated by spaces
    '''
    string = ''
    for letter in set1:
        string += str(letter) + ' '
    
    return string.upper()



def insert_letter(guess_letter, working_word, actual_word):
    '''
    Takes a working word of underscores and compares an inputted letter to an actual word and replaces underscores of the working word
    with the letter in the correct index if the letter it is in actual the actual word
    
    Args:
        guess_letter: a letter
        working_word: word with underscores in place of letters
        actual_word: actual word that the working_word is going off of
        
    Returns:
        a new working_word with the guess_letter in place of the underscores based off of actual_word 
    '''
    new_word = ''
    index = 0
    for letter in working_word:
        if guess_letter == actual_word[index]:
            new_word += guess_letter
        else:
            new_word += letter
        index += 1
    return new_word
            
 


def starting_format(letters_guessed, guesses_left, working_word):
    '''
    Makes the starting format for hangman by printing out guessed letters, incorrect guesses left and the working word
    
    Args:
        letters_guessed: letters guessed
        guesses_left: the number of guesses left
        working_word: current word being worked on
    '''
    print('-----------------')
    print('Guessed letters: ' +  set_to_string(letters_guessed))
    print('Incorrect guesses left: ' + str(guesses_left))
    print('Word: ' + working_word + '\n')
    
 
 
 
 
def play_hangman(filename, guesses):
    '''
    An interactive program that plays hangman with the user by generating a random word and prompting the user to guess the letters
    
    Args:
        filename: file that consist of words
        guesses: desired number of wrong guesses
    '''
    #Local variables
    actual_word = choice(read_words(filename))
    working_word = '_' * len(actual_word)
    wrong_guesses = 0
    guesses_left = '*' * guesses
    letters_guessed = set()
    
    #Play game until game is won or guesses have been used
    while wrong_guesses < guesses and working_word != actual_word:
        #Print out the Hangman
        if wrong_guesses+1 == 9: #so the variable FIGURE can work every time
            print(FIGURES[-1])
        else:
            print(FIGURES[wrong_guesses+1])
        starting_format(letters_guessed, guesses_left, working_word)

        letter = input('Guess a letter: ').lower()
        
        #While the inputs are not valid
        while (letter not in ALPHABET) or (len(letter)>1) or (letter == '') or (letter in letters_guessed):
            if letter in letters_guessed:
                print('Letter already guessed!')
            else:
                print('Not a valid input, please type a single letter.')
            letter = input('Guess a letter: ').lower()
       
        #When the input is valid
        if letter in actual_word:
            working_word = insert_letter(letter, working_word, actual_word)
        elif letter not in actual_word:
            wrong_guesses += 1
            guesses_left = guesses_left[:-1]   
        letters_guessed.add(letter)
    
    #Once the game ends
    if wrong_guesses == guesses:
        print(FIGURES[0])
        print('\nThe word was: ' + actual_word + '\nBetter luck next time!')
    elif working_word == actual_word:
        print('\nYou win! \nThe word was: ' + actual_word + '\nYou guessed it with ' + str(wrong_guesses) + ' incorrect guesses')
        



if __name__ == '__main__':
    play_hangman('cs_words.txt', 7)
    