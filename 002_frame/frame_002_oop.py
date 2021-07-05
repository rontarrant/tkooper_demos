from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Frame OOP"
		self.size = "300x100"
		# configure
		self.grid_propagate(False) # otherwise, window has no size at all
		self.title(self.title_text)
		self.geometry(self.size)
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# layout
		self.grid()

if __name__ == "__main__":
	main()
