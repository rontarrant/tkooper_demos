from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.size = "200x300"
		# configure
		self.geometry(self.size)
		#populate
		mainframe = MainFrame(self)

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
