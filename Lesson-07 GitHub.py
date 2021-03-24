# name:				Python Version Control With Git and Github - #7
# YouTube Link:		https://www.youtube.com/watch?v=yYknmU_gBgs&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=8
#
# Filename:  		'Lesson-07 GitHub.py'
#
#  $ cd "/c/Users/Nick/PycharmProjects/AA Python Programming 2021"      to get to the directory



full_name = 'Steve Morse'

# 6 types

# string
# number
# list
# Tuples
# Dictionary
# Boolean

# string
#		"A sting!"
first_name = "Steve"

# number
#		1, 1.1
age = 70

# list		are always in square brackets []
#		name = ["John", "Steve", "Pete"]	elements can be any data type including lists
names = ["John", "Steve", "Pete"]


# Tuples	are always in parentheses ()
#		is a list that cannot change (speeds up use), 
#		immutable (unchanging over time or unable to be changed.)
names2 = ("Ann", "Jane", "Mary")

# Dictionary 	are always in curly brackets {}
#	Are more complicated lists, normally entered on seperate lines
#	each entry is made up of a key and a value called a key value pair
#	the key and the value are seperated by a colon : and end with a comma ,
#		the last entry can have a comma , or not.
#	You use the key value to access its value

fave_pizza = {
	"John":	"Pepperoni",
	"Bob":	"Mushroom",
	"Mary":	"Cheese",	# can be removed
}

# Boolean
#	True or False

a_bool = True



import os

os.system('clear')
print("Hello World Again!!!!!!! This is lesson 06")
print("\n\n\n")

print(full_name)
print("\n")
print(age)
print("\n")
print(names)     # prints everything in the list
print(names[1])  # Any one item
print("\n")
print("\n")
print(names2)     # prints everything in the list
print(names2[1])  # Any one item
print("\n")
print("\n")
print(fave_pizza)
print(fave_pizza["Bob"])
print("\n")
print("Thats all folks TTFN.\n\n\n")



