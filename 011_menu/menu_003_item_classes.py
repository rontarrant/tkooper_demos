# In this example, each menu item has its own class, which may be overkill.

from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		windowing_system = self.tk.call('tk', 'windowingsystem') # ID the windowing system
		self.option_add('*tearOff', FALSE) # must be set BEFORE any menus are created
		self.menubar = Menubar(self)
		# configure
		self.config(menu = self.menubar)

class Menubar(Menu):
	def __init__(self, window):
		super().__init__(window)
		# menus
		file_menu = FileMenu(self)
		edit_menu = EditMenu(self)
		# attach menus
		self.add_cascade(menu = file_menu, label = file_menu.label_text)
		self.add_cascade(menu = edit_menu, label = edit_menu.label_text)

class FileMenu(Menu):
	def __init__(self, menubar):
		super().__init__(menubar)
		# object attributes
		self.label_text = "File"
		# menu items
		new_menu_item = NewMenuItem(self)
		# populate
		self.add_command(label = new_menu_item.label_text, command = new_menu_item.command)

class NewMenuItem():
	def __init__(self, parent_menu):
		self.label_text = "New"
		self.command = self.new_file
		
	def new_file(self):
		print("Creating a new file...")

class EditMenu(Menu):
	def __init__(self, menubar):
		super().__init__(menubar)
		# object attributes
		self.label_text = "Edit"
		# menu items
		copy_menu_item = CopyMenuItem(self)
		# populate
		self.add_command(label = copy_menu_item.label_text, command = copy_menu_item.command)

class CopyMenuItem():
	def __init__(self, parent_menu):
		self.label_text = "Copy"
		self.command = self.copy
		
	def copy(self):
		print("Copying...")
	
if __name__ == "__main__":
	main()
