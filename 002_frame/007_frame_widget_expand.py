from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# configure
		self.title("Expand Widget to Fill Cell")
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		self.columnconfigure(0, minsize = 106)
		self.columnconfigure(1, minsize = 106)
		self.columnconfigure(2, minsize = 106)
		self.rowconfigure(0, minsize = 40)
		self.rowconfigure(1, minsize = 40)
		self.rowconfigure(2, minsize = 50)
		# populate
		quit_button = QuitButton(self, window)
		# layout
		quit_button.grid(column = 1, row = 1, sticky = (N, W, E, S))

class QuitButton(ttk.Button):
	def __init__(self, parent, window):
		super().__init__(parent)
		# object attributes
		self.text = 'Quit'
		self.top_window = window
		# configure
		self.config(text = self.text, command = self.quit)

	def quit(self):
		self.top_window.quit()
		
if __name__ == "__main__":
	main()
