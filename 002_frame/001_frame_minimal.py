from tkinter import *
from tkinter import ttk

def main():
	app = MainFrame()
	app.mainloop()

class MainFrame(ttk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.grid()

		
if __name__ == "__main__":
	main()
