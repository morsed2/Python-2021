name =				'For Loops In Python - #19'
Filename=  			'Lesson-19 For Loops.py'
Tomboy =			'Python Programming 2021'
# YouTube Link:		https://www.youtube.com/watch?v=Krrb2M8PwEQ&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=19
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


# For Loops

name = "John"
for x in name:
	print(x)

#-------------------------------------------------------
# So this makes more sense
print('\n')
name = "John"
for letter in name:
	print(letter)

#-------------------------------------------------------
print('\n')			# For a list
names = ["John","Mary","Peter"]

for name in names:
	print(name)

#-------------------------------------------------------
print('\n')			# For a dictonary
names = {
			"John":	"Perperoni",
			"Mary": "Cheese",
			"Peter": "Onion",
		}

for key, value in names.items():
	print("Wow..." + key + " likes " + value + " pizza")



#-------------------------------------------------------