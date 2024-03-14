'''
Practice Problems 2
Monday, Sept 16th

'''


import random


#Problem 1: Find whats wrong with these

'''
#a
sum = 0
for i in range(n):
    sum = sum + i
   
   #This one calculates the sum, but it is one lower than the actual sum because it starts at 0, not 1


#b
sum = 0
for i in range(n):
    temp = sum + (i+1)
    sum = temp
 
    #This one is not actually adding the sum because the sum stays zero. It does not add anything uo
     
#c
sum = 0
for i in range(n):
    sum = (i+1)
  
    #This one is not adding the sum with the next value, so it just adds i + 1 and keeps doing that over and over again
 
#b 
sum = 0
for i in range(n):
    temp = (i+1)
    sum = temp
    
    #This is the same problem as b because it doesnt add to the sum so the sum ends up being the last i + 1
'''

#Problem 2: Writing a factorial definition
     
def factorial(n):
    total = 1
    for i in range(n):
        total = total * (i+1)
    return total

    #i + 1 is because it starts at zero, not 1
    

#Problem 3: Writing a docstring for the function

def mystery():
    '''
        This prints out the first 5 even numbers

        Args: None
       
        Return: None

    '''
    for i in range(5):
        print(2 + 2*i)


#Problem 4: Random Time function

def rand_time():
    return str(str(random.randint(1,12))) + ":" + str(random.randint(0,5)) + str(random.randint(0,9))
    
  
#Way to do it with double letters  
  
def rand_time2():
    hours = randint(1, 12)
    return str(hours // 10) + str(hours % 10) + ":" + str(randint(0, 5)) + str(randint(0, 9))
    
    
    
    
    