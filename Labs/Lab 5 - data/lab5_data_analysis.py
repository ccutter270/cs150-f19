"""
CSCI150 Fall 2019 Lab 5

Name: <Caroline Cutter> , <Claudia Vira>
Section: <B>

Creativity:

    - We added "Mode" to the data anaylsis by making a most_frequent function that returns the number that occurs the most in a data set
    - To extend the "Mode" in the data analysis, we also say how many times it occurs in the data set. We did this by making a mode_count
    function that returns the amount of times the mode appears in a data set
    - We added "Range" to the data analysis function
    - We added "Sum" to the data analysis function that adds all the number in the list
"""



# TODO: Include your data analyses here


'''
Grumpier Old Stats

Enter file to analyze: grumpierold_review.txt
The file contained 478 entries
Max: 5
Min: 1
Average: 3.01673640167364
Median: 3.0
Std. dev: 1.071711838975401
Mode: 3 (occurs 191 time(s))
Range: 4
Sum: 1442

Jumanji Stats

Enter file to analyze: jumanji_review.txt
The file contained 701 entries
Max: 5
Min: 1
Average: 3.20114122681883
Median: 3
Std. dev: 0.9831720435251046
Mode: 3 (occurs 266 time(s))
Range: 4
Sum: 2244


Comparison of the movie stats: 

Grumpier Old Men and Jumanji both have very similar average ratings (around 3 stars each). In each of the movie, a little more than
1/3 of the people rated the movies 3 stars. It is interesting how similar both movies are to eachother in terms of statistics of the
ratings.

'''



# 95 Age

'''
Enter file to analyze: 95age.txt
The file contained 35326 entries
Max: 90
Min: 0
Average: 35.73141595425466
Median: 34.0
Std. dev: 22.54500613160551
Mode: 90 (occurs 110 time(s))
Range: 90
Sum: 1262248


It is not shocking that the average age was around 35, because we expect that the baby boomers make up most of the population at this
time. We find it shocking that the mode is 90 because that is far above the average life expectancy at the time. It makes sense that
the standard deviation is so high because it is covering such a wide range of age (90).

'''

# 95 Kids

'''
Enter file to analyze: 95kids.txt
The file contained 35326 entries
Max: 9
Min: 0
Average: 0.43285398856366414
Median: 0.0
Std. dev: 0.8975902261262514
Mode: 0 (occurs 27009 time(s))
Range: 9
Sum: 15291


*Frequency Table*

data    frequency
0   27009
1   3450
2   3302
3   1189
4   275
5   64
6   18
7   13
8   3
9   3

We find it shocking that the average number of kids was around .5, which shows that many family did not have kids at all. Therefore it
makes sense that the mode was 0 and it occured 27009 times in this data set. This shows the shift in the 'ideal' american family because
families were starting to have less and less kids. We printed out the frequency table (shown above) and it is interesting that the amount
of families with 0 kids is 8 times the amount of families with 1 or 2 childern. 

'''

# 95 Income

'''
Enter file to analyze: 95income.txt
The file contained 35326 entries
Max: 304998
Min: -13411
Average: 16974.277925607203
Median: 8929.5
Std. dev: 22838.780363565795
Mode: 224998 (occurs 2 time(s))
Range: 318409
Sum: 599633342

The the thing that stood out to us the most was that the minimum income was -13411 because instead of an income, people were losing money
which could point to issues of debt. Additionally, we recognized a disparity between the median and average income. We believe that
there were outliars that skewed the data, especially the average. 

'''

    
    
# TODO: Implement your data analysis function



# Read Data
def read_data(filename):
    '''
    Opens a data file and creates a list from the data inside the file
    
    Args:
        filename: the file name
        
    Returns:
        A list of the data in the file
    '''
    stats = []
    with open(filename, "r") as file:
        for line in file:
            stats.append(int(line.strip()))
    return stats
   
   
   

#Average Value of a list
def average_value(num_list):
    '''
    Computes the average value from a list of numbers
    
    Args:
        num_list: list of numbers
    
    Returns:
        Average value of num_list
    '''
    sum_data = 0
    for element in num_list:
        sum_data += int(element)
    return sum_data/len(num_list)



#Median Number
def median_num(num_list):
    '''
    Finds the median number in a list. If it is odd, it prints the middle of the sorted list, if it is even it takes the two middle
    values of the sorted list and averages them
    
    Args:
        num_list: list of numbers
        
    Returns:
        Median of num_list
    '''
    num_list.sort()
    if (len(num_list) % 2) == 0:   #Even
        return (num_list[len(num_list)//2] + num_list[(len(num_list)//2) - 1]) / 2
    else: #odd
        return num_list[len(num_list)//2]
        
        
    
#Standard Deviation of a data set
def standard_dev(num_list):
    '''
    Computes the standard deviation of a list of numbers
    
    Args:
        num_list: List of numbers
        
    Returns: Standard deviation of num_list
    '''
    mean_value = average_value(num_list)
    sum_deviation = 0
    for number in num_list:
        sum_deviation += (number - mean_value)**2
    return ((1/(len(num_list)-1)) * sum_deviation)**.5



#Most frequent number

def most_frequent(num_list):
    '''
    Computes the most frequently occuring number (aka the mode) of a list of numbers
    
    Args:
        num_list: list of numbers
    
    Returns:
        The mode of num_list

    '''
    mode = 0
    prev_count = 0
    for element in num_list:
        count = num_list.count(element)
        if count > prev_count:
            mode = element
            
        prev_count = count
    
    return mode
    
def mode_count(num_list):
    '''
    Finds the number of times the most frequent number (aka mode) appears in a list of numbers
    
    Args:
        num_list: a list of numbers
        
    Returns:
        # of appearences of the mode in num_lists
    '''
    mode = most_frequent(num_list)
    return num_list.count(mode)



def data_analysis():
    '''
    Computes different statistical analyses of a file containing data. This function prompts the user for a file name, then takes the
    data from the file, makes it into a list and computes how many entires, the max, the min, the average, the median, the standard
    deviation, the mode, the range and the sum of the data.
    
    Args:
        None
    
    Returns:
        None, just prints
    '''
    file = input("Enter file to analyze: ")
    data_list = read_data(file)
    if len(data_list) == 0:
        print("File contained 0 entries")
    else:
        print("The file contained " + str(len(data_list)) + " entries")
        print("Max: " + str(max(data_list)))
        print("Min: " + str(min(data_list)))
        print("Average: " + str(average_value(data_list)))
        print("Median: " + str(median_num(data_list))) 
        print("Std. dev: " + str(standard_dev(data_list)))
        print("Mode: " + str(most_frequent(data_list)) + " (occurs " + str(mode_count(data_list)) + " time(s))")
        print("Range: " + str((max(data_list)) - min(data_list)))
        print("Sum: " + str(sum(data_list)))



# TODO: Implement your fixed frequencies functions here


def frequencies(data):
    """
    Attempts to print the frequency of each item in the list data
    
    Args:
        data: List of "sortable" data items
    """
    data.sort()
    
    count = 0
    previous = data[0]

    print("data\tfrequency") # '\t' is the TAB character

    for d in data:
        if d == previous:
            # Same as the previous, increment the count for the run
            count += 1
        else:
            # We've found a different item so print out the old and reset the count
            print(str(previous) + "\t" + str(count))
            count = 1
        
        previous = d
    print(str(previous) + "\t" + str(count))
    
    
#startup
    
if __name__ == '__main__':
    data_analysis()







