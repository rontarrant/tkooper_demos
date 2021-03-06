import tkinter as tk

def main():
	window = Window()
	window.mainloop()
	
class Window(tk.Tk):
	def __init__(self):
		super().__init__()

if __name__ == "__main__":
	main()
