## You can size an empty window using config(), but really, what's the point?
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	width = 320
	height = 400
	
	def __init__(self):
		super().__init__()
		
		# object attributes
		
		# configure
		self.config(width = self.width, height = self.height)
		
		#populate


if __name__ == "__main__":
	main()
