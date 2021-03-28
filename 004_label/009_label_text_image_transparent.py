from tkinter import *
from tkinter import ttk
import os

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Label Image Transparency"
		self.width = 353
		self.height = 270
		# configure
		self.config(width = self.width, height = self.height)
		self.title(self.title_text)
		self.grid_propagate(False) # without this, window size is ignored
		# populate
		mainframe = MainFrame(self)
		# centering
		mainframe.grid(column = 0, row = 0)
		mainframe.update()
		xbias = (self.winfo_width() - mainframe.winfo_width()) / 2
		mainframe.grid(padx = xbias)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.config(padding = "20 10 20 20")
		# populate
		label = HelloLabel(self)
		# layout
		label.grid(column = 0, row = 0)
		# centering


class HelloLabel(ttk.Label):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "A Label with Text and a Transparent Image"
		self.image = RelativeImagePath.get_path('images/head_transparent_bg.png')
		self.width = len(self.text)
		# configure
		self.rowconfigure(0, weight = 1)
		self.columnconfigure(0, weight = 1)
		self.config(text = self.text, image = self.image, compound = 'top')
		self.config(anchor = "center", width = self.width, background = "yellow", relief = "raised")

class RelativeImagePath:
	def get_path(file_name):
		current_directory = os.path.dirname(__file__)
		path = os.path.join(current_directory, file_name)
		relative_file_name = PhotoImage(file = path)

		return relative_file_name


if __name__ == "__main__":
	main()
