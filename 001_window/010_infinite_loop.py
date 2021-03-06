from tkinter import *

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Repeat After Me"
		self.width = 260
		self.height = 200
		# configure
		self.title(self.title_text)
		self.after(1000, self.report)
		self.config(width = self.width, height = self.height)

	def report(self):
		print("Reporting after 1000 ms.")
		self.after(1000, self.report)


if __name__ == "__main__":
	main()
