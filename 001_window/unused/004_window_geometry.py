import tkinter as tk

def main():
	window = Window()
	window.mainloop()
	
class Window(tk.Tk):
	title_text = "Hello, TkInter World!"
	width: int = 400
	height: int = 250

	
	def __init__(self):
		super().__init__()
		self.title(self.title_text)
		self.geometry(str(self.width) + "x" + str(self.height))
		
if __name__ == "__main__":
	main()
