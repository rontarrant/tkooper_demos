from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Frame Sized"
		# configure
		self.title(self.title_text)
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.width = 250
		self.height = 100
		# configure
		self.config(width = self.width, height = self.height)
		self.grid()
		# populate
		# layout

if __name__ == "__main__":
	main()
