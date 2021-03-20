from tkinter import *
from tkinter import ttk
from quit_button import QuitButton

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Sticky Widgets"
		self.width = 300
		self.height = 300
		# configure
		#self.grid_propagate(False)
		self.config(width = self.width, height = self.height)
		self.title(self.title_text)
		#populate
		mainframe = MainFrame(self)
		

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		self.columnconfigure(0, minsize = 100)
		self.columnconfigure(1, minsize = 100)
		self.columnconfigure(2, minsize = 100)
		self.rowconfigure(0, minsize = 40)
		self.rowconfigure(1, minsize = 40)
		self.rowconfigure(2, minsize = 50)
		# populate
		quit_button1 = QuitButton(self, window)
		quit_button2 = QuitButton(self, window)
		quit_button3 = QuitButton(self, window)
		quit_button4 = QuitButton(self, window)
		quit_button5 = QuitButton(self, window)
		quit_button6 = QuitButton(self, window)
		quit_button7 = QuitButton(self, window)
		quit_button8 = QuitButton(self, window)
		quit_button9 = QuitButton(self, window)
		# layout
		quit_button1.grid(column = 0, row = 0, sticky = (S, E))
		quit_button2.grid(column = 1, row = 0, sticky = S)
		quit_button3.grid(column = 2, row = 0, sticky = (S, W))
		quit_button4.grid(column = 0, row = 1, sticky = E)
		quit_button5.grid(column = 1, row = 1, sticky = (N, W, E, S))
		quit_button6.grid(column = 2, row = 1, sticky = W)
		quit_button7.grid(column = 0, row = 2, sticky = (N, E))
		quit_button8.grid(column = 1, row = 2, sticky = N)
		quit_button9.grid(column = 2, row = 2, sticky = (N, W))
		
if __name__ == "__main__":
	main()
