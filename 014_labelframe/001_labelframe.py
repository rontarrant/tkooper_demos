from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Labelframe Demo")
		# configure
		self.grid_propagate(False)
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		# configure
		self.grid()
		# populate
		first_labelframe = FirstFrame(self)
		# layout
		first_labelframe.grid(row = 0, column = 0)

class FirstFrame(ttk.LabelFrame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "First Frame"
		# configure
		self.grid()
		self.config(text = self.text)
		# populate
		changable_label = ChangableLabel(self)
		change_agent_button = ChangeAgentButton(self, changable_label)
		# layout
		changable_label.grid(row = 0, column = 0, padx = 10, pady = 10)
		change_agent_button.grid(row = 1, column = 0, padx = 10, pady = 10)

class ChangableLabel(ttk.Label):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.choices = ["Change Me with a Click", "Change Me Back"] # choices for label text
		self.changeable = StringVar()
		self.changeable.set(self.choices[0]) # set an initial value
		# configure
		self.config(textvariable = self.changeable)

	def action(self):
		if self.cget("text") == self.choices[0]:
			self.changeable.set(self.choices[1])
		else:
			self.changeable.set(self.choices[0])

class ChangeAgentButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.text = "Say Hello"
		# configure
		self.config(text = self.text, command = lambda:self.make_change(label))

	def make_change(self, label):
		label.action()
		
if __name__ == "__main__":
	main()
