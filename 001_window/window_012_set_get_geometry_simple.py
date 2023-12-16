from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.size_position = "330x200+500-100"
		self.remember_size_position = ""
		# configure
		#populate
		mainframe = MainFrame(self)

	def set_geometry(self):
		self.geometry(self.size_position)
		print(f"{self.size_position}")
		self.update_idletasks()

	def get_geometry(self):
		self.remember_size_position = self.geometry()
		print(f"Grab geometry: {self.geometry()}")
		print(f"Store it locally: {self.remember_size_position}")
		
class MainFrame(Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		set_size_button = SetSizeButton(self)
		get_size_button = GetSizeButton(self)

class SetSizeButton(Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Set Geometry"
		# configure
		self.config(text = self.text, command = self.winfo_toplevel().set_geometry)
		self.grid()

class GetSizeButton(Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Get Geometry"
		# configure
		self.config(text = self.text, command = self.winfo_toplevel().get_geometry)
		self.grid()


if __name__ == "__main__":
	main()
