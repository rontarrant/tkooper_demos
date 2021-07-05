# Given a string entered by the user, validate it as a sentence... although not too stringently.
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Validate a Sentence"
		# configure
		self.title(self.title_text)
		self.grid_propagate(False)
		self.config(width = 260, height = 50)
		#populate
		string_entry = StringEntry(self)
		# layout
		string_entry.grid()

class StringEntry(ttk.Entry):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.var = StringVar()
		self.reg = (self.winfo_toplevel().register(self.validate_input))
		# configure
		self.config(textvariable = self.var, validate = "key", validatecommand = (self.reg, "%S"))
		self.focus()

	def validate_input(self, new_value):
		valid_characters = (" ", ".", ",", "!", ":", ";", "'", '"')
		valid = (new_value.isalpha() or new_value in valid_characters)
		 
		return valid


if __name__ == "__main__":
	main()
