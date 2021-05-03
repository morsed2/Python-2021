name =				'SQLite Tutorial: Build a Python project with a SQLite database'
Filename=  			'Database.py'		# DB commands file
Tomboy =            'Not registered in Tomboy yet.'
#
#  $ cd "/c/Users/Nick/PycharmProjects/AA Python Programming 2021"      to get to the directory
#	C:\Users\Nick\PycharmProjects\AA Python Programming 2021            windows way!
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
print("\n\n\n" + name + "\nFilename = " + Filename + "\t", Tomboy + "\n\n")
print('-----------------------------------------------------------\n\n')



# ----------------------------------------------------------------------
# SQL, SQLlies commands (in strings so we can change easly)

CREATE_BEANS_TABLE = "CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"

INSERT_BEAN = "INSERT INTO beans (name, method, rating) VALUES (?, ?, ?);"

GET_ALL_BEANS = "SELECT * FROM beans"

GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"

GET_BEST_PREPARATION_FOR_BEAN = """
	SELECT * FROM beans
	WHERE name = ?
	ORDER BY rating DESC
	LIMIT 1
"""



import sqlite3

def connect():
	return sqlite3.connect("data.db")


def create_tables(connection):
	with connection:
		connection.execute(CREATE_BEANS_TABLE)


def add_bean(connection, name, method, rating):
	with connection:
		connection.execute(INSERT_BEAN, (name, method, rating))


def get_all_beans(connection):
	with connection:
		return connection.execute(GET_ALL_BEANS).fetchall()


def get_beans_by_name(connection, name):
	with connection:
		return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()


def get_best_preparation_for_bean(connection, name):
	with connection:
		return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()