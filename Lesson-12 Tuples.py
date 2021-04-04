name =				'Tuples in Python - #12'
Filename=  			'Lesson-12 Tuples.py'
Tomboy =			'Python Programming 2021'
# YouTube Link:		https://www.youtube.com/watch?v=9-vvUGyUcLw&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=12
#
#  $ cd "/c/Users/Nick/PycharmProjects/AA Python Programming 2021"      to get to the directory
#
# ------------------------------------------------------------------------------------------------------------
#            Git push commands
# git add .
# git commit -am "SuitableText"
# git push
# <password, tavr>
# ------------------------------------------------------------------------------------------------------------

import os
os.system("clear")
print("\n\n\n" + name + "\t\t" + Filename + "\t", Tomboy + "\n\n")
print('-----------------------------------------------------------\n\n')


# What is a Tuple
# A Tuple is immutable (unchangable), sorta kinda, true
# Cannot be changed after creation, no adding, no changing no nothing!
# A Tuple has () prenthese around it.
# Why use:
#			faster?
#			need for unchanging data, such as const in C
#			No real need to use, as a list is more versitile.



names = ("Steve", "Fred", "Tom")
print(names)

names2 = ("Mary",)   # Note the comma is needed
names3 = names + names2

names = names3	# Not changes BUT remade, recreated
print(names)

