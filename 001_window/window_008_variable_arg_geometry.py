from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width: int = 400
		self.height: int = 250
		self.x_pos: int = 200
		self.y_pos: int = -300
		self.size: str
		# configure
		# populate
		mainframe = MainFrame(self)
		
	def set_geometry_string(self, *args):
		'''
		Build a size and placement string from a variable-length argument list.
		The format will be: width+height<+/->x_pos<+/->y_pos.
		When x_pos is negative, x is offset from the right.
		When y_pos is negative, y is offset from the bottom.
		'''
		x_offset: str
		y_offset: str
		size_position: str

		x_offset = self.sign(self.x_pos)
		y_offset = self.sign(self.y_pos)
		print(f"self.x_pos: {self.x_pos}, self.y_pos: {self.y_pos}")
		print(f"x_offset: {x_offset}, y_offset: {y_offset}")
		size_position = str(self.width) + "x" + str(self.height) + x_offset + str(self.x_pos) + y_offset + str(self.y_pos)
		print(f"size_position: {size_position}")
		self.geometry(size_position)

	def sign(self, value):
		'''
		If either x or y is positive, a sign has to be added to make a properly-formatted
		geometry string. If one of these is negative, the string representation will
		include the '-' and so nothing needs to be added.
		'''
		'Find the sign of an x or y position and return the sign as a string.'
		offset_str: str
		
		if value < 0:
			offset_str = ""
		else:
			offset_str = "+"
		
		return offset_str

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		size_button = SizeButton(self)

class SizeButton(Button):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.text = "Set Size (Geometry)"
		# configure
		self.config(text = self.text, command = self.winfo_toplevel().set_geometry_string)
		self.grid()
		

if __name__ == "__main__":
	main()
