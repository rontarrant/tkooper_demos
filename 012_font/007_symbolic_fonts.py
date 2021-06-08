# As can be seen when running this demo, all symbolic fonts in tkinter are the same on a single system.
# Therefore, I don't recommend using them if you're trying to be designerly.
from tkinter import *
from tkinter import ttk
from tkinter import font

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Set a Label's Font")
		self.width = 265
		self.height = 251
		# configure
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False) # without this, window size is determined by its contents and padding
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.font_list = ['TkDefaultFont',
								'TkTextFont',
								'TkTextFont',
								'TkFixedFont',
								'TkMenuFont',
								'TkHeadingFont',
								'TkCaptionFont',
								'TkSmallCaptionFont',
								'TkIconFont',
								'TkTooltipFont']
		self.labels = {}
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate & layout
		self.row = 0
		for font_ in self.font_list:
			self.labels[font_] = FontyLabel(self, font_)
			self.labels[font_].grid(column = 0, row = self.row)
			self.row += 1

class FontyLabel(ttk.Label):
	def __init__(self, parent, font_):
		super().__init__(parent)
		# object attributes
		#self.display_font = font.nametofont(font)
		self.text = "Use a Specific Font on a Label"
		self.width = len(self.text) + 3 # width is in characters
		# configure
		self.config(text = self.text, width = self.width)
		self.config(font = font.Font(family = font_), text = font_)


if __name__ == "__main__":
	main()
