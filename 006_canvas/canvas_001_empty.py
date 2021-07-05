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
		self.grid()


if __name__ == "__main__":
	main()
