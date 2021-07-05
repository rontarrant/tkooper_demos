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
		self.images: dict = {} # A bug makes it necessary to keep an independent reference to any images placed on a canvas.
		# configure
		self.config(bg = self.bg, width = self.width, height = self.height)
		# populate
		rectangle_red = RectangleRed(self)
		arrow_image = ArrowImage(self)
		rectangle_blue = RectangleBlue(self)
		arrow_image = FaceImage(self)
		# layout
		self.grid()

class FaceImage():
	def __init__(self, canvas):
		# object attributes
		self.x = 88
		self.y = 173
		canvas.images['head'] = RelativePath.get_image_path("images/head.png") # extra reference workaround
		self.anchor = 'nw'
		# configure
		canvas.create_image(self.x, self.y, image = canvas.images['head'], anchor = self.anchor)

class ArrowImage():
	def __init__(self, canvas):
		# object attributes
		self.x = 118
		self.y = 79
		canvas.images['arrow'] = RelativePath.get_image_path("images/arrow.png")
		self.anchor = 'nw'
		# configure
		canvas.create_image(self.x, self.y, image = canvas.images['arrow'], anchor = self.anchor)

class RectangleBlue():
	def __init__(self, canvas):
		# object attributes
		self.start_x = 12
		self.start_y = 174
		self.end_x = 381
		self.end_y = 391
		self.fill_color = 'blue'
		self.outline_color = ''
		# configure
		canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y, fill = self.fill_color, outline = self.outline_color)

class RectangleRed():
	def __init__(self, canvas):
		# object attributes
		self.start_x = 10
		self.start_y = 10
		self.end_x = 200
		self.end_y = 100
		self.fill_color = 'red'
		self.outline_color = ''
		# configure
		canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y, fill = self.fill_color, outline = self.outline_color)

class RelativePath:
	def get_image_path(file_name):
		current_directory = os.path.dirname(__file__)
		path = os.path.join(current_directory, file_name)
		relative_file_name = PhotoImage(file = path)

		return relative_file_name


if __name__ == "__main__":
	main()
