"""
CSCI150 Fall 2019 Lab 4

Name: <Caroline Cutter>
Section: <B>

Creativity:
    - Prompts for difficulty level (easy, medium, hard)
    - Added more feedback, now the program tells if it is higher or lower
    - Gives the % correct of the user and the average # correct per second
    - If the user doesn't answer 'yes' or 'no' to play the game, it tells them to say the correct thing next time
    - Adds random parenthesis, I could only get the parenthesis to work without the number 10, I tried many different ways but couldnt
      figure it out, so I made a if not in 10 loop that adds arbitrary parenthesis if 10 is not in the equation

THings to do:
    - Fix the parenthesis code, work on 10



"""


#imports
from random import randint
from random import randrange
import time


#constants
OPERANDS = '+-*'
RANGE_NUMBERS_LOWER = 1
RANGE_NUMBERS_UPPER = 10


def random_equation(num_operators):
    '''
        This function generates a random equation with a desired amount of operators
        
        Args:
            num_operators: desired number of operators in the random equation
            
        Returns:
            A random equation

    '''
    #creating random equation
    equation = str(randint(RANGE_NUMBERS_LOWER, RANGE_NUMBERS_UPPER))
    for i in range(num_operators):
        equation += OPERANDS[randint(0,len(OPERANDS)-1)]
        equation += str(randint(RANGE_NUMBERS_LOWER, RANGE_NUMBERS_UPPER))
    
    #adding parenthesis
    if '10' not in equation:
        if num_operators == 0:
            return equation
        else:
            parenthesis = randrange(0, (len(equation)-1), 2)
            parenthesis2 = randrange((parenthesis+3), (len(equation)+1), 3)
            equation2 = equation[:parenthesis] + '(' + equation[parenthesis:parenthesis2] + ')' + equation[parenthesis2:]
            return equation2
    else:
        return equation


     

def query_equation(equation):
    '''
        This function asks the user to answer an equation that is inputted, if it the user answers wrong it gives feedback and asks
        the user to answer again, if the user is correct, it terminates.
        
        Args:
            equation: equation to be solved
    
        Returns:
            total_guesses, which is the total guesses it took for the user to answer the question. This is not integral to the function,
            but it is used in the function 'play_game' to calcualte the % correct.
    '''
    #asking user for answer to the equation
    answer = eval(equation)
    total_guesses = 0
    while True:
        guess = int(input(str(equation) + " = "))
        
        #if guess is correct
        if guess == answer:
            print("Correct!")
            total_guesses += 1
            break
        #if guess is close to answer
        elif ((0 <= (guess - answer) <= 2) or (0<= (answer - guess) <= 2)):
            if answer > guess:
                print("Close, a little higher. Try again.")
                total_guesses += 1
            else:
                print("Close, a little lower. Try again.")
                total_guesses += 1
        #if guess is not close to answer
        else:
            if answer > guess:
                print("The answer is higher, keep trying.")
                total_guesses += 1
            else:
                print("The answer is lower, keep trying.")
                total_guesses += 1
   
    #return total guesses to help calcualate average in play_game  
    return total_guesses        
     
    



def play_game(duration, num_operators):
    '''
        This has the user play a math game with n operators in n seconds. The goal is for the user to answer the math questions as
        quickly as they can before time runs out.
        
        Args:
            duration: length of game
            num_operators: number of operators in the equation
            
        Returns: none, BUT prints out # correct, how much time, average correct per second and % correct
    '''
    
    correct = 0
    start_time = time.time()
    total_guesses = 0
    
   
   #Play play_game until time is up
    while (time.time() - start_time) <  duration:
        num_guesses = query_equation(random_equation(num_operators))
        correct += 1
        total_guesses += num_guesses
        
    #Calculate time passed
    total_time = time.time() - start_time
    
    #Printing results, not returning because puropse is to communicate w/ user
    print("You got " + str(correct) + " correct in " + str(total_time) + " seconds.")
    #creativity
    print("That is an average of " + str(correct/total_time) + " per second. Your percent correct was " + str(round((correct/total_guesses)*100,2)) + "%.")





if __name__ == '__main__':
    '''
        Prompts the user to play 'play_game' when the program is run. Asks if the user wants to play, for how long and how hard the game
        should be

    '''
    
    answer = input("Do you want to play a game [yes/no]? ")
    
    #if they don't want to play game
    if answer == "no":
        print("Thats okay, maybe next time! Goodbye!")
        
    #if they want to play game   
    elif answer == "yes":
        playtime = int(input("How long do you want to play for [seconds]? "))
        
        #Difficulty level
        difficulty = (input("How difficult do you want the game [easy, medium, hard]? "))
        if difficulty == "easy":
            operators = randint(1,2)
        elif difficulty == "medium":
            operators = randint(3,4)
        elif difficulty == "hard":
            operators = randint(5,6)
        
        
        play_game(playtime, operators)

    #if they don't give a valid response   
    else:
        print("I'm sorry, please answer yes or no next time")
      
