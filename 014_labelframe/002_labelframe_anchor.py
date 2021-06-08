from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Labelframe Demo")
		# configure
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid()
		# populate
		southeast_labelframe = SEFrame(self)
		northeast_labelframe = NEFrame(self)
		southwest_labelframe = SWFrame(self)
		northwest_labelframe = NWFrame(self)
		# layout
		northwest_labelframe.grid(row = 0, column = 0, padx = 10, pady = 10)
		northeast_labelframe.grid(row = 0, column = 1, padx = 10, pady = 10)
		southwest_labelframe.grid(row = 1, column = 0, padx = 10, pady = 10)
		southeast_labelframe.grid(row = 1, column = 1, padx = 10, pady = 10)

class SEFrame(ttk.LabelFrame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "SE LabelFrame"
		# configure
		self.grid()
		self.config(text = self.text, labelanchor = 'se')
		# populate
		first_label = StringLabel(self, "Southeast Group")
		# layout
		first_label.grid(padx = 20, pady = 20)

class SWFrame(ttk.LabelFrame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "SW LabelFrame"
		# configure
		self.grid()
		self.config(text = self.text, labelanchor = 'sw')
		# populate
		first_label = StringLabel(self, "Southwest Group")
		# layout
		first_label.grid(padx = 20, pady = 20)

class NEFrame(ttk.LabelFrame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "NE LabelFrame"
		# configure
		self.grid()
		self.config(text = self.text, labelanchor = 'ne')
		# populate
		first_label = StringLabel(self, "Northeast Group")
		# layout
		first_label.grid(padx = 20, pady = 20)

class NWFrame(ttk.LabelFrame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "NW LabelFrame"
		# configure
		self.grid()
		self.config(text = self.text, labelanchor = 'nw')
		# populate
		first_label = StringLabel(self, "Northwest Group")
		# layout
		first_label.grid(padx = 20, pady = 20)

class StringLabel(ttk.Label):	
	def __init__(self, parent, text_):
		super().__init__(parent)
		# object attributes
		# configure
		self.config(text = text_)


if __name__ == "__main__":
	main()
