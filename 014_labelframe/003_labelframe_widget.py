from tkinter import *
from tkinter import ttk
from tkinter import font
from relative import RelativePath

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Labelframe Image")
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
		northwest_labelframe = NWFrame(self)
		# layout
		northwest_labelframe.grid(row = 0, column = 0, padx = 10, pady = 10)

class NWFrame(ttk.LabelFrame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.widget = ImageLabel(self)
		# configure
		self.grid()
		self.config(labelanchor = 'nw', labelwidget = self.widget)
		# populate
		first_label = StringLabel(self, "Timer Group")
		# layout
		first_label.grid(padx = 20, pady = 20)

class ImageLabel(ttk.Label):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.image = RelativePath.get_image_path('./images/clock_40x40.png')
		# configure
		self.config(image = self.image)

class StringLabel(ttk.Label):	
	def __init__(self, parent, text_):
		super().__init__(parent)
		# object attributes
		# configure
		self.config(text = text_)


if __name__ == "__main__":
	main()
