# As the user types a string, a running report is written to the CLI.
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "String Entry"
		# configure
		self.title(self.title_text)
		self.grid_propagate(False)
		self.config(width = 260, height = 50)
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid()
		# populate
		labeled_entry = LabeledEntry(self)
		# layout
		labeled_entry.grid()
		
class LabeledEntry(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		# configure
		# populate
		string_entry = StringEntry(self)
		label = SimpleLabel(self)
		# layout
		label.grid(column = 0, row = 0, padx = 10, pady = 10)
		string_entry.grid(column = 1, row = 0, padx = 10, pady = 10)

class StringEntry(ttk.Entry):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.string = StringVar()
		# configure
		self.config(textvariable = self.string)
		self.bind('<Tab>', self.report)
		self.string.trace_add("write", self.per_key_change)
		
	def report(self, event): # two ways to fetch the Entry contents
		print(self.get())
		print(self.string.get())

	def per_key_change(self, *args):
		print(f"You typed a: {self.string.get()[-1]}")
		
class SimpleLabel(ttk.Label):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "Enter a String:"
		# configure
		self.config(text = self.text)


if __name__ == "__main__":
	main()
