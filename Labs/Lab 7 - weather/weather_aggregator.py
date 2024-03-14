'''
This module takes in two command line arguments, a filename and a zipcode and creates / adds lines to the file specified the current
date, time and temperature at the specified zipcode.

CSCI150 Fall 2019 Lab 7

Name: Caroline Cutter
Section: <B>

Creativity:
    - I added a valid_zip() function that checks if the zipcode is valid in the get_temperature function, so in weather_aggreator it
      checks to make sure the zip is valid, and if it is not is says, "please enter a valid zipcode"
    - I also added the zipcode to the end of the lines in the aggregated file AND check to see if the date, time and zipcode exists in
      a file or not. So, my program will enter the temperature from the same date and time only if it is at a different zipcode
'''


#Imports

from weather_reader import get_temperature
import sys
import os.path
import datetime




def get_hour():
    '''
    Gives current hour in 24 hour time
    
    Args: None
    
    Returns:
        Current hour in 24 hour time
    '''
    now = datetime.datetime.now()
    return str(now.hour)



def get_date():
    '''
        Gives current date
    
        Args: None
    
        Returns:
           Returns current date in 'MM-DD-YYY' format 
    '''
    now = datetime.datetime.now()
    return str(now.month) + "-" + str(now.day) + "-" + str(now.year)




def write_lines_to_file(temp, filename, zipcode):
    '''
        Adds lines to a file with given inputs (works wether the file exists or not)
        
        Args:
            temp: a temperature
            filename: the name of the file to write to
            zipcode: a zipcode
    '''
    with open(filename, "a") as file:
        file.write(get_date() + ',' + get_hour() + ',' + str(temp) + ', Zip: ' + zipcode + '\n')
    



def file_exist(filename):
    '''
        Checks wether a file exists or not
    
        Args:
            filename: a file name
    
        Returns:
            returns True if the file exists, False otherwise
    '''
    return os.path.exists(filename)
    




def entry_exist(filename, zipcode):
    '''
        Checks wether a specific entry from the current hour and zipcode exists within the file
        
        Args:
            filename: the file name
            zipcode: a zipcode
        
        Returns:
            True if the temperature from the current hour and zipcode exists and False otherwise
    '''
    entry = get_date() + ',' + get_hour() + ','
    with open(filename, "r") as file:
        for line in file:
            if entry in str(line) and zipcode in str(line):
                return True
    return False



        
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: python3 weather_aggregator.py <file> <zip_code>')
    else:
        file = sys.argv[1]
        zipcode = sys.argv[2]
        temp = get_temperature(zipcode) 
        
        if not(file_exist(file) and entry_exist(file, zipcode)):
            write_lines_to_file(temp, file, zipcode)
            
            
    
        
        