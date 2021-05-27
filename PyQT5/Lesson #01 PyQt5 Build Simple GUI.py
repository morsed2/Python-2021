name =				'How To Install PyQt5 And Build Simple GUI App - PyQt5 GUI Thursdays #1'
Filename = 			'Lesson #01 PyQt5 Build Simple GUI.py'
Tomboy =			'Lessons PyQT5'
# YouTube Link:		https://www.youtube.com/watch?v=rZcdhles6vQ&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=1
#
#		cd "/c/Users/Nick/PycharmProjects/AA Python Programming 2021 -GIT/PyQT5"    Git Bash code to get to the directory
#
#		C:\Users\Nick\PycharmProjects\AA Python Programming 2021 -GIT\PyQT5 	Windows code to get to directory
#
#
# ------------------------------------------------------------------------------------------------------------
#            Git push commands
# git add .
# git commit -am "SuitableText"
# git push
# <password, tavr>
# ------------------------------------------------------------------------------------------------------------



'''
import os


def open_text_display():
	os.system("clear")
	print("\n\n\nName:\t   " + name + "\nFilename:  " + Filename + "\nTomboy:\t  ", Tomboy + "\n\n")
	print('-----------------------------------------------------------\n\n')
open_text_display()
'''


# Some code to start the ... [virtual inviroment]

# In the Git Bash Terminal:
#		python -m venv virt                 #virt is my name for the virtual inviroment
#											# Takes a while
#
#		ls                 					#virt/ in purple should show up
#
#		source virt/Scripts/activate		# should show (virt)
#
#		Now the prompt has (virt) above it!	    ie...
#												(virt)
#												Nick@Steve-HP MINGW64 ~/PycharmProjects/PyQT5
#
#		deactivate							# will turn it off


import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		# Add a Title
		self.setWindowTitle("Hello World!!!")
		# Set the layout, several layout vert, hori box, grid etc
		self.setLayout(qtw.QVBoxLayout())     # V=vertical
		# Create a label
		my_label = qtw.QLabel("Hello. What's your name? ")
		# Change font size of label
		my_label.setFont(qtg.QFont('Helvetica', 18))
		self.layout().addWidget(my_label)
		# Create an entry box
		my_entry = qtw.QLineEdit()
		my_entry.setObjectName("name_field")
		my_entry.setText("Place holder text")	# This needs to be deleted by the user
		self.layout().addWidget(my_entry)
		# Create a button
		my_button = qtw.QPushButton("Press Me!", clicked=lambda: press_it())
		self.layout().addWidget(my_button)

		# Show the app!
		self.show()

		#=================================================
		# Class Functions

		def press_it():
			my_label.setText(f'Hello {my_entry.text()} how are you today?')
			my_entry.setText("")							# Delete the entry text!


app = qtw.QApplication([])
mw  = MainWindow()

# Run the App
app.exec_()