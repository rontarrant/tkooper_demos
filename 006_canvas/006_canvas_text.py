from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.size = "400x400"
		self.title_text = "Empty Canvas"
		# configure
		self.geometry(self.size)
		self.title(self.title_text)
		# populate
		canvas = MyCanvas(self)

class MyCanvas(Canvas):
	def __init__(self, parent):
		super().__init__(parent)
		# class attributes
		self.width = 400
		self.height = 400
		self.bg = "white"
		# configure
		self.config(bg = self.bg, width = self.width, height = self.height)
		# populate
		sample_text = TextObject(self)
		# layout
		self.grid()

class TextObject():
	def __init__(self, canvas):
		# object attributes
		self.x = 200
		self.y = 200
		self.text_ = "A Simple Bit of Text"
		# configure
		canvas.create_text(self.x, self.y, text = self.text_)

if __name__ == "__main__":
	main()
