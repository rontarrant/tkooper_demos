# Menus are handled a bit differently than other widgets.
# First, the default behaviour of tear-off menus needs to be suppressed (see: overrides section).
# Next, if you plan to do OS-specific layouts, you'll need to ID the windowing system (win32, x11, aqua)
# Then you need to create the Menubar (here done as a class derived from Menu), and
# finally, configure the window's menu option.
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# overrides
		self.option_add('*tearOff', FALSE) # override tear-off menus
		# object attributes
		windowing_system = self.tk.call('tk', 'windowingsystem') # ID the windowing system (for OS-specific menu layouts)
		self.menubar = Menubar(self)
		# configure
		self.config(menu = self.menubar)
		print(windowing_system)

class Menubar(Menu):
	def __init__(self, window):
		super().__init__(window)


if __name__ == "__main__":
	main()
