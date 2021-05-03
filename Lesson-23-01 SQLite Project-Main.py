name =				'SQLite Database With Python Project-Main - #23-01'
Filename=  			'Lesson-23-01 SQLite Project-Main.py'		# This file
Filename_DB=  		'Lesson-23-02 SQLite Database.db'			# The database
Filename_App=  		'Lesson-23-03 App.db'						# Application file, uses DB
Tomboy =			'Python Programming 2021'
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
print("\n\n\n" + name + "\t\t" + Filename + "\t", Tomboy + "\n\n")
print('-----------------------------------------------------------\n\n')


# Great for starting
# Already installed in Python

# -----------------------------------------------------------
# Create Table Notes
#
#	creates the table, error is it existed
#	|
#	|							table name
#	|							|	
#	|							|				   Auto increments
#	|							|					|
#	CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);
#				 |	
#				 |
# 				Get rid of error above


# -----------------------------------------------------------
# Insert Notes
#
#
#	INSERT INTO beans VALUES (1, 'Exclusive Blend', 'Percolator', 65);
#
# Must have single quotes (check)
# Values must match type, ie TEXT, INTEGER, etc; and be in the correct position
#
# BUT!!!!! the id is auto-inc, so we dont need to p[ass a value
# But notice the change on how we present the data...
#
#	INSERT INTO beans (name, method, rating) VALUES ('Exclusive Blend', 'Percolator', 65);
#
# column names must match
# also, QUESTION can  VALUES be variables?????
#


# -----------------------------------------------------------
# SELECT Notes
#
#
#	SELECT * FROM beans;		# Gets everything
#									all the columns
#									all the rows
#
# or ...
#
#
#	SELECT name, method FROM beans;		# Gets everything
#											only the columns, name & method
#											all the rows
#
# and ...
#
#	they can be sorted
#
#	SELECT name, method rating FROM beans ORDER BY rating DESC;		# Gets everything
#																	only the columns, name, method & rating
#																	all the rows, and SORTED by rating
#																	DESC = decending, ASC = acending
#
#
#	SELECT method rating FROM beans ORDER BY rating DESC LIMIT 1;	# Gets just 1 row
#																	only the columns, method & rating
#																	one row.
#																	DESC = decending, ASC = acending
#		ie the largest value is returned
#
#
# -----------------------------------------------------------
# WHERE Notes
#
#	SELECT * FROM beans WHERE name = 'Exclusive Blend';			# Gets just 1 rows		
# 																Gets rows ONLY Exclusive Blend
#																all the columns
#
#
#     Spelling must be exact!
#
#
#
#
# -----------------------------------------------------------
# Everything! Notes
#
#
#	SELECT * FROM beans						# Get everything from beans, but
#	WHERE name = 'Exclusive Blend'			# only is it is 'Exclusive Blend'
#	ORDER BY rating							# sort by rating
#	LIMIT 1;								# get the first (ie the top) one
#
#
#
#
#
# -----------------------------------------------------------
# GROUP BY Notes
#
#
#	SELECT method FROM beans GROUP BY method;
#
#
#		returns all the methods, without the names
#		duplicates are all merged into a sigle entry
#
# USE:
#
#
#	SELECT method, AVE(rating) FROM beans GROUP BY method;
#
#
#		AVG is averages of ALL the ratings for all methods
#			can I assume that MIN, MAX, etc are supported
#
#
#





import sqlite3




def DB_connect(Filename):
	return sqlite3.connect(Filename)


def DB_create_tables(connection):
	with connection:
		connection.execute(
		"CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"
		)