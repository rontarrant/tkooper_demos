from tkinter import *
from tkinter import ttk
from tkinter import font

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Set a Label's Font")
		self.width = 265
		self.height = 100
		# configure
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False) # without this, window size is determined by its contents and padding
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		fonty_label = FontyLabel(self)
		# layout
		fonty_label.grid(column = 0, row = 0)

class FontyLabel(ttk.Label):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.display_font = font.Font(family = "Times New Roman")
		self.text = "Use a Specific Font on a Label"
		self.width = len(self.text) + 3 # width is in characters
		# configure
		self.config(text = self.text, width = self.width)
		self.config(font = self.display_font)


if __name__ == "__main__":
	main()
