from tkinter import *
from tkinter import ttk
from relative import RelativePath

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		windowing_system = self.tk.call('tk', 'windowingsystem') # ID the windowing system
		self.option_add('*tearOff', FALSE) # must be set BEFORE any menus are created
		self.actions = Actions()
		self.menubar = Menubar(self)
		# configure
		self.config(menu = self.menubar)
		self.bind('<Control_L><c>', self.actions.copy_stuff)
		self.bind('<Control_L><x>', self.actions.cut_stuff)
		self.bind('<Control_L><p>', self.actions.paste_stuff)

class Menubar(Menu):
	def __init__(self, window):
		super().__init__(window)
		# menus
		self.edit_menu = EditMenu(self, window)
		# attach menus
		self.add_cascade(menu = self.edit_menu, label = self.edit_menu.label_text)

class EditMenu(Menu):
	def __init__(self, menubar, window):
		super().__init__(menubar)
		# object attributes
		self.label_text = "Edit"
		self.actions = window.actions
		self.copy_image = RelativePath.get_image_path("images/copy_16x16.png")
		self.cut_image = RelativePath.get_image_path("images/cut_16x16.png")
		self.paste_image = RelativePath.get_image_path("images/paste_16x16.png")
		# populate
		self.add_command(label = "Copy", command = self.actions.copy_stuff, accelerator = "(Ctrl-C)", image = self.copy_image, compound = 'left')
		self.add_command(label = "Cut", command = self.actions.cut_stuff, accelerator = "(Ctrl-X)", image = self.cut_image, compound = 'left')
		self.add_command(label = "Paste", command = self.actions.paste_stuff, accelerator = "(Ctrl-P)", image = self.paste_image, compound = 'left')

class Actions():
	def copy_stuff(self, event = None):
		print("Copying stuff.")

	def cut_stuff(self, event = None):
		print("Cutting stuff.")

	def paste_stuff(self, event = None):
		print("Pasting stuff.")


if __name__ == "__main__":
	main()
