## To get size-on-demand with children present,
## use geometry(). Just remember, it takes a string,
## not a pair of integers. You can also place the 
## window by passing in a string like this: 
##	"330x200+500+100" (width x height + x pos + y pos).
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	width = 320
	height = 400
	
	def __init__(self):
		super().__init__()
		
		# object attributes
		
		# configure
		self.geometry(str(self.width) + "x" + str(self.height))
		
		#populate
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
