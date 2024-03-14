'''
Practice Problems 8
Wednesday, November 16th

'''

import numpy as np
import datascience as ds
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#1. Re-Write this function in plain code

def mystery(a):
    return np.max(a) - np.min(a)

def mystery2(a):
    return max(a) - min(a)
        

#2. Re_Write this function in plain code

def mystery3(a, b):
     return np.sum((np.array(a)-np.mean(a)) * (np.array(b)-np.mean(b)))
    
    
def mystery4(a,b):
    total = 0
    a_mean = sum(a) / len(a)
    b_mean = sum(b) / len(b)
    for i in range(len(a)):
        total += (a[i] - a_mean) * (b[i] - b_mean)
    return total
    




    
#3. Re-Write this in numpy so it doesnt have explicit loops  

def length_normalize(items):
    """
         Normalize all the values in the list by the sum
         
         Args:
             item: A list of numbers
        
         Returns: List of normalized numbers
    """
    total = 0
    for item in items:
        total += item
        
    new_items = []
    for item in items:
        new_items.append(item / total)
    return new_items

def length_normalize2(items):
    return np.array(items) / np.sum(items)


#4. What is plotted by the following code

tips = ds.Table().read_table("tips.csv")


'''
Plots a graph with the x-axis as the total bill and the y-axis as the tip

Females at Lunch == red O's
Males at Lunch == blue O's
Females at Dinner == red X's
Males at Dinner == blue X's

'''
d = tips.where((tips["sex"] == "Female") & (tips["time"] == "Lunch"))
plt.plot(d["total_bill"], d["tip"], "ro") 

d = tips.where((tips["sex"] == "Male") & (tips["time"] == "Lunch"))
plt.plot(d["total_bill"], d["tip"], "bo")


d = tips.where((tips["sex"] == "Female") & (tips["time"] == "Dinner"))
plt.plot(d["total_bill"], d["tip"], "rx")

d = tips.where((tips["sex"] == "Male") & (tips["time"] == "Dinner"))
plt.plot(d["total_bill"], d["tip"], "bx")


plt.show()

#5. Write code that only has lines with tip above 15% of total bill

d = tips.where((tips["tip"] / tips["total_bill"]) > .15)

  
#6. Use group to compute average tip % for all gender and meal times
 
tips["%"] = (tips["tip"] / tips["total_bill"])

tips.group(["sex", "time"], np.mean)

 
 
#7. Bonus - do the same but with python functions

groups = {}
for row in tips.rows:
    # Create tuple with combination of sex and time to use as dictionary key
    combo = (row.sex, row.time)
    # Append to tip pct. to list to compute average later
    groups[combo] = groups.get(combo, []) + [row.tip / row.total_bill]
    
for key, value in groups.items():
    print(key[0], key[1], sum(value) / len(value))
 
 
 
 
