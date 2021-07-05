from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width = 310
		self.height = 100
		# configure
		self.title("Basic Button with Callback")
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False)
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		hello_button = HelloButton(self)
		# layout
		hello_button.grid()

class HelloButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Say Hello"
		self.message = "Hello, tkinter World!"
		# configure
		self.config(text = self.text, command = self.say_hello)

	def say_hello(self):
		print(self.message)
	
if __name__ == "__main__":
	main()
