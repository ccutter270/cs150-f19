"""
CS150 Fall 2019 Lab 3

Name: <Caroline Cutter>
Section: <B>

Creativity:
 
 - I created the shift() function that takes the desired number of places you want the alphabet to be shifted and shifts it left that
 number of places with a wrap around. What is cool about the funciton I created is that you can use numbers greater than 26 without an
 error.
 
 - I also created the my_encrypt and my_decrypt. For my_encrypt, it is special / more secure because it requires three specific
 passwords. The my_decrypt decrypts the encryption by using the three specific passwords. It will only be the correct decyrption if the
 passwords are the same used from the encryption.This makes it much more secure, it it is also very easy to change the password and come
 up with many new encryptions that would be very difficult to break.

"""

from random import randint, seed

ALPHABET = "abcdefghijklmnopqrstuvwxyz "

#---------------------------------------------------------
# Fools functions
 
   
def fools_encrypt(string):
    '''
        Takes in a messege and returns the message with each character repeated 3 times
        
        Args:
            string: message that you want to encrypt
        
        Returns: the message with each character repeated three times
    '''
    result = ''
    for i in string:
        result = result + i*3
    return result


def fools_decrypt(string):
    '''
        Decrypts 'fools_encrypt', meaning it takes each of the 3 repeated characters in the encryption and returns the normal message
        Note: this is meant to decrypt, if used with a normal message, it will print every 3rd character out
        
        Args:
            string: message to be decrypted
            
        Returns:
            The decrypted message, every 3rd letter in the string
    '''
    result = ''
    for i in string[::3]:
        result = result + i
    return result


#---------------------------------------------------------
# Caesar's method



# Premade funtion

def shift_letter(letter, num):
    """
    Shifts a letter up num places in the alphabet with
    wraparound.

    Args:
        letter: A single character
        num: Integer distance to shift letter

    Returns:
        Character in ALPHABET num distance from letter
    """
    # Get the index of the current letter
    index = ALPHABET.find(letter)
    # We use the mod operator (%) for wraparound
    return ALPHABET[(index + num) % len(ALPHABET)]



#Caesars Encryption

def caesar_encrypt(message, shift):
    '''
        Takes a message and encrypts it according to caesars cipher with the desired shift key. Caesars ciper shifts the alphabet over
        n number of spaces.
        
        Args:
            message: message to be encrypted
            shift: desired shift for caesars cipher
        Returns:
            Encrypted code based on caesars cipher
    '''
    result = ''
    for letter in message:
        result = result + shift_letter(letter, shift)
    return result

def caesar_decrypt(message, shift):
    result = ''
    for letter in message:
        result = result + shift_letter(letter, -shift)
    return result


    '''
        Question answer from the Lab:

            caesar_decrypt("htruzyjwexhnjshjenxestertwjefgtzyehtruzyjwxeymfsefxywtstrcenxefgtzyeyjqjxhtujx", 5)

            'computer science is no more about computers than astronomy is about telescopes'
    '''



#---------------------------------------------------------
# Substitution cipher


#Splice Function

def splice(message, letter):
    """
    Splices out letter from message and returns the 
    remaining message. letter can only occur ONCE in
    the message
    
    For example:
    >>> splice("abcdefg", "f")
    'abcdeg'

    Args:
        message: String
        letter: A string to be removed from message

    Returns:
        String message with letter removed.
    """
    index = message.find(letter)
    return message[:index] + message[(index+1):]    #index+1 so it splices out the index
    
    
    
      
#keygen

def keygen(password):
    """
    Given a string password, generates a new random key.
    A key consists of a random ordering of the letters in
    ALPHABET.

    Args:
        password: String password used to generate key

    Return:
        Key string
    """
    remaining = ALPHABET
    key = ""
    
    seed(password)
    
    for dummy in range(len(ALPHABET)):
        index = randint(0, len(remaining)-1)
        next_letter = remaining[index]
        key = key + next_letter
        remaining = splice(remaining, next_letter)
    
    return key
    


#Subsitution Encryption

def subst_encrypt(message, key):
    '''
        Encrypts a message based on a substitution key provided
        
        Args:
            message: message to be encrypted
            key: a key to substite characters with ALPHABET
            
        Returns:
            An encrypted message based on the substitution key
    '''
    encryption = ''
    for char in message:
        index = ALPHABET.find(char)
        encryption += key[index]
    return encryption
    



def subst_decrypt(message, key):
    '''
        Decrypts a message based on the subsitution key provided
        
        Args:
            message: message to be decrypted
            key: a key to subsitute characters with ALPHABET
            
        Returns:
            A decrypted message based on the substitution key
    '''
    decryption = ''
    for char in message:
        index = key.find(char)
        decryption += ALPHABET[index]
    return decryption


    '''
        Question from Lab:
            
            'ao us jauaoiwpuxsrtauxusrrf xwuiju g wuiduqrtuxh uyhrwpuqrtuxh urwfqurddusquxusia'
            
                is

            'the best thing about a boolean is even if you are wrong you are only off by a bit'

    '''



'''
CREATIVITY POINTS
'''

#Shift Function
def shift(number):
    '''
        Shifts the letters in the alphabet desired number of places to the left with a wrap aroud
        
        Args:
            number: desired number of places each letter is shifted
        
        Returns:
            A string of the new shifted alphbet based on number of shifts entered.
    '''
    if number > 26:
        number -= 26
    shifted = ''
    for i in range(number,len(ALPHABET)):
        shifted += ALPHABET[i]
    for i in range(0, number):
        shifted += ALPHABET[i]
    return shifted
        


#My Encrypt
    #Encryption --> alphabet index to key1 letter to key2 index to key3 letter

def my_encrypt(message, password, password2, password3):
    '''
        This program takes a message and three passwords and then encrypts a message based on the password. All three passwords must
        be correct in order for it to work, so it is much more secure than any of the other ciphers
        
        Args:
            message: message to be encyrypted
            password: password for encryption key
            password2: password for encryption key
            password3: password for encryption key
        
        Returns:
            An encrypted message based off the three passwords entered
    '''
    key1 = keygen(password)
    key2 = keygen(password2)
    key3 = keygen(password3)
    encryption = ''
    for char in message:
        index = ALPHABET.find(char)
        letter = key1[index]
        index2 = key2.find(letter)
        encryption += key3[index2]
    return encryption
        

#My Decrypt
    #Decryption --> key3 letter to key2 index to key1 letter to alphabet index to aplhbaet letter

def my_decrypt(message, password, password2, password3):
    '''
        This program is the decryption key for my_encryption. It takes an encyrpted message and decrypts is using keys from three
        specific passwords
        
        Args:
            message: message to be decyrypted
            password: password for decryption key
            password2: password for decryption key
            password3: password for decryption key
       
       Returns:
            The decrypted message based on my_encryption
    '''
    key1 = keygen(password)
    key2 = keygen(password2)
    key3 = keygen(password3)
    decryption = ''
    for char in message:
        index = key3.find(char)
        letter = key2[index]
        index2 = key1.find(letter)
        decryption += ALPHABET[index2]
    return decryption
        
        
    
    
    
    
   




