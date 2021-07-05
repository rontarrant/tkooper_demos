# The simplest form of a Combobox is a read-only list with no allowance for user input.
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
		self.config(width = 270, height = 100)
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
		thing_combobox = DynamicCombobox(self)
		# layout
		thing_combobox.grid(padx = 10, pady = 10)

class DynamicCombobox(ttk.Combobox):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.var = StringVar()
		self.value_list = ('something', 'something else', 'another thing', 'and finally')
		# configure
		self.config(textvariable = self.var, values = self.value_list)
		self.bind('<<ComboboxSelected>>', self.report) # note the double chevrons
		self.state(['readonly'])

	def report(self, event): # the event argument needs to be here, even though it's not enlightening (always x = 0, y = 0)
		print(f"event: {event}")
		print(self.var.get())


if __name__ == "__main__":
	main()
