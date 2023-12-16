from tkinter import *
from tkinter import ttk
from relative import RelativePath

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Transparent Window")
		# configure
		self.wm_attributes('-alpha', 0.7)
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		message_label = MessageLabel(self)

class MessageLabel(ttk.Label):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "Everything transparent, even the titlebar."
		self.width = len(self.text) # width is in characters
		self.photo = RelativePath.get_image_path("images/example.png")
		# configure
		self.config(text = self.text, image = self.photo, compound = 'bottom', width = self.width)
		self.grid(column = 0, row = 0)


if __name__ == "__main__":
	main()
