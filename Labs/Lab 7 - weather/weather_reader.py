'''
This module takes in a zipcode as a command line argument and gives the current temperature at the zipcode specified

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

import urllib.request
import sys



#Constants

SEARCH_STRING = '"temp":'
WEBSITE = 'http://api.openweathermap.org/data/2.5/weather?zip={},us&APPID=9838b264525602b46f0b2ef8c191eef8&units=imperial'




def valid_zip(zipcode):
    '''
    Determines if a zipcode is valid (aka has 5 characters)
    
    Args:
        zipcode: a zipcode
        
    Returns: True if zipcode is a valid zipcode and False otherwise
    '''
    return(len(zipcode) == 5)




def get_temperature(zipcode):
    '''
    Gets a temperature as a float from the Open Weather Map website for a specific zipcode
    
    Args:
        zipcode: a zipcode
        
    Retruns:
        Current temperature at the specified zipcode

    '''
    webpage = WEBSITE.format(zipcode)
    if not(valid_zip(zipcode)):
        print("Please enter a valid zipcode")
        
    else: 
        with urllib.request.urlopen(webpage) as webpage:
            for line in webpage:
                line = line.decode('utf-8', 'ignore')  # Obtain a string from the raw bytes
                begin_index = line.find(SEARCH_STRING)
                begin_index += len(SEARCH_STRING)
                end_index = line.find('"', begin_index)
                temperature = line[begin_index:end_index-1]
    
        return float(temperature)




if __name__ == '__main__':
    #sys.argv[1] = zipcode
    if len(sys.argv) != 2:
        print('usage: python3 weather_reader.py <zip_code>')
    else:
        print(get_temperature(sys.argv[1]))


 
    
    
    
    
    
    
    
    
    
    
    
