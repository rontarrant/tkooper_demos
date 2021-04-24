from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Simple Entry"
		# configure
		self.title(self.title_text)
		self.config(width = 270, height = 50)
		self.grid_propagate(False) # otherwise, window has no size at all
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid()
		# populate
		string_entry = StringEntry(self)
		# layout
		string_entry.grid(padx = 10, pady = 10)

class StringEntry(ttk.Entry):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.string = StringVar()
		# configure
		self.config(textvariable = self.string)
		self.bind('<Tab>', self.report) # binding a key
		
	def report(self, event): # two ways to fetch the Entry contents
		print(self.get())
		print(self.string.get())

if __name__ == "__main__":
	main()
