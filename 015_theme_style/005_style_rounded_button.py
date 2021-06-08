from tkinter import *
from tkinter import ttk
import os

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Theme & Style")
		# configure
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid()
		# populate
		first_label = CommonLabel(self, "Some Label Text")
		rounded_button = RoundedButton(self)
		# layout
		first_label.grid(padx = 20, pady = 20)
		rounded_button.grid(padx = 20, pady = 20)

class RoundedStyle(ttk.Style):
	def __init__(self):
		super().__init__()
		# class attributes
		self.current_directory = os.path.dirname(__file__)
		self.rbutt_normal_path = os.path.join(self.current_directory, "images/rbutt_normal.png") # normal state image
		self.rbutt_normal = PhotoImage(file = self.rbutt_normal_path)
		self.rbutt_active_path = os.path.join(self.current_directory, "images/rbutt_active.png") # active state image
		self.rbutt_active = PhotoImage(file = self.rbutt_active_path)
		self.rbutt_pressed_path = os.path.join(self.current_directory, "images/rbutt_pressed.png") # pressed state image
		self.rbutt_pressed = PhotoImage(file = self.rbutt_pressed_path)
		# configure derivative styles
		self.element_create('Button.button', "image", self.rbutt_normal, ("pressed", self.rbutt_pressed), ("active", self.rbutt_active))
		
class CommonLabel(ttk.Label):	
	def __init__(self, parent, text_):
		super().__init__(parent)
		# object attributes
		# configure
		self.config(text = text_)

class RoundedButton(ttk.Button):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		self.style = RoundedStyle()
		self.text = "Hello"
		# configure
		self.config(text = self.text, command = self.do_something)

	def do_something(self):
		print("Hello, Rounded Button")

if __name__ == "__main__":
	main()
