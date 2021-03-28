from tkinter import *
from tkinter import ttk
import os

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
		hello_button = HelloButton(self)
		# layout
		hello_button.grid(row = 0, column = 0, sticky = 'e', padx = 2, pady = 2)

class HelloButton(ttk.Button):
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

class RelativeImagePath:
	def get_path(file_name):
		current_directory = os.path.dirname(__file__)
		path = os.path.join(current_directory, file_name)
		relative_file_name = PhotoImage(file = path)

		return relative_file_name

if __name__ == "__main__":
	main()
