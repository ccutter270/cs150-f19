'''
PreLab 4
Wednesday, Oct 2nd
'''

import time

#prints seconds since start time
print(time.time())


#Returns days since start date
def days_since():
    t = time.time()
    mins = t/60
    hours = mins/60
    days = hours/24
    return(days)

#Time it takes for the user to type there name
def time_elapsed():
    time1 = time.time()
    input("Type your name here: ")
    time2 = time.time()
    return str(time2 - time1) + " seconds elapsed."

