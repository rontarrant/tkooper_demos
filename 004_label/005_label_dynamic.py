from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Button Binary Choices")
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.label_choices = ["Change Me with a Click", "Change Me Back"] # choices for label text
		self.changeable = StringVar()
		self.changeable.set(self.label_choices[0]) # set an initial value
		# configure
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		self.config(padding = "10 5 10 20")
		# populate
		changable_label = ChangableLabel(self)
		change_agent_button = ChangeAgentButton(self, changable_label)
		# layout
		changable_label.grid(row = 0, column = 0, padx = 10, pady = 10)
		change_agent_button.grid(row = 1, column = 0, padx = 10, pady = 10)

class ChangableLabel(ttk.Label):	
	def __init__(self, parent):
		super().__init__(parent)
		# configure
		self.config(textvariable = parent.changeable)

class ChangeAgentButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.text = "Make the Change"
		self.label = label
		self.changeable = parent.changeable
		self.label_choices = parent.label_choices
		# configure
		self.config(text = self.text, command = lambda:self.say_hello())

	def say_hello(self):
		if self.label.cget("text") == self.label_choices[0]:
			self.changeable.set(self.label_choices[1])
		else:
			self.changeable.set(self.label_choices[0])

if __name__ == "__main__":
	main()
