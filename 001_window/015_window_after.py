from tkinter import *

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.width = 290
		self.height = 200
		self.title_text = "Report After 1 Second"
		# configure
		self.after(1000, self.report)
		self.config(width = self.width, height = self.height)
		self.title(self.title_text)
		
	def report(self):
		print("Reporting after 1000 ms.")

if __name__ == "__main__":
	main()
