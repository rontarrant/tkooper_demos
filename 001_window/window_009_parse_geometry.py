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
		self.x_pos: int = 500
		self.y_pos: int = -100
		self.size: str
		# configure
		# populate
		mainframe = MainFrame(self)
		
	def set_size_position(self):
		x_offset: str
		y_offset: str
		size_position: str

		if self.x_pos > 0:
			x_offset = "+"
		else:
			x_offset = ""
		
		if self.y_pos > 0:
			y_offset = "+"
		else:
			y_offset = ""
		
		size_position = str(self.width) + "x" + str(self.height) + x_offset + str(self.x_pos) + y_offset + str(self.y_pos)
		self.geometry(size_position)

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
		self.text = "Set Size and Position"
		# configure
		self.config(text = self.text, command = self.print_size)
		self.grid()
		
	def print_size(self):
		self.winfo_toplevel().set_size_position()

		print(f"width, height, x, y: {self.winfo_toplevel().winfo_geometry()}")


if __name__ == "__main__":
	main()
