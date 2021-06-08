# Menus are handled a bit differently than other widgets.
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
		file_menu = FileMenu(self, window)
		edit_menu = EditMenu(self)
		# attach menus
		self.add_cascade(menu = file_menu, label = file_menu.label_text)
		self.add_cascade(menu = edit_menu, label = edit_menu.label_text)
		
class FileMenu(Menu):
	def __init__(self, menubar, window):
		super().__init__(menubar)
		# object attributes
		self.label_text = "File"
		# menu items
		file_new = "New"
		file_open = "Open"
		file_open_recent = "Open Recent"
		file_quit = "Quit"
		# populate
		self.add_command(label = file_new, command = NewFileCommand)
		self.add_command(label = file_open, command = OpenFileCommand)
		
		recent_submenu = SubMenu(self)
		self.add_cascade(label = file_open_recent, menu = recent_submenu) # NOTE: for a submenu, it's 'menu' NOT 'command'
		
		self.add_separator() # nothing extraordinary here
		
		self.add_command(label = file_quit, command = lambda: QuitCommand(window))

class SubMenu(Menu):
	def __init__(self, parent_menu):
		super().__init__(parent_menu)
		# object attributes
		recent_files = ["file1.py", "file2.py", "file3.py"]
		# populate
		for recent_file in recent_files:
			self.add_command(label = recent_file, command = lambda: OpenFileCommand(recent_file))
	
class NewFileCommand():
	def __init__(self):
		print("Creating a new file...")

class OpenFileCommand():
	def __init__(self, file = None):
		if (file == None):
			print("Opening a new file via dialog")
		else:
			print(f"Opening {file}...")

class QuitCommand():
	def __init__(self, window):
		print("doing clean-up...")
		# do clean up now
		print("done cleaning up")
		window.destroy()
	
class EditMenu(Menu):
	def __init__(self, menubar):
		super().__init__(menubar)
		# object attributes
		self.label_text = "Edit"
		# menu items
		edit_copy = "Copy"
		edit_cut = "Cut"
		edit_paste = "Paste"
		# populate
		self.add_command(label = edit_copy, command = EditCopyCommand)
		self.add_command(label = edit_cut, command = EditCutCommand)
		self.add_command(label = edit_paste, command = EditPasteCommand)
		
class EditCopyCommand():
	def __init__(self):
		print("Copying...")

class EditCutCommand():
	def __init__(self):
		print("Cutting...")

class EditPasteCommand():
	def __init__(self):
		print("Pasting...")


if __name__ == "__main__":
	main()
