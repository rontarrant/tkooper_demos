from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("A Simple Label")
		self.width = 260
		self.height = 100
		# configure
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False)
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		simple_label = SimpleLabel(self)
		# layout
		simple_label.grid()

class SimpleLabel(ttk.Label):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.text = "Definitely a Simple Label"
		# configure
		self.config(text = self.text)


if __name__ == "__main__":
	main()
