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
		self.columnconfigure(0, weight = 1)
		self.rowconfigure(0, weight = 1)
		# populate
		mainframe = MainFrame(self)

class MainFrame(Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid(column = 0, row = 0, sticky = (N, E, W, S))
		self.columnconfigure(0, weight = 1)
		self.rowconfigure(0, weight = 1)
		# populate
		text_display = TextDisplay(self)
		text_scrollbar = TextScrollbar(self, text_display)
		# layout
		text_display.grid(column = 0, row = 0, sticky = (N, E, W, S))
		text_scrollbar.grid(column = 1, row = 0, sticky = (N, S))

class TextDisplay(Text):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.width = 40 # characters
		self.height = 10 # character rows
		self.wrap = "word"
		# configure
		self.focus()
		self.config(width = self.width, height = self.height, wrap = self.wrap)
		self.tag_add("scene", "1.0", 'end')
		self.tag_configure("scene", foreground = "red")

class TextScrollbar(Scrollbar):
	def __init__(self, parent, widget):
		'''
		arg2 = pointer to the widget the scrollbar will control
		'''
		super().__init__(parent)
		# object attributes
		self.orientation = VERTICAL
		# configure
		self.config(command = widget.yview) # scrollbar to widget communication
		widget.config(yscrollcommand = self.set) # widget to scrollbar communications


if __name__ == "__main__":
	main()
