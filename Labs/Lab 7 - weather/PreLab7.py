'''
Pre Lab 7
Wednesday, October 29th
'''

import datetime
   
def get_hour():
    now = datetime.datetime.now()
    return str(now.hour)
   
def get_date():
    now = datetime.datetime.now()
    return str(now.month) + "-" + str(now.day) + "-" + str(now.year)



'''
Notes:
file_exist(...)    entry_exist(...)  

File Esist?   |  Entry Exist?   |    Should Write?          not( file_exist() and entry_exist()  )  --> should I write?
_________________________________________________
 
      F             N/A                 T         
  
      T              T                  F              
  
      T              F                  T






'''



def leading_underscore(strings):
    for string in strings:
        if string.startswith('_'):
            return True
    
    return False
        







