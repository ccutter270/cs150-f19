'''
Practice Problems 6
Monday, October 21st
'''

#1. Append 5 to a list, one way changing the list, one way not changing the list


    #changes list
list_one = [1, 2, 3, 4]
list_one.append(5)

    #does not change list
list_two = [1, 2, 3, 4]
list_two2 = list_two + [5]



#2. What would be prodcued by...

values = [0, 1, 2]
values[1] = values

    # values = [0, [0, 1, 2], 2]
    
#3. What is the value of 'a' in this code?
    
def mystery(a_list):
    a_list.sort()
    return a_list[0]
    
a = [3, 7, 2, 9, 1]
print("Result:", mystery(a))    
    
    # a = [3, 7, 2, 9, 1] but the result is "Result: 1" WRONG - a list is sorted
    # a = [1, 2, 3, 7, 9]
    
    
    
#4. What is the value of 'a' in this code?
    
def mystery(a_list):
    a_list = sorted(a_list)
    return a_list[0]
    
a = [3, 7, 2, 9, 1]
print("Result:", mystery(a))
 
 
     # a = [3, 7, 2, 9, 1] but the result = "Result: 1"
    
    
    
#5. What is the value of 'a' in this code?
     
def mystery(a_list):
    a_list = a_list[::]
    a_list.sort()
    a_list[1].append(2)
    return a_list[0][0]
    
a = [[3], [7], [2], [9], [1]]
print("Result:", mystery(a))
    
    # a =  [[3], [7], [2,2], [9], [1]]   ** Because it doesnt permenantly sort it, but it appends to the second slot
    
    
#6. What would this code produce?
    
a = [1, 2, [3, 4], 5]
b = a[:]
a[2].append(4)

    # a = [1, 2, [3, 4, 4], 5] and b = [1, 2, [3, 4], 5] *** Wrong, b is the same as a because they point to the same objects
    

#7. What is the results of the expressions
    
#a. {2, 3, 5, 7} | {5, 6, 7, 8}  = {2, 3, 4, 6, 7, 8}
#b. {2, 3, 5, 7} & {5, 6, 7, 8}  = {5, 7}
#c. {2, 3, 5, 7} - {5, 6, 7, 8}  = {2, 3,}
#d. {2, 3, 5, 7} ^ {5, 6, 7, 8}  = {2, 3, 6, 8}
#e. {2, 3} <= {3, 4}             = False
#f. {2, 3} >= {3}                = True
    

#8.Create function that returns a set of integers that occur more than once in a list
    
def find_dups(random_list):
    dups = set()
    for element in random_list:
        if random_list.count(element) > 1:
            dups.add(element)
    return dups


#These are dictionaries

#9. What is the value of e after this?

d = { 1: 2, 3: 4 }
d[2] = 1
d[2] = 2

#d = {1:2, 3:4, 2:2}

e = {}
for x in d:
    e[2*x] = d[x]
 
    # {2:2, 6:4, 4:2}


#10. make count_values that counts how many distinct value there are
    
def count_values(dictionary):
    previous = []
    count = 0
    for key in dictionary.values():
        if key not in previous:
            count += 1
            previous.append(key)
    return count
        
    # or


def count_values2(dictionary):
    return len(set(dictionary.values()))
            


#11.
    
def smallest_prob(dictionary):
    smallest = ''
    smallest_prob = 1
    for element in dictionary:
        prob = dictionary[element]
        if prob <= float(smallest_prob):
            smallest = element
            smallest_prob = prob
    return smallest
        
    
    
    
    
#12. make a function that tells if all keys are integers or not
    
def all_ints(dictionary):
    for key in dictionary:
        if type(key) != int:
            return False
    return True
            
        
        
        
        
        
        
        