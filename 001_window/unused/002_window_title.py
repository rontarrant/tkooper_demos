import tkinter as tk

def main():
	window = Window()
	window.mainloop()


class Window(tk.Tk):
	title_text = "Hello, TkInter World!"
	
	def __init__(self):
		super().__init__()
		self.title(self.title_text)
		

if __name__ == "__main__":
	main()
