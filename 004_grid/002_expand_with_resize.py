from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width = 350
		self.height = 160
		# configure
		self.title("Expand Children as Window Resizes")
		self.config(width = self.width, height = self.height)
		self.rowconfigure(0, weight = 1)
		self.columnconfigure(0, weight = 1)
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid(sticky = (N, W, E, S))
		self.columnconfigure(0, minsize = 60, weight = 1)
		self.columnconfigure(1, minsize = 220, weight = 1)
		self.columnconfigure(2, minsize = 60, weight = 1)
		self.rowconfigure(0, minsize = 40, weight = 1)
		self.rowconfigure(1, minsize = 40, weight = 1)
		self.rowconfigure(2, minsize = 50, weight = 1)
		# populate
		place_holder_01 = PlaceHolderFrame(self)
		place_holder_02 = PlaceHolderFrame(self)
		place_holder_03 = PlaceHolderFrame(self)
		place_holder_04 = PlaceHolderFrame(self)
		quit_button = QuitButton(self, window)
		place_holder_05 = PlaceHolderFrame(self)
		place_holder_06 = PlaceHolderFrame(self)
		place_holder_07 = PlaceHolderFrame(self)
		place_holder_08 = PlaceHolderFrame(self)
		# layout
		place_holder_01.grid(column = 0, row = 0, sticky = (N, W, E, S))
		place_holder_02.grid(column = 1, row = 0, sticky = (N, W, E, S))
		place_holder_03.grid(column = 2, row = 0, sticky = (N, W, E, S))
		place_holder_04.grid(column = 0, row = 1, sticky = (N, W, E, S))
		quit_button.grid(column = 1, row = 1, sticky = (N, W, E, S))
		place_holder_05.grid(column = 2, row = 1, sticky = (N, W, E, S))
		place_holder_06.grid(column = 0, row = 2, sticky = (N, W, E, S))
		place_holder_07.grid(column = 1, row = 2, sticky = (N, W, E, S))
		place_holder_08.grid(column = 2, row = 2, sticky = (N, W, E, S))

class PlaceHolderFrame(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		# configure
		self.configure(borderwidth = 5, relief = "ridge")
		self.rowconfigure(0, weight = 1)
		self.columnconfigure(0, weight = 1)
	
class QuitButton(ttk.Button):
	def __init__(self, parent, window):
		super().__init__(parent)
		# object attributes
		self.text = 'Quit'
		self.top_window = window
		# configure
		self.config(text = self.text, command = self.quit)

	def quit(self):
		# do someting
		self.top_window.quit()
		
if __name__ == "__main__":
	main()
