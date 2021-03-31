from tkinter import *
from relative import RelativePath

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Title-bar Icon"
		self.titlebar_image = RelativePath.get_image_path("images/airport_25.png")
		self.width = 250
		self.height = 200
		# configure
		self.iconphoto(False, self.titlebar_image)
		self.title(self.title_text)
		self.config(width = self.width, height = self.height)

if __name__ == "__main__":
	main()
