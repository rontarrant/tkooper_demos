from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Label with Colour"
		self.size = "200x75"
		# configure
		self.title(self.title_text)
		self.geometry(self.size)
		self.grid_propagate(False)
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		hello_label = HelloLabel(self)
		# layout
		hello_label.grid()

class HelloLabel(ttk.Label):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "A Label with Colour"
		self.width = len(self.text) + 5 # width is in characters
		# configure
		self.config(anchor = "c", background = "blue", foreground = "yellow", text = self.text, width = self.width)


if __name__ == "__main__":
	main()
