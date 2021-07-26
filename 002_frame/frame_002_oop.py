from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.mainframe = MainFrame(self)
		# configure

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.label = Label(self)
		# configure
		self.grid()

class Label(ttk.Label):
	def __init__(self, parent):
		super().__init__(parent, text = "This is a label inside a frame inside a window.")
		# object attributes
		# configure
		self.grid()
		
if __name__ == "__main__":
	main()
