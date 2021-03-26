# name:				Numbers and Math in Python - #10
# YouTube Link:		https://www.youtube.com/watch?v=3RpJ_Idr-2w&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=10
#
# Filename:  		'Lesson-10 Math.py'
#
#  $ cd "/c/Users/Nick/PycharmProjects/AA Python Programming 2021"      to get to the directory
#
#            Git push commands
# git add .
# git commit -am "SuitableText"
# git push
# <password, tavr>

import os
os.system("clear")

print("Strings in Python - #9")

greetings = 'My boss shouter \n"Get back to work"'  # use of quotes
greetings = "My boss shouter \nGet back to work\"" # use of esq char \
print(greetings)


# Concationation only works with strings, no int, bool, etc
name = "Steve Morse"
greetings = "Hello, my name is " + name
print(greetings)

# Methods, function. Python is an oops laguage

print(greetings.upper())
print(greetings.lower())
print(greetings.capitalize())
print(greetings.title())
print(greetings.swapcase())

print(len(greetings))
print(greetings[13])
print(greetings[18:23])


print(greetings.split(" "))		# Note the type changes from string to a list
print(greetings.split(" ")[5])	# the 6th item in the list
print(greetings.split(" ")[4:6])	# the 4th thru 6th item in the list


