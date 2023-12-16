from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width: int = 330
		self.height: int = 200
		# configure
		self.geometry(f"{self.width}x{self.height}")
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		size_button = SizeButton(self)

class SizeButton(Button):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.text = "Print Size"
		# configure
		self.config(text = self.text, command = self.print_size)
		self.grid()
		
	def print_size(self):
		print(f"width: {self.winfo_toplevel().winfo_width()}")
		print(f"height: {self.winfo_toplevel().winfo_height()}")

if __name__ == "__main__":
	main()
