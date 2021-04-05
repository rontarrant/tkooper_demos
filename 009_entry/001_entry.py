from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# configure
		self.grid_propagate(False) # otherwise, window has no size at all
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid()
		# populate
		string_entry = StringEntry(self)
		# layout
		string_entry.grid()

class StringEntry(ttk.Entry):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.string = StringVar()
		# configure
		

if __name__ == "__main__":
	main()
