from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# configure
		self.title("Hello, Button!")
		#populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.width: int = 310
		self.height: int = 100
		# configure
		self.master.title('Override Content Sizing')
		self.grid()
		self.grid_propagate(False)
		self.config(width = self.width, height = self.height)
		# populate
		quit_button = QuitButton(self, window)
		# layout
		quit_button.grid(column = 1, row = 1)

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
