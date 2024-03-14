'''
CSCI150 Fall 2019 Pre-Lab 6

Name: Caroline Cutter
Section: <B>

'''

def iterable_to_string(iterable):
    '''
    Takes an iterable object and turns it into a string seperated by spaces
    
    Args:
        iterable: an iterable object
        
    Returns:
        Each item in iterable concatenated into a string seperated by spaces

    '''
    string = ''
    for element in iterable:
        string += str(element) + ' '
    return string




#In Class Notes

existing_usernames = {'mlinderman'}





username = input('Enter a username: ')
while username in existing_usernames:
    print('Username is taken')
    username = input('Enter a username: ')
    
existing_usernames.add(username)

def has_won(working_word, secret_word):
    return working_word == secret_word
    








