from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.delay = 2000
		self.title("Dynamic 'Hello' Button")
		# populate
		mainframe = MainFrame(self)

	def delayed_close(self):
		self.after(self.delay, self.destroy)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# object atrributes
		# configure
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		self.config(padding = "10 5 10 20")
		# populate
		hello_label = HelloLabel(self)
		hello_button = HelloButton(self, hello_label)
		goodbye_button = GoodbyeButton(self, hello_label)
		# layout
		hello_label.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2)
		hello_button.grid(row = 1, column = 0, padx = 10, pady = 10)
		goodbye_button.grid(row = 1, column = 1, padx = 10, pady = 10)
		
class HelloLabel(ttk.Label):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.original_text = "Pick Your Choose"
		self.changeable = StringVar()
		self.hello_message = "Hello, Tkinter World!"
		self.good_bye_message = "Goodbye, World!\n (Closing in 2 seconds)"
		self.not_yet_message = "You have to say, 'hello' first."
		self.window = self.winfo_toplevel()
		# configure
		self.changeable.set(self.original_text)
		self.config(textvariable = self.changeable)
		
	def update_(self, arg: str):
		if arg == 'good-bye':
			if self.changeable.get() == self.original_text:
				self.changeable.set(self.not_yet_message)
			else:
				self.changeable.set(self.good_bye_message)
				self.window.delayed_close()
		elif arg == 'hello':
			self.changeable.set(self.hello_message)
		else:
			# do nothing
			pass

class GoodbyeButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.text = "Say Good-bye"
		# configure
		self.config(text = self.text, command = lambda:self.say_goodbye(label))
	
	def say_goodbye(self, label):
		label.update_('good-bye')

class HelloButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.text = "Say Hello"
		self.label = label
		# configure
		self.config(text = self.text, command = lambda:self.say_hello(label))

	def say_hello(self, label):
		label.update_('hello')

if __name__ == "__main__":
	main()
