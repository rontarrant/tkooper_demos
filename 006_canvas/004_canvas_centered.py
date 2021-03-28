from tkinter import *
from tkinter import ttk
import os

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.size = "400x400"
		self.title_text = "Centered Canvas"
		# configure
		self.geometry(self.size)
		self.title(self.title_text)
		# populate
		canvas = MyCanvas(self)

class MyCanvas(Canvas):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.width = 300
		self.height = 300
		self.bg = "lightBlue1"
		# config
		self.place(relx = .125, rely = .1) # place canvas in window relative to upper-left corner as a fraction of window size (0.0 to 1.0)
		self.config(bg = self.bg, width = self.width, height = self.height)
		# populate
		self.create_rectangle(10, 10, 200, 100, fill='red')
		self.create_rectangle(50, 50, 250, 150, fill='green')
		self.create_rectangle(30, 80, 150, 120, width = 5, outline = '#800000', fill='')



if __name__ == "__main__":
	main()
