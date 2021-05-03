name =				'SQLite Tutorial: Build a Python project with a SQLite database'
Filename=  			'App.py'		# Application commands file
Tomboy =            'Not registered in Tomboy yet.'
#
# Files used on disk:
Main_app =   		'App.py'		# This file
Database_app =		'database.py'	# Controls the database
data_file =			'data.db'		# The actual database file
#
#  $ cd "/c/Users/Nick/PycharmProjects/AA Python Programming 2021"      to get to the directory
#	C:\Users\Nick\PycharmProjects\AA Python Programming 2021            windows way!
#
#------------------------------------------------------------------------------------------------------------
#
#	Main (Initial) Project:
#
#		Python SQLite Tutorial: Build a Python project with a SQLite database
#		https://www.youtube.com/watch?v=iXYeb2artTE	
#
#	A usful SQLite tutorial and a small program devlopment
#	36 minutes  
#
#
#	A follow on project
#
#		Python SQLite Tutorial: Complete Overview - Creating a Database, Table, and Running Queries
#		https://www.youtube.com/watch?v=pd-0G0MigUA
#
#	Adds alternative INSERT's, UPDATES, and REMOVES
#	30 minutes  
#
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
print("\n\n\n" + name + "\nFilename = " + Filename + "\t", Tomboy + "\n\n")
print('-----------------------------------------------------------\n\n')

MENU_PROMPT = """  --- Coffee Bean App ---

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit the program.

Enter your selection, Please...:
"""





print("+++++++++++++++++++++++++ Why?")



import database

def menu():
	connection = database.connect()
	database.create_tables(connection)



	while (user_input := input(MENU_PROMPT)) != "5":
		print(user_input)

		if user_input == "1":
			print('Option 1 selected')
			name = input("Enter bean name: ")
			method = input("Enter how you prepared it: ")
			rating = int(input("Enter your rating score (0-100): "))

			database.add_bean(connection, name, method, rating)



		elif user_input == "2":
			print('Option 2 selected')
			beans = database.get_all_beans(connection)

			for bean in beans:
				print(bean)		# Prints a tuple
				print(f"{bean[1]} \t ({bean[2]})\t - {bean[3]}/100")




		elif user_input == "3":
			print('Option 3 selected')
			name = input("Enter bean name to find: ")
			beans=database.get_beans_by_name(connection, name)

			for bean in beans:
				print(bean)		# Prints a tuple
				print(f"{bean[1]} \t ({bean[2]})\t - {bean[3]}/100")



		elif user_input == "4":
			print('Option 4 selected')
			name = input("Enter bean name to find: ")
			best_method = database.get_best_preparation_for_bean(connection, name)

			print(f"The best preparation for {name} is: {best_method[2]}")



		else:
			print('Invalid Option selected, please try again')

		print('\n\n\n')




# ==========================================================================
# Main Program

menu()