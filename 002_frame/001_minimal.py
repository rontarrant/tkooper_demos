from tkinter import *
from tkinter import ttk

def main():
	app = MainFrame()
	app.mainloop()

class MainFrame(ttk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.width = 300
		self.height = 50
		# configure
		self.config(width = self.width, height = self.height)
		self.master.title('Frame without Window')
		self.config(borderwidth = 2, relief = "raised")
		self.grid()

		
if __name__ == "__main__":
	main()
