from tkinter import *

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width: int = 400
		self.height: int = 250
		self.x_pos: int = -200
		self.y_pos: int = 300
		self.size: str
		self.title_text = "Geometry from Variable-length Args"
		# configure
		self.size = self.set_geometry_string(self.width, self.height, self.x_pos, self.y_pos)
		self.geometry(self.size)
		self.title(self.title_text)
		
	def set_geometry_string(self, *args):
		'''Build a size and placement string from a variable-length argument list.
		The format will be: width+height<+/->x_pos<+/->y_pos.'''
		x_offset: str
		y_offset: str
		size_position: str
		
		# does the arg list include x and y window positions?
		if len(args) == 4:
			x_offset = self.sign(args[2])
			y_offset = self.sign(args[3])
			# get absolute values of x_pos & y_pos
			size_position = str(self.width) + "x" + str(self.height) + x_offset + str(args[2]) + y_offset + str(args[3])
		else:
			size_position = str(self.width) + "x" + str(self.height)
		
		return size_position

	def sign(self, value):
		'Find the sign of an x or y position and return the sign as a string.'
		offset_str: str
		
		if value < 0:
			offset_str = ""
		else:
			offset_str = "+"
		
		return offset_str
		
if __name__ == "__main__":
	main()
