'''
The GTK philosophy is to allow the window manager to handle placement and sizing
of all windows as they're opened. However, not all window managers are capable
of such things. This is one of my pet peeves. I use a multi-monitor desktop
configuration and having to take the extra time and effort to place and size
a window after opening it is just annoying. I want it dealt with for me and
since we have these devices (computers) that can do all that for us, why not?

That's where this demo comes in. 
'''
from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width: int = 400
		self.height: int = 250
		self.x_pos: int = -200
		self.y_pos: int = 300
		self.title_text = "Geometry from Variable-length Args"
		self.size_position = StringVar()
		# configure
		self.set_geometry_string(self.width, self.height, self.x_pos, self.y_pos)
		self.geometry(self.size_position.get())
		self.title(self.title_text)
		self.grid_propagate(False)
		#populate
		mainframe = MainFrame(self)
		
	def set_geometry_string(self, *args):
		'''Build a size and placement string from a variable-length argument list.
		The format will be: width+height<+/->x_pos<+/->y_pos.'''
		x_offset: str
		y_offset: str
		
		# does the arg list include x and y window positions?
		if len(args) == 4:
			x_offset = self.sign(args[2])
			y_offset = self.sign(args[3])
			# get absolute values of x_pos & y_pos
			self.size_position.set(str(self.width) + "x" + str(self.height) + x_offset + str(args[2]) + y_offset + str(args[3]))
		else:
			self.size_position.set(str(self.width) + "x" + str(self.height))

	def get_geometry(self):
		print(f"can be grabbed directly from self.geometry(): {self.geometry()}")
		self.update_idletasks()
		print(f"or stored in a local variable and then printed: {self.size_position.get()}")
		
	def sign(self, value):
		'Find the sign of an x or y position and return the sign as a string.'
		offset_str: str
		
		if value < 0:
			offset_str = ""
		else:
			offset_str = "+"
		
		return offset_str

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid()
		# populate
		hello_button = HelloButton(self)
		# layout
		hello_button.grid()

class HelloButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.text = "Get Geometry"
		self.window = self.winfo_toplevel()
		# configure
		self.config(text = self.text, command = self.window.get_geometry)


if __name__ == "__main__":
	main()
