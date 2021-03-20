from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("A Sized Frame, No Children")
		self.width = 450
		self.height = 300
		# configure
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False)
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.width: int = 400
		self.height: int = 250
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		self.config(width = self.width, height = self.height)
		self.config(borderwidth = 2, relief = "groove")
		# populate
		# layout

if __name__ == "__main__":
	main()
