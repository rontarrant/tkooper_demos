# Add or delete key/value pairs from the radio_names dictionary to suit your needs.
# The RadiobuttonSet (based on ttk.Frame) and RadioItemButton objects will automatically
# set the width and height for the set, making this very reusable.
# To pre-select a default, add:
#	self.radiobuttons[x].invoke()
# in the configure section of RadiobuttonSet where 'x' is a valid index into RadiobuttonSet.self.radiobuttons.
# NOTE: This also triggers the button's callback method.
from tkinter import *
from tkinter import ttk
import tkinter.font as font

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width = 310
		self.height = 100
		# configure
		self.title("Set of Radiobuttons")
		self.config(width = self.width, height = self.height)
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		self.config(padding = (10, 10, 10, 20))
		# populate
		radiobutton_set = RadiobuttonSet(self)
		# layout
		radiobutton_set.grid(padx = 5, pady = 5)

class RadiobuttonSet(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.radio_names = {"planes" : 11,
								  "trains" : 14,
								  "buses" : 32,
								  "automobiles" : 90,
								  "bicycles" : 68,
								  "skateboards" : 122,
								  "rollerblades" : 943,
								  "shanks mare" : 1}
		self.radio_var = StringVar()
		self.radiobuttons = []
		# populate
		for (name, value) in self.radio_names.items():
			self.radiobuttons.append(RadioItemButton(self, name, value, self.radio_var))
		# configure
		self.radiobuttons[2].invoke()
		self.config(borderwidth = 2, relief = "groove")
		# layout
		column_ = 0
		for radiobutton in self.radiobuttons:
			radiobutton.grid(sticky = 'nw', padx = 10, row = 0, column = column_)
			column_ += 1
	
	def show_choice(self, radio_item):
		print(f"radio_item: {radio_item}, value: {self.radio_var.get()}")
	
class RadioItemButton(ttk.Radiobutton):
	def __init__(self, parent, name, value, radio_variable):
		super().__init__(parent)
		# object attributes
		self.name = name
		# configure
		self.config(text = name, value = value, variable = radio_variable)
		self.config(command = lambda:parent.show_choice(self.name))


if __name__ == "__main__":
	main()
