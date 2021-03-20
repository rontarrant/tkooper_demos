from tkinter import *

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Build a Geometry String from Integers"
		self.width: int = 375
		self.height: int = 220
		self.size: str
		# configure
		self.size = self.set_size(self.width, self.height)
		self.geometry(self.size)
		self.title(self.title_text)
		
	def set_size(self, width: int, height: int): # build size string
		return str(self.width) + "x" + str(self.height)
		
if __name__ == "__main__":
	main()
