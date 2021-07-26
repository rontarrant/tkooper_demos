from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Geometry Set/Get Simple"
		self.size_position_string = "400x250+200+300"
		self.size_position = StringVar()
		self.size_position.set(self.size_position_string)
		# configure
		self.geometry(self.size_position.get())
		self.title(self.title_text)
		#populate
		mainframe = MainFrame(self)
		
	def get_geometry(self):
		print(f"can be grabbed directly from self.geometry(): {self.geometry()}")
		self.size_position_string = self.geometry()
		self.size_position.set(self.size_position_string)
		print(f"then stored in an object attribute (self.size_position): {self.size_position.get()}")
		
class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		hello_button = HelloButton(self)

class HelloButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Get Geometry"
		self.window = self.winfo_toplevel()
		# configure
		self.config(text = self.text, command = self.window.get_geometry)
		self.grid()


if __name__ == "__main__":
	main()
