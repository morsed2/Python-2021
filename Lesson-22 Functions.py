name =				'Creating Functions With Python - #22'
Filename=  			'Lesson-22 Functions.py'
Tomboy =			'Python Programming 2021'
# YouTube Link:		https://www.youtube.com/watch?v=4NQvoUyTI5U&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=22
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




# print(outcome * 20)   #will throw an error as newFunc() has not YET been defined




# Functions



def nameif(name, name2):
	print("Hello "+ name + " " + name2)


myName = "Pete"
myName2 = "Jones"
nameif(myName, myName2)



def newFunc(num1, num2):
	return (num1 + num2)



outcome = newFunc(11,21)
print(outcome * 20)


