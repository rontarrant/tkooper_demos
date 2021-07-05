from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width = 400
		self.height = 400
		self.title_text = "Programatic Drawing on a Canvas"
		# configure
		self.config(width = self.width, height = self.height)
		self.title(self.title_text)
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		my_canvas = MyCanvas(self)
		my_canvas.grid(column = 0, row = 0)

class MyCanvas(Canvas):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		# configure
		self.config(width = 400, height = 400, bg = "white")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# draw face
		self.draw()
	
	def draw(self):
		self.create_oval((50, 50, 350, 350), fill = '#eccf43', outline = "")
		# draw eyes
		self.create_oval((140, 100, 160, 130), fill = 'black')
		self.create_oval((230, 100, 250, 130), fill = 'black')
		# draw mouth
		self.create_arc((125, 150, 275, 290), width = 5, style = ARC, start = -20, extent = -140)


if __name__ == "__main__":
	main()
