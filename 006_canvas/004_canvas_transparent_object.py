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
		self.title_text = "Canvas with Transparent Object"
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
		red_rectangle = RectangleRedOne(self)
		green_rectangle = RectangleGreenTwo(self)
		hollow_rectangle = RectangleHollow(self)

class RectangleRedOne():
	def __init__(self, canvas):
		# object attributes
		self.start_x = 10
		self.start_y = 10
		self.end_x = 200
		self.end_y = 100
		self.fill_color = 'red'
		# configure
		canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y, fill = self.fill_color)

class RectangleGreenTwo():
	def __init__(self, canvas):
		self.start_x = 50
		self.start_y = 50
		self.end_x = 250
		self.end_y = 150
		self.fill_color = 'green'
		# configure
		canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y, fill = self.fill_color)
	
class RectangleHollow():
	def __init__(self, canvas):
		self.start_x = 30
		self.start_y = 80
		self.end_x = 150
		self.end_y = 120
		self.fill_color = ''
		self.width = 5
		self.outline_color = '#800000'
		# configure
		canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y, fill = self.fill_color, width = self.width, outline = self.outline_color)
		

if __name__ == "__main__":
	main()
