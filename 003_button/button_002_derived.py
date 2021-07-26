from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		# configure
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		hello_button = HelloButton(self)
		goodbye_button = GoodbyeButton(self)

class Button(ttk.Button):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.text = "*******"
		self.message = "no message"
		# configure
		self.config(command = self.do_something)
		self.grid()

	def do_something(self):
		print(self.message)
		
class HelloButton(Button):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.text = "Say Hello"
		self.message = "Hello, tkinter World!"
		# configure
		self.config(text = self.text)

class GoodbyeButton(Button):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.text = "Say Good-bye"
		# configure
		self.config(text = self.text)
		
if __name__ == "__main__":
	main()
