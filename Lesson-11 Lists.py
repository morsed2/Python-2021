name =				'Lists in Python - #11'
Filename=  			'Lesson-11 Lists.py'
Tomboy =			'Python Programming 2021'
# YouTube Link:		https://www.youtube.com/watch?v=N6PRLl5s6TE&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=11
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
print("\n\n\n" + name + "\t" + Filename + "\t", Tomboy + "\n\n")
print('-----------------------------------------------------------\n\n')

# What is a list in Python
# Lists are in []
# We can changes list BUT we connot change Tuples

names = ["John", "Bob", "Tina"]
print(names)
print(names[1])

# Elements can be changed as required
names[1] = "Steve"
print(names)
print(names[1])


# To add an element TO THE END
names.append("Wess")		
print(names)
print(names[3])


# To add an element even if it is a variable
newName = "Pete"
names.append(newName)		
print(names)
print(names[4])


# Also lists inside lists
anotherList = [1,2,3,4,5]
names.append(anotherList)		
print(names)
print(names[5])
print(names[5][2])    # [] Added to access the list within a list


# for the number of items
print(len(names))
print(names[len(names)-1])	# For the last item






