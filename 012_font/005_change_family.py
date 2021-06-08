from tkinter import *
from tkinter import font as tkFont
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Step Through System Font List")
		self.width = 450
		self.height = 100
		# configure
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False) # without this, window size is determined by its contents and padding
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		fonty_label = FontyLabel(self)
		fonty_button = FontyButton(self, fonty_label)
		# layout
		fonty_button.grid(column = 0, row = 0)
		fonty_label.grid(column = 1, row = 0)

class FontyLabel(ttk.Label):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.fontfamilylist = list(tkFont.families())
		self.fontindex = 0
		self.fontStyle = tkFont.Font(family = self.fontfamilylist[self.fontindex])
		self.text = "Configuration with Style"
		self.width = len(self.text) # width is in characters
		# configure
		self.config(anchor = "c", text = self.text, width = self.width)
		self.config(text = self.fontfamilylist[self.fontindex], font = self.fontStyle)
		self.next_font()

	def next_font(self):
		self.fontindex = self.fontindex + 1

		if self.fontindex < len(self.fontfamilylist):
			current_font = (str(self.fontfamilylist[self.fontindex]), 12, "bold")
			self.configure(font = current_font, text = self.fontfamilylist[self.fontindex])

class FontyButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.text = "Change Font"
		self.label = label
		# configure
		self.config(text = self.text, command = label.next_font)

if __name__ == "__main__":
	main()
