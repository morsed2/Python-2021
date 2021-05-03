name =				'Fizzbuzz With Python - #20'
Filename=  			'Lesson-20 Fizzbuzz.py'
Tomboy =			'Python Programming 2021'
# YouTube Link:		https://www.youtube.com/watch?v=s3trxPS3ggI&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=20
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


# WTF is Fizzbuzz?

# printout all the numbers from 1 to 100

# if the number is dfiviziable by 3 also print fizz

# if the number is dfiviziable by 5 also print buzz

# if the number is dfiviziable by 3 AND 5 also print fizzbuzz


for x in range(1, 101):
	y=x%3
	z=x%5

	if (y == 0 and z != 0):
		print(str(x) + " fizz")
	else:
		if (z == 0 and y != 0):
			print(str(x) + " buzz")
		else:
			if (z == 0 and y == 0):
				print(str(x) + " fizzbuzz")
			else:
				print(str(x))

# OK I did this on my own!, John used a while loop!