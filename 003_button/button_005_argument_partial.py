from tkinter import *
from tkinter import ttk
from functools import partial

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
		self.grid_propagate(False)
		self.config(width = self.width, height = self.height)
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		hello_button = HelloButton(self)
		self.hello_label = HelloLabel(self)
		# layout
		hello_button.grid(column = 0, row = 0, sticky = (N, W, E, S))
		self.hello_label.grid(column = 0, row = 1, sticky = (N, E, W, S))
		
	def show_message(self, message):
		self.hello_label.update_(message)

class HelloButton(ttk.Button):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.text = "Say Hello"
		self.message = "Hello, tkinter World!"
		# configure
		self.config(text = self.text, command = partial(self.say_hello, self.message))

	def say_hello(self, message):
		master_name = self.winfo_parent()
		master = self._nametowidget(master_name)
		master.show_message(message)

class HelloLabel(ttk.Label):
	def __init__(self, parent):
		super().__init__(parent)
		#object attributes
		self.message = StringVar()
		# configure
		self.config(textvariable = self.message)
	
	def update_(self, message):
		self.message.set(message)
	
if __name__ == "__main__":
	main()
