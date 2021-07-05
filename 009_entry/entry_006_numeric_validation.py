# Given a string entered by the user, make sure it's a number.
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Number Validation"
		# configure
		self.title(self.title_text)
		self.grid_propagate(False)
		self.config(width = 260, height = 50)
		#populate
		numeric_entry = NumericEntry(self)
		# layout
		numeric_entry.grid()

class NumericEntry(ttk.Entry):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.var = StringVar()
		self.reg = (self.winfo_toplevel().register(self.validate_input))
		# configure
		self.config(textvariable = self.var, validate = "key", validatecommand = (self.reg, "%S"))

	def validate_input(self, new_value):
		print(new_value)
		valid = (new_value.isdigit())
		 
		return valid


if __name__ == "__main__":
	main()
