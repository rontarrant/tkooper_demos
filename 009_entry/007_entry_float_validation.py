# Given a string entered by the user, make sure it's a valid floating point number.
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Validate a Floating Point Number"
		# configure
		self.title(self.title_text)
		self.grid_propagate(False)
		self.config(width = 360, height = 50)
		#populate
		numeric_entry = NumericEntry(self)
		# layout
		numeric_entry.grid()

class NumericEntry(ttk.Entry):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.var = StringVar()
		self.reg = (self.winfo_toplevel().register(self.validate_input), '%S', '%s')
		self.inreg = (self.winfo_toplevel().register(self.invalid_input), '%s')
		# configure
		self.config(textvariable = self.var, validate = "key", validatecommand = self.reg, invalidcommand = self.inreg)

	def validate_input(self, new_value, entry_content):
		valid = True
		
		if new_value.isdigit() or new_value == '.':
			if new_value == '.' and '.' in entry_content:
				print(f"A decimal already exists in this number: {entry_content}")
				valid = False
		elif new_value.isalpha():
			print("Numerals only, please.")
			valid = False

		return valid

	def invalid_input(self, entry_content):
		print("Please try again.")
		index = entry_content.find('.')
		self.icursor(index)
		
if __name__ == "__main__":
	main()
