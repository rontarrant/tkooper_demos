# Validate a Postal Code entered by the user.
# NOTE: %s is to represent entry_content, but this is _before_ validation.

from tkinter import *
from tkinter import ttk
from canadian_postal_code import CheckPostalCode

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Validate a Canadian Postal Code"
		# configure
		self.title(self.title_text)
		self.config(width = 260, height = 100)
		#populate
		postal_code_label = EntryLabel(self, "Postal Code:")
		postal_code_entry = NumericEntry(self)
		city_label = EntryLabel(self, "City:")
		city_entry = CityEntry(self)
		# layout
		postal_code_label.grid(row = 0, column = 0)
		postal_code_entry.grid(row = 0, column = 1)
		city_label.grid(row = 1, column = 0)
		city_entry.grid(row = 1, column = 1)

class EntryLabel(ttk.Label):
	def __init__(self, parent, label_text):
		super().__init__(parent)
		self.config(text = label_text)
	
class CityEntry(ttk.Entry):
	def __init__(self, parent):
		super().__init__(parent)
		
class NumericEntry(ttk.Entry):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.error = ""
		self.var = StringVar()
		self.reg = (self.winfo_toplevel().register(self.validate_input), '%S', '%s', '%V')
		self.inreg = (self.winfo_toplevel().register(self.invalid_input), '%s', '%V')
		# configure
		self.config(textvariable = self.var, validate = "all", validatecommand = self.reg, invalidcommand = self.inreg)

	def validate_input(self, new_value, entry_content, validation_type):
		validated = True # assume it's right
		
		if validation_type == "key":
			print("key validation")
			if new_value.isdigit() or new_value.isalpha():
				validated = True
			elif new_value == '':
				validated = False
			else:
				validated = False
		elif validation_type == "focusout":
			print("focusout validation")
			# is it a valid postal code?
			valid = CheckPostalCode.check_postal_code(entry_content)
			print(f"valid = {valid}")
			
			if valid[0] == False:
				self.error = valid[1]
				validated = False
				print("self.error: {self.error}")
		elif validation_type == "focusin":
			print("focusin validation")
			pass

		return validated

	def invalid_input(self, entry_content, validation_type):
		if validation_type == "focusout":
			if len(entry_content) < 6:
				print("field cannot be left blank")
				self.focus()
				self.icursor(0)
			elif self.error != "":
				print(f"error: {self.error}")
				self.focus()
				self.icursor(0)
	 
	 
if __name__ == "__main__":
	main()
