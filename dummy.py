# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 21:43:41 2021

@author: Gowtham S
"""

print("Hello World")

#15 - 2 = 13 (Not Approved)
'''
dummy.py

extension of image file? - VERY VVV


Priorities of this workshop

1. Live Sessions

2. Assignments given by me

3. Assignments given in MyCaptain App

Suggestion - 1 to 2 hrs per day 


For beginner - Anaconda
For non beginners - Anything

Review of Assigments - 11th of this month
Timing - Between 11 pm and 1 am


Just Chill !!
Go through MyCaptain App 
'''

# Comments

# This is a comment

"""
This is
a multiple
line comment
"""


# Variables
# A_Z, a_z, 0_9, _
x = 2

y = 3.5

name = "gowtham"

Name = "gtm" # Case sensitive

x = "gowtham"

thisguy = "gowtham"

my_name = "gowtham" # Snake Case
myName = "gowtham" # Camel Case
MyName = "gtm" # Pascal Case

# Not do
2var = 3
var name = 3
var-name = 3

# Type Casting

x = 2

y = decimal form of x - 2.0
change the data type from int to float
Type Casting

y = float(x)

y = 3.6

x = int(y)

name = 'gtm'
x = int(name)

name = '1'
x = int(name)



# Print

print("Hello World")

x = 10

print("X: ", x)

print(x)

name = "gowtham"

print(name)

print("My name is ",name," I am a CSE student")







# Input

name = input("Enter a name: ")

number = input("Enter a number: ")

default - String 

number = int(input("Enter a number: "))


Assignment 1.1:

1. 10, 1, 8, 3, 6, 5, 4, 7, x, y
    Find X and Y - general solution
    Write an algorithm for the same

2. Go through MyCaptain App and complete
    first assignment which is Area of a circle

NOT SUBMIT NOW
KEEP IT NOW, WILL TELL LATER

TAKE A SCREENSHOT









# Arithmetic Operators
# +, -, *, //, /, %

2 + 1

x = 4
y = 2

x + y

y * x


x * y

x / y

x // y # Floor Division - typecasting a float to int

x % y # Modulus - remainder






# Assignment Operator

x = 5

x = x + 1
x += 1

# Try this out

# Use this as less as possible
# Not a good programming etiquette





# Comparison Operators
# <, >, ==, <=, >=, !=

x = 4
y = 3

x > y = True

x < y = False

True, False = Boolean

x = 5
y = 5

x == y

x != y



# Logical Operator
# and, or, not


x = 5
y = 6

x != y
and
x < y


x != y and x<y







# Try this out
Assignment 1.2 (OPTIONAL)
1. Try Assignment operator and Logical Operator

Dont worry about submission yet
Complete assignment



# if statement

 Turing complete programming language ?
1. Alan Turing - How many of you know him?
2. Captcha - Not a Robot - Turing test

Movie: Imitation Games - seen ?

Cryptography - know ??

Hello - Encrypted - Ohell

Ohell - Decrypt - Hello

Turing Complete - Inducing Logic

# IF

If it rains tomorrow
then I will bring the umbrella

rain = 1

if rain == 1:
    print("Bring Umbrella") # Use first letter of print statements


If it rains tomorrow
then I will bring the umbrella
Else
I will NOT

rain = 0
if rain == 1:
    print("BU")
else:
    print("I will not")

Space is Indentation

If it rains tomorrow
then I will bring the umbrella
Else
If it snows tomorrow
then I will use boots

elif - statement

else + if = elif

rain = 1 # True
snow = 1 # True

if rain == 1:
    print("BU")
elif snow == 1:
    print("bring Boots - BB")
# and, or - Logical 











# Functions

def add(a, b):
    print(a+b)

# You have not called your function
add(1, 2)

add(2, 5)

# Main usage - Reusability
# More number of parameters
# More lines of body

Assignment 2.1:

1. Nested if-else statement in python (Google it)
Do NOT copy paste the code, rather write it

2. Create functions with 0, 3 and 4 parameters

3. Create a calculator
Example Output:
1. Add
2. Subtract

Enter a choice: 1

Enter value A1: 10
Enter value A2: 10

Result: 20
Complete creative freedom
core: (if-else statements and functions)

4. watch Imitation Games (optional)



# use of logical operator in if

and, or, not

rain = 1
snow = 1

If it rains and snows I will take the umbrella

rain==1 and snow==1
a. True
b. False
ans: a

rain = 1
snow = 0

rain==1 and snow==1
a. True
b. False
ans: b

if rain==1 and snow==1:
    print("BU")

a. BU
b. Error
c. Nothing
ans: c

rain = 1
snow = 0

rain==1 or snow==1
a. True
b. False
ans: a

if rain==1 or snow==1:
    print("BU")
a. BU
b. Error
c. Nothing

# Functions - return

def add(a, b):
    print(a+b)

add(1, 2)

c = addition of 1 and 2

c*2


def add(a, b):
    return a+b

c = add(1, 2)



# Data Structures

# Lists

l1 = [1, 2, 3, 4, 5.3, "gowtham"]

# Access
l1[0]

l1.append(66)

l1.pop()
a. add
b. remove - 66
c. remove - "gowtham"
ans: b


l1.pop()
b. remove - 5.3
c. remove - "gowtham"


# Strings
# Data Structure

a1 = ['g', 'o', 'w', 't', 'h', 'a', 'm']

a1[0]




a = "gowtham"

a[0]

a. error
b. 'g'
c. nothing
ans: b

extension? hint: use a string method


Assignment 2.2
Hyper Important

1. Implement all w3schools methods of lists and strings

Submission Procedure:
1. Add or upload ur code into github with
    different repository name NOT MyCaptain

2. Sending u a google forms link on Sunday
    paste ur github link in the forms

3. Deadline on Monday 12:30 AM and NOT 'PM'
   Early Morning 12:30 on Monday


Movies (Optional)
1. Imitation Games - real story of Alan Turing
2. The Big Short - real story of 2008 Financial Crisis

a = 10

Exact, Prefered, Best, Perfect way
A: print("Value: ", a)


Also ok
B: print("Value: "+str(a))




l1 = [1, 2, 3, 4]

I want to remove the element 2, how do I do it?
- Find answer

############################################

1. Is list ordered ?? - Yes

2. What is ordered ??
Having Index values

############################################

# Tuple
# Ordered
# Tuples are Immutable
# Immutable - cannot change
# Tuples are unchangeable list

t1 = (1, 2, 3, 4)

t1[0]


Use??
To retreive data faster than a List

Packages came into play - numpy


# Dictionary
# key-value pair

d1 = {"name":"Gowtham", "age":23, "branch":"CSE"}

name - key
Gowtham - value

d1["name"]



# Loops
# Performing a task repeatedly
# Putting a song on loop
# Turing Complete

print(1)
print(2)
..
..

for value in range(1, 11):
    print(value)

for i in range(0, 4):
    print(i)

l1 = [1, 2, 3, 4]

Display each element in the List l1

for i in range(0, 4):
    print(l1[i])

for i in range(0, 3):
    print(i)


3
4
5??

4 - length of List l1

How do you find length of List l1?
Is there a function to do that ??

for i in range(0, len(l1)):
    print(l1[i])


for elements in l1:
    print(elements)


# While

i = 0
while i<11:
    print(i)
    #i = i+1

infinite loop


l1 = [1, 2, 3, 4]

i = 0
while i<len(l1):
    print(l1[i])
    i = i+1
   


Assignment

1. Methods of dictionary
2. create the following pattern using for loop 





# Web Scraping

import requests
from bs4 import BeautifulSoup as bs

urls = ["https://www.amazon.in/United-Colors-Benetton-Sneakers-11-19P8SNEA3113I_902_40/dp/B07L58JVGV/ref=pd_d0_recs_v4_ac_w2_22/258-3905153-5220442?pd_rd_w=1uyYc&pf_rd_p=d07e23a0-088f-4edf-84b9-2836fb74cf31&pf_rd_r=4TKKTDR8TCG1WV73P70B&pd_rd_r=e725627d-a833-48c0-8d14-1869b648be09&pd_rd_wg=thhbR&pd_rd_i=B07LGJZ3YP&psc=1"]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}

page = requests.get(urls[0], headers=headers)

soup = bs(page.content, "html.parser")

title = soup.find(id="productTitle").get_text()

price = float(soup.find_all('span', attrs={"class":"a-price-whole"})[0].get_text()[:-1].replace(',', '.'))


price

from twilio.rest import Client

client = Client('ACe2a630f70c541317ddd1db56b251f57f', '39a9c77b662cc798172f9115c8fb')
client.message.create(to_='+919382601818', from_='+14703471360', body='Price Reduced '+urls[0])


# Classes

class Vehicle:
    def __init__(self, wheels, doors):
        self.wheels = wheels
        self.doors = doors
    
    def display(self):
        print("Vroom Vroom")

lambo = Vehicle(4, 2)
lambo.wheels


prius = Vehicle(4, 4)
prius.display()


l1 = [1, 2, 3]

l1.append(5)

l2 = [3, 4, 5, 6]



l1, l2  = object

















