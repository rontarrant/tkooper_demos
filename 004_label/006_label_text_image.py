from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Label Text & Image"
		self.width = 318
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
		self.grid()
		# populate
		hello_label = HelloLabel(self)
		# layout
		hello_label.grid()

class HelloLabel(ttk.Label):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "A Label with Text and an Image"
		self.image = PhotoImage(file = './images/head.png')
		self.grid(column = 0, row = 0)
		self.rowconfigure(0, weight = 1)
		self.columnconfigure(0, weight = 1)
		self.config(padding = "20 10 20 20")
		# configure
		self.config(text = self.text, image = self.image, compound = 'top')


if __name__ == "__main__":
	main()
