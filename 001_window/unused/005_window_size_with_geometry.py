from tkinter import *

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Set Size with Geometry String"
		self.width: int = 330
		self.height: int = 200
		# configure
		self.title(self.title_text)
		self.geometry(str(self.width) + "x" + str(self.height))
		
if __name__ == "__main__":
	main()
