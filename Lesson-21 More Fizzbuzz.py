name =				'More Fizzbuzz With Python - #21'
Filename=  			'Lesson-21 More Fizzbuzz.py'
Tomboy =			'Python Programming 2021'
# YouTube Link:		https://www.youtube.com/watch?v=PBfc6MP2hxY&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=21
#
#  $ cd "/c/Users/Nick/PycharmProjects/AA Python Programming 2021"      to get to the directory
#
# ------------------------------------------------------------------------------------------------------------
#            Git push commands
# git add .
# git commit -am "SuitableText"
# git push
# <password, tavr>
#
#
# Git Bash Shortcut path     "c:\Users\Nick\PycharmProjects\AA Python Programming 2021"
#						https://github.com/morsed2/Python-2021/tree/master
#
# ------------------------------------------------------------------------------------------------------------

import os
os.system("clear")
print("\n\n\n" + name + "\t\t" + Filename + "\t", Tomboy + "\n\n")
print('-----------------------------------------------------------\n\n')


# WTF is MORE Fizzbuzz?


# printout all the numbers from 1 to 100

# if the number is dfiviziable by 3 also print fizz

# if the number is dfiviziable by 5 also print buzz

# if the number is dfiviziable by 3 AND 5 also print fizzbuzz

# Count how many fizzes,  buzzes, and fizzbuzzes

counter = 1000000

fizzes = 0
buzzes = 0
fizzbuzzes = 0


for x in range(1, counter):
	y=x%3
	z=x%5



	if (y == 0 and z != 0):
		print(str(x) + " fizz")
		fizzes += 1
	else:
		if (z == 0 and y != 0):
			print(str(x) + " buzz")
			buzzes += 1
		else:
			if (z == 0 and y == 0):
				print(str(x) + " fizzbuzz")
				fizzbuzzes += 1
			else:
				print(str(x))

# OK I did this on my own!, John used a while loop!
print('--------------------------------------------')
print ("Fizzes = \t" + str("{:,}".format(fizzes)))
print ("Buzzes = \t" + str("{:,}".format(buzzes)))
print ("FizzBuzzes = \t" + str("{:,}".format(fizzbuzzes)))