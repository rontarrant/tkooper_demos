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

		x_offset = self.sign(self.x_pos)
		y_offset = self.sign(self.y_pos)
		size_position = str(self.width) + "x" + str(self.height) + x_offset + str(self.x_pos) + y_offset + str(self.y_pos)
		self.geometry(size_position)
		self.update_idletasks()
		print(f"{self.geometry()}")

	def sign(self, value):
		offset_str: str
		
		if value < 0:
			offset_str = ""
		else:
			offset_str = "+"
		
		return offset_str

class MainFrame(Frame):
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
		self.config(text = self.text, command = self.winfo_toplevel().set_size_position)
		self.grid()
		

if __name__ == "__main__":
	main()
