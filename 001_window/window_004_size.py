from tkinter import *

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width = 200
		self.height = 300
		# configure
		self.config(width = self.width, height = self.height)
		
if __name__ == "__main__":
	main()
