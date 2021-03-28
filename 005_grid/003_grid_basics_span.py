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
		simple_label_01 = SimpleLabel(self, "A Very Simple Label Indeed")
		simple_label_02 = SimpleLabel(self)
		simple_label_03 = SimpleLabel(self)
		simple_label_04 = SimpleLabel(self)
		# layout
		simple_label_01.grid(row = 0, column = 0, columnspan = 2)
		simple_label_02.grid(row = 1, column = 1)
		simple_label_03.grid(row = 2, column = 2)

class SimpleLabel(ttk.Label):	
	def __init__(self, parent, text: str = 'A Simple Label'):
		super().__init__(parent)
		# object attributes
		self.original_text = text
		# configure
		self.config(text = self.original_text)
		self.configure(borderwidth = 5, relief = "ridge", anchor = 'c')


if __name__ == "__main__":
	main()
