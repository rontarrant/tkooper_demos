## Reveal all options for the Button class.
## NOTE: For this to work, Button must be instantiated.
from tkinter import *
from tkinter import ttk

## option values in order:
## - option name,
## - name of the option in the option database,
## - Class,
## - default value,
## - current value.

from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		# configure
		#populate
		mainframe = MainFrame(self)
		self.option_add('*tearOff', FALSE) # must be set BEFORE any menus are created
		self.menubar = Menubar(self)
		# configure
		self.config(menu = self.menubar)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		#hello_label = HelloLabel(self)

class Menubar(Menu):
	def __init__(self, window):
		super().__init__(window)
		# menus
		file_menu = FileMenu(self)
		#edit_menu = EditMenu(self)
		# attach menus
		self.add_cascade(menu = file_menu, label = file_menu.label_text)
		#self.add_cascade(menu = edit_menu, label = edit_menu.label_text)
		self.show_options()

	def show_options(self):
		option_values = ["name", "database name", "class", "default value", "current value"]

		config_options = self.configure()

		for key, value in config_options.items():
			print(f"Key: {key}")
			if len(value) > 2:
				for i in range(5):
					print(option_values[i], ": ", value[i])
			print("\n")

class FileMenu(Menu):
	def __init__(self, menubar):
		super().__init__(menubar)
		# object attributes
		self.label_text = "File"
		# menu items
		new_item = NewItem(self)
		open_item = OpenItem(self)
		
		# populate
		self.add_command(label = new_item.text, command = new_item.command)
		self.add_command(label = open_item.text, command = open_item.command)
		self.show_options()
		
	def show_options(self):
		option_values = ["name", "database name", "class", "default value", "current value"]

		config_options = self.configure()

		for key, value in config_options.items():
			print(f"Key: {key}")
			if len(value) > 2:
				for i in range(5):
					print(option_values[i], ": ", value[i])
			else:
				for i in range(2):
					print(option_values[i], ": ", value[i])
					
			print("\n")

class NewItem():
	def __init__(self, parent_menu):
		self.text = "New"
		self.command = self.new_file
		
	def new_file(self):
		print("Creating a new file...")

class OpenItem():
	def __init__(self, parent_menu):
		self.text = "Open"
		self.command = self.open_file
		
	def open_file(self):
		print("Opening a file...")

class HelloLabel(ttk.Label):
	text = "Show Options"
	
	def __init__(self, frame):	
		super().__init__(frame)
		# object attributes
		# configure
		self.grid()
		self.config(text = self.text)
		self.show_options()

	def show_options(self):
		option_values = ["name", "database name", "class", "default value", "current value"]

		config_options = self.configure()

		for key, value in config_options.items():
			print(f"Key: {key}")
			for i in range(5):
				print(option_values[i], ": ", value[i])
			print("\n")
	
if __name__ == "__main__":
	main()
