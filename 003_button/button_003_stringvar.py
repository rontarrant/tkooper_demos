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
		# configure
		self.grid()
		# populate
		changable_label = ChangableLabel(self)
		change_agent_button = ChangeAgentButton(self, changable_label)
		# layout
		changable_label.grid(row = 0, column = 0)
		change_agent_button.grid(row = 1, column = 0)

class ChangableLabel(ttk.Label):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.choices = ["Change Me with a Click", "Change Me Back"] # choices for label text
		self.changeable = StringVar()
		self.changeable.set(self.choices[0]) # set an initial value
		# configure
		self.config(textvariable = self.changeable)
		
	def update(self):
		if self.cget("text") == self.choices[0]:
			self.changeable.set(self.choices[1])
		else:
			self.changeable.set(self.choices[0])

class ChangeAgentButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.text = "Say Hello"
		self.label = label
		# configure
		self.config(text = self.text, command = self.say_hello)

	def say_hello(self):
		self.label.update()

if __name__ == "__main__":
	main()
