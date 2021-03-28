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
		self.title("Button Config Dictionary")
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
		dictionary_button = DictionaryButton(self)
		# layout
		dictionary_button.grid()

class DictionaryButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Print Config Dictionary"
		self.message = "Button things that can be configured:"
		# configure
		self.config(text = self.text, command = self.print_config_dictionary)

	def print_config_dictionary(self):
		print(self.message)
		self.print_config_list()
		
	def print_config_list(self):
		config_dict = self.config()
		
		for key, value_set in config_dict.items():
			print(f"{key} : {value_set}")

	
if __name__ == "__main__":
	main()
