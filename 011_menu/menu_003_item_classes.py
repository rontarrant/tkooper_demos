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
		self.add_cascade(menu = file_menu, label = file_menu.text)
		self.add_cascade(menu = edit_menu, label = edit_menu.text)
		print("Edit menu index: ", self.index("Edit"))

class FileMenu(Menu):
	text = "File"
	
	def __init__(self, menubar):
		super().__init__(menubar)
		## make items() an alias for self.index()
		## 
		items = self.index
		
		# New menu item
		new_item = NewItem(self)
		self.add_command(label = new_item.text)
		self.entryconfig(items(new_item.text), command = new_item.command)
		# Open menu item
		open_item = OpenItem(self)
		self.add_command(label = open_item.text)
		self.entryconfig(items(open_item.text), command = open_item.command)
		# Save menu item
		save_item = SaveItem(self)
		self.add_command(label = save_item.text)
		self.entryconfig(items(save_item.text), command = save_item.command)

class NewItem():
	def __init__(self, parent_menu):
		self.text = "New"
		self.command = self.do_action
		
	def do_action(self):
		print("Creating a new file...")

class OpenItem():
	def __init__(self, parent_menu):
		self.text = "Open"
		self.command = self.do_action
		
	def do_action(self):
		print("Opening a new file...")

class SaveItem():
	def __init__(self, parent_menu):
		self.text = "Save"
		self.command = self.do_action
		
	def do_action(self):
		print("Saving a file...")

class EditMenu(Menu):
	def __init__(self, menubar):
		super().__init__(menubar)
		# object attributes
		self.text = "Edit"
		# menu items
		copy_menu_item = CopyMenuItem(self)
		# populate
		self.add_command(label = copy_menu_item.text, command = copy_menu_item.command)

class CopyMenuItem():
	def __init__(self, parent_menu):
		self.text = "Copy"
		self.command = self.copy
		
	def copy(self):
		print("Copying...")
	
if __name__ == "__main__":
	main()
