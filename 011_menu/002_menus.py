# Menus are handled a bit differently than other widgets.
# They're also a departure from other toolkits.
# In the Menubar class, create the menus and attach them to the Menubar with:
# 0) add_cascade().
# The 'menu' parameter specifies which menu to add.
# For each Menu (cascade) three types of menu item can be added:
# 1) add_command(),
# 2) add_radiobutton(), or 
# 3) add_checkbutton().
# Each of these uses a 'command' parameter to assign its action.
# If adding a submenu, instead of a 'command,' we use the 'menu' parameter and add items
# using:
# 4) add_cascade().

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
		# object attributes
		file_menu = FileMenu(self)
		edit_menu = EditMenu(self)
		# populate
		self.add_cascade(menu = file_menu, label = file_menu.label_text)
		self.add_cascade(menu = edit_menu, label = edit_menu.label_text)

class FileMenu(Menu):
	def __init__(self, menubar):
		super().__init__(menubar)
		# object attributes
		self.label_text = "File"
		# configure
		self.add_command(label = "New", command = self.file_new)

	def file_new(self):
		print("Creating a new file...")
		
class EditMenu(Menu):
	def __init__(self, menubar):
		super().__init__(menubar)
		# object attributes
		self.label_text = "Edit"
		# configure
		self.add_command(label = "Copy", command = self.copy)
	
	def copy(self):
		print("Copying...")

if __name__ == "__main__":
	main()
