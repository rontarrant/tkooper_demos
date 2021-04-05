from tkinter import *
from tkinter import ttk
import tkinter.font as font

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Label Font")
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
		self.text = "Changed the font to Times New Roman"
		self.width = len(self.text) # width is in characters
		label_font = font.Font(family = "Times New Roman", size = 12, weight = "normal")
		# configure
		self.config(anchor = "c", text = self.text, width = self.width, font = label_font)


if __name__ == "__main__":
	main()
