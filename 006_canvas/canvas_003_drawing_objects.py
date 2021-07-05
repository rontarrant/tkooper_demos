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
		# populate
		face = Face(self)
		left_eye = LeftEye(self)
		right_eye = RightEye(self)
		mouth = Mouth(self)
		# layout
		self.grid()

class Face():
	def __init__(self, canvas):
		# object attributes
		self.geometry = (50, 50, 350, 350)
		self.color = '#eccf43'
		self.outline = ''
		# configure
		self.draw(canvas)
		
	def draw(self, canvas):
		canvas.create_oval(self.geometry, fill = self.color, outline = self.outline)

class LeftEye():
	def __init__(self, canvas):
		self.geometry = (140, 100, 160, 130)
		self.curve_length = 180
		self.color = "black"
		self.draw(canvas)
	
	def draw(self, canvas):
		canvas.create_oval(self.geometry, fill = self.color)

class RightEye():
	def __init__(self, canvas):
		self.geometry = (230, 100, 250, 130)
		self.curve_length = 180
		self.color = "black"
		self.draw(canvas)
		
	def draw(self, canvas):
		canvas.create_oval(self.geometry, fill = self.color)

class Mouth():
	def __init__(self, canvas):
		self.geometry = (125, 150, 275, 290)
		self.width = 5
		self.style = ARC
		self.start = -20
		self.extent = -140
		self.draw(canvas)
	
	def draw(self, canvas):
		canvas.create_arc(self.geometry, width = 5, style = ARC, start = -20, extent = -140)
		self.width = 5


if __name__ == "__main__":
	main()
