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
		# configure
		self.geometry(self.size)
		# populate
		canvas = MyCanvas(self)

class MyCanvas(Canvas):
	def __init__(self, parent):
		super().__init__(parent)
		# class attributes
		self.width = 400
		self.height = 400
		self.bg = "white"
		self.image = RelativeImagePath.get_path("images/arrow.png")
		# configure
		self.config(bg = self.bg, width = self.width, height = self.height)
		self.create_rectangle(10, 10, 200, 100, fill='red', outline = "")
		self.create_image(150, 120, image = self.image)
		self.grid()

class RelativeImagePath:
	def get_path(file_name):
		current_directory = os.path.dirname(__file__)
		path = os.path.join(current_directory, file_name)
		relative_file_name = PhotoImage(file = path)

		return relative_file_name


if __name__ == "__main__":
	main()
