name =				'Dictionaries in Python - #13'
Filename=  			'Lesson-13 Dictionaries.py'
Tomboy =			'Python Programming 2021'
# YouTube Link:		https://www.youtube.com/watch?v=7IceYneXv3A&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=13
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


# What is a Dictionary?
# Something with a key value pair in this form key: value,    note colon :  and the comma ,
# a dictionary uses curly braces {}



fav_pizza = {
	"John":	"Pepper",
	"Tim": "Sauage",
	"Mary": "Cheese",		# note last comma
}

print(fav_pizza)
print("Invidual item..." + fav_pizza["Tim"])    # item after + must be string

# del fav_pizza["John"]		# uses the del command
print(fav_pizza)

fav_pizza.update({"Tina": "Green Peppers",})
print(fav_pizza)
print(fav_pizza["Tina"])

fav_pizza["John"] = "MUSHROOMS"
print(fav_pizza)
fav_pizza["John"] = [1,2,3,4,5]
print(fav_pizza)