from tkinter import *

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "My Big Fat Window Title"
		# configure
		self.title(self.title_text)

if __name__ == "__main__":
	main()
