CHARS = "abcdefghijklmnopqrstuvwxyz0123456789_!@#$%^&*"

#imports

from random import randint


def password_gen(length):
    '''
        Generates a random password
        
        Args:
            length: number of characters in the password
        
        Return:
            Password as a string
    '''
    result = ""
    for i in range(length):
        result = result + CHARS[randint(0,len(CHARS)-1)]
    return result

