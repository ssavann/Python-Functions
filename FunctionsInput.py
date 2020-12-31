"""
Review: 
Create a function called greet(). 
Write 3 print statements inside the function.
Call the greet() function and run your code.

"""
#define a function called "greet()"
def greet():
    print("Hello!")
    print("What is your name?")
    print("Where are you from?")



#to use the function (to call a function)
greet()

print("===================")



#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")
    print("===================")


#calling the function and add any name inside parenthesis
greet_with_name("Toto")
greet_with_name("Angela")

"""
Hello Toto!
How do you do Toto?
===================
Hello Angela!
How do you do Angela?
===================

"""


#Function with more than one input
def my_location(number, name_of_street):
    print(f"My house number is {number}")
    print(f"My street name is {name_of_street}")
    print("===================")


my_location(456, "Bourrassa")
my_location(9055, "Beverly")


#Function with "Keyword" arguments
def student_score(studentA = 71, studentB = 93, studentC = 85):
    print(f"Student B score is: {studentB}")
    print(f"Student C score is: {studentC}")
    print(f"Student A score is: {studentA}")
    print("===================")

student_score()
"""
Student B score is: 93
Student C score is: 85
Student A score is: 71

"""

#It will replace the "default" value by these values
student_score(88, 62 , 77)  
"""
Student B score is: 62
Student C score is: 77
Student A score is: 88

"""