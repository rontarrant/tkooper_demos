from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("A Centered Frame, Designerly")
		self.width = 450
		self.height = 300
		# configure
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False)
		#self.rowconfigure(0, weight = 1)
		#self.columnconfigure(0, weight = 1)
		#populate
		mainframe = MainFrame(self)
		self.center_designerly(mainframe)
		
	def center_designerly(self, widget):
		# centering
		widget.grid(column = 0, row = 0)
		widget.update() # After the UI is drawn, winfo_ will have accurate dimensions.
		xbias = (self.winfo_width() - widget.winfo_width()) / 2
		ybias = (self.winfo_height() - widget.winfo_height()) / 2
		widget.grid(padx = xbias, pady = (ybias - 4, ybias))

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.width: int = 400
		self.height: int = 230
		# configure
		self.config(padding = "20 10 20 40")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		self.config(width = self.width, height = self.height)
		self.config(borderwidth = 2, relief = "groove")
		# populate
		# layout

if __name__ == "__main__":
	main()
