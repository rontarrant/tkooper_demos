from tkinter import *

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Set Border Width"
		self.width = 275
		self.height = 200
		# configure
		self.title(self.title_text)
		self.config(borderwidth = 3, relief = "raised", width = self.width, height = self.height)


if __name__ == "__main__":
	main()
