'''
If the Frame size (content) is to override the Window size (container),
the Window geometry has to be set using self.config(width, height). If,
instead, it's set using self.geometry(), grid_propagate() has no effect.
The Window's size will always be that set by self.geometry().

To obtain a proof, comment out self.geometry(self.size). The window will
use the Frame's size. Uncomment it, and the Window's size will be used.

Take-away:
Which approach you take to sizing a window will depend on whether you want
the option of overriding the size later with a minimum of fuss. 
'''
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.size = "250x100"
		self.width = 250
		self.height = 100
		# configure
		self.geometry(self.size) # This cannot be overridden, even by self.config().
		self.config(width = self.width, height = self.height) # But these (width, height) can.
		#populate
		mainframe = MainFrame(self)
		self.print_size()
	
	def print_size(self):
		self.update_idletasks()
		print(self.geometry())

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.width = 450
		self.height = 300
		# configure
		self.config(width = self.width, height = self.height)
		self.grid()
		# populate
		# layout

if __name__ == "__main__":
	main()
