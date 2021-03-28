from tkinter import *
from tkinter import ttk
from relative import RelativeImagePath

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Hello!")
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		image_button = ImageButton(self)
		# layout
		image_button.grid(row = 0, column = 0, sticky = 'e', padx = 2, pady = 2)

class ImageButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Say Hello"
		self.message = "Hello, Avatar!"
		self.image = RelativeImagePath.get_path("images/head.png")
		# configure
		self.config(text = self.text, command = self.say_hello, image = self.image, compound = 'top')

	def say_hello(self):
		print(self.message)


if __name__ == "__main__":
	main()
