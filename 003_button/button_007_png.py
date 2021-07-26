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
		self.title("Hello, Button!")
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		hello_button = HelloButton(self)

class HelloButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Say Hello"
		self.message = "Hello, tkinter World!"
		self.current_directory = os.path.dirname(__file__)
		self.image_path = os.path.join(self.current_directory, "images/head.png")
		self.image = PhotoImage(file = self.image_path)
		# configure
		self.config(text = self.text, command = self.say_hello, image = self.image, compound = 'top')
		self.grid(row = 0, column = 0, sticky = 'e', padx = 2, pady = 2)

	def say_hello(self):
		print(self.message)


if __name__ == "__main__":
	main()
