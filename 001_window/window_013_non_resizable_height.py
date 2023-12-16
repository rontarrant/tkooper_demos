from tkinter import *

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Non-resizable Width"
		self.width = 300
		self.height = 200
		# configure
		self.resizable(width = True, height = False)
		self.config(width = self.width, height = self.height)
		self.title(self.title_text)
		
if __name__ == "__main__":
	main()
