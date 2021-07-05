'''
This is a menu that can be placed not just in a menubar, but anywhere in a window.
It also has the distinction of not actually looking like a menu until it's clicked
which could lead to mistaking it for a Label.

Which is why there's also a dropdown menu arrow image stuffed in there. If nothing
else, it'll make the user curious as to why it's there and perhaps they'll click
on it.
'''
from tkinter import *
from tkinter import ttk
from functools import partial
from relative import RelativePath

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		windowing_system = self.tk.call('tk', 'windowingsystem') # ID the windowing system
		self.menubutton = MB_DropDownMenu(self)
		self.geometry_string = "200x100"
		# configure
		self.menubutton.grid()
		self.geometry(self.geometry_string)

class MB_DropDownMenu(Menubutton):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.label_text = "Fanciness"
		self.options = ["Colourful", "Greyscale", "Humdrum", "Downright Dull", "F'geddabouddit"]
		self.selected = StringVar()
		self.selected.set(self.options[0])
		self.menu = Menu(self, tearoff = False)
		self.copy_image = RelativePath.get_image_path("images/drop_down_arrow_10x06.png")
		# configure
		self.configure(text = "Options", image = self.copy_image, compound = 'right')
		
		for option in self.options:
			# Either of the following lines will populate the drop-down menu.
			#menu.add_command(label = option, command = lambda option = option: self.option_select(option))
			self.menu.add_command(label = option, command = partial(self.option_select, option))

		self.configure(menu = self.menu)


	def option_select(self, *args):
		self.selected.set(args[0])
		print(self.selected.get())
		

if __name__ == "__main__":
	main()
