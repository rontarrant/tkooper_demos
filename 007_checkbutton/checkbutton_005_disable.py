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
		self.on = 1
		self.off = 0
		self.off_string = "Checkbutton is DISabled."
		self.on_string = "Checkbutton is ENabled."

		# config
		self.config(text = self.text, onvalue = self.on, offvalue = self.off, variable = self.var)
		self.config(command = lambda:self.update_(label))
		
	def update_(self, label):
		label.change_state(self.var.get())
		
	def state_(self):
		if self.instate(['disabled']):
			print(self.on_string)
			self.state(['!disabled'])
			#self.config(state = NORMAL)
		else:
			print(self.off_string)
			self.state(['disabled'])
			#self.config(state = DISABLED)
		
		print(self.state())

class MasterButton(ttk.Button):
	def __init__(self, frame, checkbutton):
		super().__init__(frame)
		# object attributes
		self.text = "Disable Checkbutton"
		# configure
		self.config(text = self.text, command = lambda:self.checkbutton_on_off(checkbutton))

	def checkbutton_on_off(self, checkbutton):
		checkbutton.state_()


if __name__ == "__main__":
	main()
