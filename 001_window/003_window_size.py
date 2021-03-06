from tkinter import *

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Set Window Size"
		self.width: int = 265
		self.height: int = 165
		# configure
		self.title(self.title_text)
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False)
		
if __name__ == "__main__":
	main()
