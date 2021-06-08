'''
This menu type, like the Menubutton type, can also be placed anywhere
in a window, but unlike Menubutton, it actually looks like something 
the user might click on and get a response.
In function, it's similar to a drop-down list used in other GUI toolkits
which is why the class derived from OptionMenu is named DropDownMenu.

Another thing to note here is that the call to super() must have three arguments:
the parent widget that contains it, the variable that contains the selected item,
and the list of items for the list. Instead of typing out the list item by item,
we've postponed that task using None so we can do the assignments later in a for
loop. It makes things cleaner. Now, adapting this demo for practical use will mean
simply changing self.options rather than doing all that splitting, etc.
'''
from tkinter import *
from tkinter import ttk
from functools import partial

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		windowing_system = self.tk.call('tk', 'windowingsystem') # ID the windowing system
		self.optionmenu = DropDownMenu(self)
		self.geometry_string = "200x100"
		# configure
		self.optionmenu.grid()
		self.geometry(self.geometry_string)

class DropDownMenu(OptionMenu):
	def __init__(self, window):
		# object attributes
		self.label_text = "File"
		self.options = ["Colourful", "Greyscale", "Humdrum", "Downright Dull", "F'geddabouddit"]
		self.selected = StringVar()
		self.selected.set(self.options[0])
		# configure
		super().__init__(window, self.selected, None)
		menu = self.children['menu']
		
		for option in self.options:
			# Either of the following lines will populate the drop-down menu.
			#menu.add_command(label = option, command = lambda option = option: self.option_select(option))
			menu.add_command(label = option, command = partial(self.option_select, option))

	def option_select(self, *args):
		self.selected.set(args[0])
		print(self.selected.get())
		

if __name__ == "__main__":
	main()
