name =				'SQLite Database With Python - #24'
Filename=  			'Lesson-24 SQLite.py'
Tomboy =			'Python Programming 2021'
# YouTube Link:		https://www.youtube.com/watch?v=xTYFtynwgAI&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=24
#
#  $ cd "/c/Users/Nick/PycharmProjects/AA Python Programming 2021"      to get to the directory
#
#------------------------------------------------------------------------------------------------------------
#
#
#	Python SQLite Tutorial: Build a Python project with a SQLite database
#	https://www.youtube.com/watch?v=iXYeb2artTE	
#
#	A usful SQLite tutorial and a small program devlopment
#	36 minutes  
#
#
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
print("\n\n\n" + name + "\t\t" + Filename + "\t", Tomboy + "\n\n")
print('-----------------------------------------------------------\n\n')


# Great for starting
# Already installed in Python

import sqlite3


# -----------------------------------------------------------------------
# 1/ connect to an existing database (or create is it does not exist)
connection = sqlite3.connect('cust.db')
print("Database created/opened\n\n")


# -----------------------------------------------------------------------
# 2/ Create a cursor for the above
cursor = connection.cursor()
print("Cursor (re)created\n")


# -----------------------------------------------------------------------
# 3/ Fill a table, ie do something, using the DOC string ("""  """) notation
cursor.execute("""
	CREATE TABLE IF NOT EXISTS customer 
		(
			first_name text,
			last_name  text,
			email      text,
			age		   integer
		)
""")
print("Table structure created if it does not exist")


# -----------------------------------------------------------------------
# 4/ Then to actually do some work, we have to commit. IE commit our changes
cursor = connection.commit()   # Remember after a commit, you have to reconnect
print("Last command above commited\n\n")


# -----------------------------------------------------------------------
# 5/ Enter some data
cursor = connection.cursor()		# Do not forget to reconnect
print("Cursor (re)created")
cursor.execute("INSERT INTO customer VALUES ('Steve','Morse','morsed2@gmail.com',70)")
print("Some data added")


# -----------------------------------------------------------------------
# 4/ (again!) Then to actually do some work, we have to commit. IE commit our changes
cursor = connection.commit()
print("Last command commited\n\n")


# -----------------------------------------------------------------------
# 6/ View some data
cursor = connection.cursor()		# Do not forget to reconnect
print("Cursor (re)created")
cursor.execute("SELECT * FROM customer")	# * = every thing
print("Some data fetched")
items = cursor.fetchall()

for item in items:
	print(item)


# -----------------------------------------------------------------------
# 4/ (again!) Then to actually do some work, we have to commit. IE commit our changes
cursor = connection.commit()
print("Last command commited\n\n")





# -----------------------------------------------------------------------
# Close the database connect when finished
connection.close()
print("Connection closed\n\n")


