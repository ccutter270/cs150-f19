'''
Practice Problems 5
Monday, Oct 7th
'''
'''
Problem 1 - list methods
'''
ids = [4353, 2314, 2956, 3382, 9362, 3900]

#a. Remove 3382 from the list

ids.remove(3382)

#b. Get the index of 9362

x = ids.index(9362)


#c. Insert 4499 in the list after 9362.

ids.insert(ids.index(9362)+1, 4499)

#d. Extend the list by adding [5566, 1830] to it.
ids.extend([5566,1830])



#e. Reverse the list.
 
ids.reverse()

#f. Sort the list.

ids.sort()



'''
Problem 2: Write docstrings for these functions
'''


#1. Mystery Function 1

def mystery1(num1, num2):
    '''
    Makes a list of num2, num 1 amount of times

    Args:
        num1: Length of list
        num2: Value of elements in the lsit
    
    Return:
        a list of num2, num1 amount of times
    
    '''
    result = []
    for i in range(num1):
        result.append(num2)
    return result


#. Mystery Function 2

def mystery2(num1, num2):
    '''
    Makes a list of num2, num 1 amount of times

    Args:
        num1: Length of list
        num2: Value of elements in the lsit
    
    Return:
        a list of num2, num1 amount of times
    
    '''
    return [num2]*num1



#3. Mystery Function 3

def mystery3(a_list):
    '''
    Reverses the list

    Args:
        a_list: a list of choice
    
    Return:
        List in reverse

    '''
    for i in range(len(a_list) // 2):
        other_index = len(a_list)-i-1
        temp = a_list[i]
        a_list[i] = a_list[other_index]
        a_list[other_index] = temp
        return a_list
        

'''
Problem 3 - make a function that tells if the first and last elements of a list are equal 

'''


def same_first_last(list1):
    return list1[0] == list1[-1]
    


'''
Problem 4 - whats the error? (fixed below)

Error = dont need "sorted_colors" because the list 'colors' sorts itself. In this case sorted_colors isnt defined.

colors = 'red orange yellow green blue purple'.split()
sorted_colors = colors.sort()
for color in sorted_colors:
    print(color)
'''


colors = 'red orange yellow green blue purple'.split()
colors.sort()
for color in colors:
    print(color)
    
    
'''
Problem 5- create a function that takes two files and returns number of students enrolled in both classes

'''

def common_students(class1, class2):
    in_both = 0
    for student in class1:
        if student in class2:
            in_both += 1
    
    return in_both
        




#His function to read names off the file
 def read_names(filename):
     with open(filename, "r") as file:
         names = []
         for name in file:
             # Assume one name per line 
             names.append(name.strip())
         return names
   





