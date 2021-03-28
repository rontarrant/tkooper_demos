from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Checkbutton OOP")
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		self.config(padding = "10 5 10 20")
		# populate
		state_label = StateLabel(self)
		feature_checkbutton = FeatureCheckbutton(self, state_label)
		# layout
		state_label.grid(row = 0, column = 0, padx = 10, pady = 10)
		feature_checkbutton.grid(row = 1, column = 0, padx = 10, pady = 10)

class StateLabel(ttk.Label):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.off_text = "Feature is OFF"
		self.on_text = "Feature is ON"
		self.changeable = StringVar()
		self.changeable.set(self.off_text)
		# configure
		self.config(textvariable = self.changeable)

class FeatureCheckbutton(ttk.Checkbutton):
	def __init__(self, parent, label):
		super().__init__(parent)
		#object attributes
		self.text = "Feature"
		self.var = StringVar()
		self.on = "FeatureCheckButton is ON"
		self.off = "FeatureCheckButton is OFF"
		# config
		self.config(text = self.text, onvalue = self.on, offvalue = self.off, variable = self.var, command = lambda:self.report(label))
		
	def report(self, label):
		if self.var.get() == self.on:
			label.changeable.set(label.on_text + "\n" + self.var.get())
		else:
			label.changeable.set(label.off_text + "\n" + self.var.get())


if __name__ == "__main__":
	main()
