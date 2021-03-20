from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# configure
		self.title("Empty Window, Empty Frame")
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.width = 340
		self.height = 50
		# configure
		self.config(width = self.width, height = self.height, padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		self.config(borderwidth = 2, relief = "sunken")
		# populate
		# layout

if __name__ == "__main__":
	main()
