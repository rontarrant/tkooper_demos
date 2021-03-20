from tkinter import *
from tkinter import ttk

class QuitButton(ttk.Button):
	def __init__(self, parent, window):
		super().__init__(parent)
		# object attributes
		self.text = 'Quit'
		self.top_window = window
		# configure
		self.config(text = self.text, command = self.quit)

	def quit(self):
		# do someting
		self.top_window.quit()
