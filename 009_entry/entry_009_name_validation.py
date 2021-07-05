# Validate a name entered by the user.
# Unless the name is "k.d. lang," any name entered without leading capitals will be converted to title case.
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Name Validation Entry"
		# configure
		self.title(self.title_text)
		self.config(width = 360, height = 100)
		self.grid_propagate(False)
		#populate
		name_label = EntryLabel(self, "Name:")
		name_entry = StringEntry(self)
		location_label = EntryLabel(self, "Location:")
		location_entry = StringEntry(self)
		# layout
		name_label.grid(row = 0, column = 0, sticky = 'e')
		name_entry.grid(row = 0, column = 1)
		location_label.grid(row = 1, column = 0, sticky = 'e')
		location_entry.grid(row = 1, column = 1)

class StringEntry(ttk.Entry):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.var = StringVar()
		self.reg = (self.winfo_toplevel().register(self.validate_input))
		# configure
		self.grid_configure(padx = 10, pady = 10)
		self.config(textvariable = self.var, validate = "all", validatecommand = (self.reg, "%S", "%P", '%V', '%d'))
		self.focus()
		
	def validate_input(self, new_value, entry_content, validation_type, action_code):
		'''
		Validates input, taking into account such things as initials (N.J. Bates), credentials (M.B.A.), 
		hyphenated names (Billy-Bob Thornclamp), or names given in first, last order (Bates, Norman).
		If the name(s) aren't capitalized, and the name given isn't 'k.d. lang,' title case is applied.
		'''
		valid = True
		
		if action_code != 1:
			valid = True
		
		if validation_type == "key":
			valid_characters = (" ", ".", ",", "-") # '.' for initials or creditials; ',' for last, first order or creditials
			valid = (new_value.isalpha() or new_value in valid_characters)
		elif validation_type == "focusout":
			valid = True
			
			if entry_content != "k.d. lang":
				self.var.set(entry_content.title())
			else:
				self.var.set(entry_content)

			print(self.var.get())

		return valid

class EntryLabel(ttk.Label):
	def __init__(self, parent, label_text):
		super().__init__(parent)
		# configure
		self.grid_configure(padx = 10, pady = 10)
		self.config(text = label_text)
	

if __name__ == "__main__":
	main()
