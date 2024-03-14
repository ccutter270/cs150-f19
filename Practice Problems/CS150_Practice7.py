'''
Practice Problems 7
Wednesday, October 30th
'''

#1. What would this code produce if...

if __name__ == "__main__":
    print("This is a test, it is only a test.")
else:
    print("This is a test of: " + __name__)

    #a. Ran the program, e.g. via the “green arrow” in Thonny
        # Would print out "This is a test, it is only a test"
    
    #b. Typed “import test” into the console
        # Would print out ("This is a test of: test")
        

#2. For this message, what will be the length of sys.argv
    
    #Message = usage: python3 time_shift.py <input file> <output file> <hours>
        #Len = 4
        
        
#3. Make a portion of a program that doesn't have the correct arguments prints out the usage; then prints out arguments if enough
        
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("usage: python3 print_files.py <file1> <file2> ...")
    else:
        for f in sys.argv[1:]:
            print(f)


#4. Use optional arguments to shorten print statement
 
key = 5
value = 6
 
print(str(key) + "," + str(value))
print(str(key), str(value), sep=',')


#5. What will be printed?

import sys
 print(sys.argv[0], sys.argv[int(sys.argv[1])])

    #a. python3 test.py 0 a b c
        # 'test.py test.py'
    #b. python3 test.py 2 a b c
        # 'test.py a'
    #c. python3 test.py 1 a b c
        # 'test.py 1'



#6. This is the docstring for 'get'; make a function that workds the same

'''
#get(...)
 #    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

'''

def my_get(dictionary, key, value=None):
     if key in dictionary:
         return dictionary[key]
     else:
         return value

#7. Make a program that takes two command lines, if there is no second, then it should default to 12



if __name__ == "__main__":
     # Print the first command line argument
     print(sys.argv[1])
     # Use the second command line parameter or the default value
     if len(sys.argv) == 3:
         value = sys.argv[2]
     else:
         value = 12
     print(value)








