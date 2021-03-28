from tkinter import *

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width: int = 300
		self.height: int = 230
		self.x_pos: int = 500
		self.y_pos: int = -100
		self.size: str
		self.title_text = "Specify Window Position"
		# configure
		self.size = self.set_size_position(self.width, self.height , self.x_pos, self.y_pos)
		self.geometry(self.size)
		self.title(self.title_text)
		
	def set_size_position(self, width: int, height: int, x_pos: int, y_pos: int):
		'''
		Build a size and placement string from integers.
		The output format will be: width+height<+/->x_pos<+/->y_pos
		'''
		x_offset: str
		y_offset: str
		size_position: str
		
		# If x_pos or y_pos is positive, we have to add a plus sign to the string.
		# If either is negative, the sign will be part of the string created by the conversion.
		if x_pos > 0:
			x_offset = "+"
		else:
			x_offset = ""
		
		if y_pos > 0:
			y_offset = "+"
		else:
			y_offset = ""
		
		# build the size and position string
		size_position = str(width) + "x" + str(height) + x_offset + str(x_pos) + y_offset + str(y_pos)
		
		return size_position
		
if __name__ == "__main__":
	main()
