"""
CSCI150 Fall 2019 Lab 1

Name: <Caroline Cutter>
Section: <B>


Creativity:

I did all the creativity suggestions in the lab including the extra liters_to_gallons function and the dollars_to_euros that incorperates
the euros_to_dollars function. Then, I also made a new function called nytime_to_madridtime which converts a 24 hour clock time and says
what time it would be on that day in Madrid. If the day is already over in Madrid, it tells the user that it is already the next day.
Note this only works with 24 hour periods.



I also created two different functions and printed them out at the end of section 3. One of them was repeat_three and the other is the
name combiner. Also, I used the type() function and printed some different classes out by experimenting with int, float and strings

Another creativity piece I added in was within my functions in section four. In these I created a varible within the function and stored
the value in that variable. For example in euros_to_dollars, I defined dollars as the conversion then returned dollars. This is useful
because it makes it clearer and easier to read because it is obvious what is being returned.


"""

"""
Section 1
"""

"""
>>>2**5
32
>>> 2+5*7**(1/2)
15.228756555322953
>>> 22/7
3.142857142857143
>>> 22//7
3
>>>type("Hello")
<class 'str'>
>>> type(4.2)
<class 'float'>
>>> 4.8**6
12230.590463999997
>>> pi =22/7
>>> pi*(15**2)
707.1428571428571
"""

"""
Section 2
"""

# Error(s): Missing colon after the def
def square(x):
    return x**2

# Error(s): sid2 --> side2 (mispelled)
def hypotenuse(side1, side2):
    return (side1**2 + side2**2)**(1/2)

print(hypotenuse(3, 4))

# Error(s): Missing indent in the body before return statement
def sqrt(x):
    return x**(1/2)

# Error(s): Missing end parenthesis after num_years
def compound_interest(investment, rate, num_years):
    amount = investment * ((1 + rate) ** num_years)
    return amount

"""
Section 3
"""

# Add your statements here...

    #Random variables
my_name = "Caroline Cutter"
favorite_number = 10
pi = 22/7

    #random definitions I created (although full_name we created in class)
    #Gets first and last name and combines into one full name
def full_name(firstname, lastname):
    return(firstname + " " + lastname)

    #Reapeats the parameter three times
def repeat_three(saying):
    return((saying + ". ")*3)
    
    #random print statements
print(10)
print("This is an interesting lab")
print (type(my_name))
print(type(favorite_number))
print(type(pi))
print(full_name("caroline", "cutter"))
print(repeat_three("Computer Science is fun"))


   
# Add your circle_area function here...

    #Area of Cirlce = pi*r^2, assigns pi inside function just in case it wasn't already assigned
    #This function computes the area of a circle with the parameter "radius"
   

def circle_area(radius):
    pi = 22/7
    return pi*(square(radius))

print(circle_area(25))



# Solve the burger pricing problem here...
hamburger = 1.50
cheeseburger = 1.75
doubledouble = 2.65

    #Price of cheese = cheeseburger - hamburger (takes out bun, veggies and patty, leaves 1 cheese)
cheese = cheeseburger - hamburger
    
    #Price of patty = doubledouble - hamburger - 2 cheeses (takes out bun, veggies, 1 patty and two cheeses, leaves 1 patty)

patty = doubledouble - hamburger - (cheese*2)

# Replace None with expressions computing the price using variables above
    #These compute the price of special menu items by adding the cost of each topping (bun, veggies, patty, cheese) and adding them
    #it is *99 because there is already one patty in a hamburger, it is *100 & *50 on cheese because there is no cheese on a hamburger
    #The hamburger already has the bun and the veggies accounted for
price_100x100 = hamburger + (99* patty) + (100*cheese) 
price_100x50 = hamburger + (99*patty) + (50*cheese)

                           
"""
Section 4
"""

# Add your study abroad functions here...


    #This converts the parameter Euros to dollars! 1 Euro = $1.16

def euros_to_dollars(euros):
    dollars = euros*1.16
    return dollars


    #Dollar to euro coverter that uses the euros_to_dollar() funtion instead of using the exact number
def dollars_to_euros(dollars):
    euros = (dollars/euros_to_dollars(1))
    return euros
   
   
   #hello in Russian!!

def welcome():
    print("Привет")

    #This converts the paremeter kilometers to miles! 1 kilometer = .621371 miles

def kilometers_to_miles(kilometers):
    miles = kilometers*.62137
    return miles

    #This converts the parameter celcius to fahrenheit! fahrenheit = celcius*(9/5) + 32 

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*(9/5)) + 32
    return fahrenheit

     #This converts the paremeter liters to gallons! 1 Liter = .264172 gallons

def liters_to_gallons(liters):
    gallons = liters*.264172
    return gallons
    
    
    #This converts the parameters "kilometers" and "liters" to miles per gallon!
    # **Note I created an extra function, "liters_to_gallons" for this
    # I use the functions I made previously to calculate miles and gallons from kilometers and liters
    # then I divided miles by gallons and set it to the variable "mpg" and then returned mpg
   

def mpg_from_metric(kilometers, liters):
    miles = kilometers_to_miles(kilometers)
    gallons = liters_to_gallons(liters)
    mpg = miles / gallons
    return mpg


    #Extra creativity, time coverter from New York time zone to Madrid, Spain time zone. But it only works with the 24 hour clock.

def nytime_to_madridtime(time):
    time = time + 6
    if time <= 24:
        print("It is", str(time) +  " O'Clock in Spain")
    else:
        print("Uh oh! It is already the next day there")
   
    














