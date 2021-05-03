name =				'Creating Desktop Apps With Python and TKinter - #25'
Filename=  			'Lesson-25 Desktop Apps.py'
Tomboy =			'Python Programming 2021'
# YouTube Link:		https://www.youtube.com/watch?v=ji8pTynQhEo&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=25
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








from tkinter import *	#Note TK is in capitals, * is everything
import os
os.system("clear")
print("\n\n\n" + name + "\t\t" + Filename + "\t", Tomboy + "\n\n")
print('-----------------------------------------------------------\n\n')


# --------------------------------------------------------------------------
# Functions

def hello():
	hello_label = Label(root, text='Hello ' + myTextbox.get())
	hello_label.pack()





# --------------------------------------------------------------------------


root = Tk()
root.title('Steve Code - How to learn!')
root.geometry("400x600")


# Lable - 2 step process, make it, display it
myLabel = Label(root, text = "Enter your first name.... ")
myLabel.pack()

# Enter text
myTextbox = Entry(root, width=30)
myTextbox.pack()


# Now for a button
myButton = Button(root, text="Submit", command = hello)
myButton.pack()


root.mainloop()		# This bit makes it run!
