## Reveal all options for the Button class.
## NOTE: For this to work, Button must be instantiated.
from tkinter import *
from tkinter import ttk

## option values in order:
## - option name,
## - name of the option in the option database,
## - Class,
## - default value,
## - current value.

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

class HelloButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Say Hello"
		self.message = "Hello, tkinter World!"
		# configure
		self.grid()
		self.config(text = self.text, command = self.show_options)

	def show_options(self):
		option_values = ["name", "database name", "class", "default value", "current value"]

		config_options = self.configure()

		for key, value in config_options.items():
			print(f"Key: {key}")
			for i in range(5):
				print(option_values[i], ": ", value[i])
			print("\n")
	
if __name__ == "__main__":
	main()
