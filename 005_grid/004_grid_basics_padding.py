from tkinter import *
from tkinter import ttk
import ast

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("A Simple Grid Layout")
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid(column = 0, row = 0)
		# populate
		simple_label_01 = SimpleLabel(self)
		simple_label_02 = SimpleLabel(self)
		simple_label_03 = SimpleLabel(self)
		simple_label_04 = SimpleLabel(self)
		simple_label_05 = SimpleLabel(self)
		simple_label_06 = SimpleLabel(self)
		# layout
		simple_label_01.grid(row = 0, column = 0, padx = 10, pady = 10)
		simple_label_02.grid(row = 1, column = 0, padx = 10, pady = 10)
		simple_label_03.grid(row = 2, column = 0, padx = 10, pady = 10)
		simple_label_04.grid(row = 0, column = 1, padx = 10, pady = 10)
		simple_label_05.grid(row = 1, column = 1, padx = 10, pady = 10)
		simple_label_06.grid(row = 2, column = 1, padx = 10, pady = 10)

class SimpleLabel(ttk.Label):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.original_text = "Simple Label"
		# configure
		self.config(text = self.original_text)
		self.configure(borderwidth = 5, relief = "ridge", anchor = 'c')


if __name__ == "__main__":
	main()
