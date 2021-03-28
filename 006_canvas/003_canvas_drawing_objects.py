from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width = 400
		self.height = 400
		self.title_text = "Programatic Drawing on a Canvas"
		# configure
		self.config(width = self.width, height = self.height)
		self.title(self.title_text)
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		my_canvas = MyCanvas(self)
		# layout
		my_canvas.grid(column = 0, row = 0)

class MyCanvas(Canvas):
	def __init__(self, window):
		# object attributes
		self.width = 400
		self.height = 400
		self.bg = "white"
		# configure
		super().__init__(window, bg = self.bg, width = self.width, height = self.height)
		# layout
		self.grid()
		
		face = SmileyFace(self)

class SmileyFace():
	def __init__(self, canvas):
		# object attributes
		self.geometry = (50, 50, 350, 350)
		self.color = "yellow"
		# 
		self.draw(canvas)
		
	def draw(self, canvas):
		
		canvas.create_oval(self.geometry, fill = self.color)
		left_eye = LeftEye(canvas)
		right_eye = RightEye(canvas)
		mouth = Mouth(canvas)

class LeftEye():
	def __init__(self, canvas):
		self.geometry = (140, 100, 160, 130)
		self.curve_length = 180
		self.color = "black"
		canvas.create_oval(self.geometry, extent = self.curve_length, fill = self.color)

class RightEye():
	def __init__(self, canvas):
		self.geometry = (230, 100, 250, 130)
		self.curve_length = 180
		self.color = "black"
		canvas.create_oval(self.geometry, extent = self.curve_length, fill = self.color)

class Mouth():
	def __init__(self, canvas):
		self.create_arc((125, 150, 275, 290), width = 5, style = ARC, start = -20, extent = -140)
		self.width = 5
		self.draw(canvas)
	
	def draw(self, canvas):
		canvas.create_line(self.line_1, fill = self.color, width = self.width)
		canvas.create_line(self.line_2, fill = self.color, width = self.width)
		canvas.create_line(self.line_3, fill = self.color, width = self.width)


if __name__ == "__main__":
	main()
