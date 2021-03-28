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
		master_button = MasterButton(self, feature_checkbutton)
		# layout
		state_label.grid(row = 0, column = 0, padx = 10, pady = 10)
		feature_checkbutton.grid(row = 1, column = 0, padx = 10, pady = 10)
		master_button.grid(row = 2, column = 0, padx = 10, pady = 10)

class StateLabel(ttk.Label):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.off_text = "Feature is OFF"
		self.on_text = "Feature is ON"
		self.disabled_text = "Feature is DISABLED"
		self.changeable = StringVar()
		self.changeable.set(self.off_text)
		# configure
		self.config(textvariable = self.changeable)

class FeatureCheckbutton(ttk.Checkbutton):
	def __init__(self, parent, label):
		super().__init__(parent)
		#object attributes
		self.text = "Feature"
		self.var = IntVar()
		self.on = 1
		self.off = 0
		# config
		self.config(text = self.text, onvalue = self.on, offvalue = self.off, variable = self.var)
		self.config(command = lambda:self.report(label))
		
	def report(self, label):
		if self.var.get() == 1:
			label.changeable.set(label.on_text)
		else:
			label.changeable.set(label.off_text)


class MasterButton(ttk.Button):
	def __init__(self, frame, checkbutton):
		super().__init__(frame)
		# object attributes
		self.text = "Disable Checkbutton"
		self.cb_off = "Checkbutton is DISabled."
		self.cb_on = "Checkbutton is ENabled."
		self.controlled_button = checkbutton
		# configure
		self.config(text = self.text, command = self.disable_checkbutton)

	def disable_checkbutton(self):
		if self.controlled_button.state(['disabled']):
			self.controlled_button.config(state = DISABLED)
			print(self.cb_off)
		else:
			self.controlled_button.config(state = NORMAL)
			print(self.cb_on)


if __name__ == "__main__":
	main()
