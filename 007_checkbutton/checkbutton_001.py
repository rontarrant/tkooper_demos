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
	
	def change_state(self, state):
		if state == 1:
			self.changeable.set(self.on_text)
		else:
			self.changeable.set(self.off_text)

class FeatureCheckbutton(ttk.Checkbutton):
	def __init__(self, parent, label):
		super().__init__(parent)
		#object attributes
		self.text = "Feature"
		self.var = IntVar()
		# config
		self.config(text = self.text)
		self.config(onvalue = 1)
		self.config(offvalue = 0)
		self.config(variable = self.var)
		self.config(command = lambda:self.update(label))
		
	def update(self, label):
		label.change_state(self.var.get())


if __name__ == "__main__":
	main()
