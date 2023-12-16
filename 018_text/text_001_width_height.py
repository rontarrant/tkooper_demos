from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Text Display Simple")
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
		text_display = TextDisplay(self)
		# layout

class TextDisplay(Text):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.width = 40 # characters
		self.height = 10 # character rows
		# configure
		self.config(width = self.width, height = self.height)
		self.grid()
		
if __name__ == "__main__":
	main()
