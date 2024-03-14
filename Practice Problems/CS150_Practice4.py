'''
Practice Problem 4
Monday, Sept 30th
'''

'''
Notes:

    *For True and False, make sure to capitalize

'''





'''
Problem 1
'''

#a. True and not False       = True
#b. True and not false       = Error - capitalization
#c. True or True and False   = True
#d. not True or Not False    = True
#e. True and not 0           = True  ***** wut
#f. 52 < 52.3                = True
#g. 1 + 52 < 52.3            = False
#h. 4! = 4.0                 = False



'''
Problem 2
'''

#Reurns True if they are the different number, False if they are the same
def different(a, b):
    return a != b




'''
Problem 3

'''

'''
Gives this, doesn't work for the values. I fixed it by switching the if and elif statements

def phcalc(ph):
    if ph < 7.0:
        print(ph, "is acidic.")
    elif ph < 3.0:
        print(ph, "is VERY acidic! Be careful.")

'''

def phcalc(ph):
    if ph < 3.0:
        print(ph, "is VERY acidic! Be careful.")  
    elif ph < 7.0:
        print(ph, "is acidic.")




'''
Problem 4
'''

def firstprimes(num):
    """Prints out the first num primes"""
    count = 0  # the number of primes we've printed out
    current = 1  # the current number we're checking
           
    while current <= num:
        if isprime(current):
            print(current)
            count += 1
           
        current += 1
        
'''
Problem 5
'''

def twentyfor():
    for i in range(21):
        if i%3 == 0:
            print(i)
        
def twentywhile():
    count = 1
    while count <= 20:
        if count%3 == 0:
            print(count)
        count += 1
        
    
'''
Problem 6
'''

def twentyfor2(start, stop):
    for i in range(start, stop+1):
        if i%3 == 0:
            print(i)
        
def twentywhile2(start, stop):
    count = start
    while count < stop:
        if count%3 == 0:
            print(count)
        count += 1
        
        
'''
Problem 7
'''
 
def gc_fraction1(dna):
    string = dna.lower()
    gccount = string.count("g")
    atcount = string.count("a")
    return (gccount/(atcount + gccount))
        
        


def gc_fraction2(dna):
    string = dna.lower()
    gc = 0
    for base in string:
        if base == 'g' or base == 'c':
            gc += 1
    return gc/len(string)
            
    
        
        
        
        
        