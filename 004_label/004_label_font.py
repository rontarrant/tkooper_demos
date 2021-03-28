from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Label Configuration")
		self.width = 290
		self.height = 100
		# configure
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False) # without this, window size is determined by its contents and padding
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		hello_label = HelloLabel(self)
		# layout
		hello_label.grid(column = 0, row = 0)

class HelloLabel(ttk.Label):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "Configuration with Style"
		self.width = len(self.text) # width is in characters
		# configure
		self.config(anchor = "c", text = self.text, width = self.width)
		self.print_config_list()
		
	def print_config_list(self):
		config_dict = self.config()
		
		for key, value_set in config_dict.items():
			print(f"{key} : {value_set}")


if __name__ == "__main__":
	main()
