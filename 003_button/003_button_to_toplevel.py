from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.delay = 2000 # 1000 = 1 second
		self.title("Dynamic 'Hello' Button")
		# populate
		mainframe = MainFrame(self)
	
	def delayed_exit(self):
		self.after(self.delay, self.destroy)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		self.config(padding = "10 5 10 20")
		# populate
		message_label = MessageLabel(self)
		goodbye_button = GoodbyeButton(self, message_label)
		# layout
		message_label.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2)
		goodbye_button.grid(row = 1, column = 1, padx = 10, pady = 10)

class MessageLabel(ttk.Label):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.hello_message = "Hello, World!"
		self.good_bye_message = "I'm outta here!\n (Closing in 2 seconds)"
		self.message = StringVar()
		# configure
		self.message.set(self.hello_message)
		self.config(textvariable = self.message)
		
	def update_(self):
		self.message.set(self.good_bye_message)
		self.winfo_toplevel().delayed_exit()

class GoodbyeButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.label_text = "Say Good-bye"
		self.label = label
		# configure
		self.config(text = self.label_text, command = self.say_goodbye)
	
	def say_goodbye(self):
		self.label.update_()


if __name__ == "__main__":
	main()
