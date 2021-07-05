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
from relative import RelativePath

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
		self.title("Set of Image-based Radiobuttons")
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
		self.radio_names = {"up" : RelativePath.get_image_path("images/arrow_up.png"),
								  "down" : RelativePath.get_image_path("images/arrow_down.png"),
								  "left" : RelativePath.get_image_path("images/arrow_left.png"),
								  "right" : RelativePath.get_image_path("images/arrow_right.png")}
		self.radio_var = StringVar()
		self.radiobuttons = []
		# populate
		for (name, image) in self.radio_names.items():
			self.radiobuttons.append(RadioItemButton(self, name, image, self.radio_var, ))
		# configure
		self.radiobuttons[2].invoke()
		self.config(borderwidth = 2, relief = "groove")
		# layout: VERTICAL (default)
		for radiobutton in self.radiobuttons:
			radiobutton.grid(sticky = 'nw', padx = 10)
	
	def show_choice(self, radio_item):
		print(f"radio_item: {radio_item}, value: {self.radio_var.get()}")
	
class RadioItemButton(ttk.Radiobutton):
	def __init__(self, parent, name, image, radio_variable):
		super().__init__(parent)
		# object attributes
		self.name = name
		# configure
		self.config(text = name, value = name, image = image, variable = radio_variable)
		self.config(command = lambda:parent.show_choice(self.name))


if __name__ == "__main__":
	main()
