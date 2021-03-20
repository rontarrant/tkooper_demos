from tkinter import *

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()

if __name__ == "__main__":
	main()
