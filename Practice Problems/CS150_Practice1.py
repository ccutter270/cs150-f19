'''
Practice Problems 1
Monday, Sept 9th

'''




#Problem 2

x= 3
y=12.5
print ("the rabit is", str(x), ".")
print ("the rabit is", str(x), "years old.")
print (str(y), "is the average.")
print (str(y), "*", str(x))
print (str(y), "*", str(x), "is", str(y*x) + ".")




#Problem 3 - fixed errors

a = 3
b = 4
# Take the sqrt of a number
def my_sqrt(x):
    return x ** (1/2)
   
# Calculate the length of the hypotenuse of a right triangle
def hypotenuse_length(a, b):
    sum = a**2 + b**2
    return my_sqrt(sum)
   
print("If a is", str(a), "and b is", str(b), "then hypotenuse is", str(hypotenuse_length(3,4)))


#Problem 4

    #Finds X-intercept using slope and Y-Intercept

def x_intercept(slope, intercept):
    return -intercept / slope

print (x_intercept(1,4))

