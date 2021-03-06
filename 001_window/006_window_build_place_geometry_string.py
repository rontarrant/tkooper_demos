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
		self.y_pos: int = 100
		self.size: str
		self.title_text = "Specify Window Position"
		# configure
		self.size = self.set_size(self.width, self.height , self.x_pos, self.y_pos)
		self.geometry(self.size)
		self.title(self.title_text)
		
	def set_size(self, width: int, height: int, x_pos: int, y_pos: int):
		'Build a size and placement string'
		x_offset: str
		y_offset: str
		
		# check for left/right offset
		if x_pos < 0:
			x_offset = "-" # window position is offset from right
		else:
			x_offset = "+"
		
		# check for top/bottom offset
		if y_pos < 0:
			y_offset = "-" # window position is offset from bottom
		else:
			y_offset = "+"
		
		# get absolute values of x_pos & y_pos
		x_pos = abs(x_pos)
		y_pos = abs(y_pos)
		
		return str(self.width) + "x" + str(self.height) + x_offset + str(x_pos) + y_offset + str(y_pos)
		
if __name__ == "__main__":
	main()
