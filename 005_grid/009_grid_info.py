from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Show Grid Contents & Info")
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		self.config(padding = "10 5 10 20")
		# populate
		information_label = HelloLabel(self)
		show_slaves_button = ShowSlavesButton(self, information_label)
		show_info_button = ShowInfoButton(self, information_label)
		# layout
		information_label.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2)
		show_slaves_button.grid(row = 1, column = 0, padx = 10, pady = 10)
		show_info_button.grid(row = 1, column = 1, padx = 10, pady = 10)

class HelloLabel(ttk.Label):	
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		self.original_text = "Click a button for more information about the grid."
		# configure

class ShowInfoButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.text = "Info about Inhabitants"
		# configure
		self.config(text = self.text, command = lambda:self.show_info(label, parent))
	
	def show_info(self, label, parent):
		for slave in parent.grid_slaves():
			print(slave)
			#print(slave.grid_info())
			
			for info in slave.grid_info():
				print(f"{info}, {slave.grid_info()[info]}")

			print() # blank line to separate items

class ShowSlavesButton(ttk.Button):
	def __init__(self, parent, label):
		super().__init__(parent)
		# object attributes
		self.text = "Grid Inhabitants"
		self.label = label
		# configure
		self.config(text = self.text, command = lambda:self.print_slaves(parent))

	def print_slaves(self, parent):
		print(parent.grid_slaves())
		
		for slave in parent.grid_slaves():
			print(slave)
		

if __name__ == "__main__":
	main()

'''
.!mainframe.!showinfobutton
{'in': <__main__.MainFrame object .!mainframe>, 'column': 1, 'row': 1, 'columnspan': 1, 'rowspan': 1, 'ipadx': 0, 'ipady': 0, 'padx': 10, 'pady': 10, 'sticky': ''}
.!mainframe.!showslavesbutton
{'in': <__main__.MainFrame object .!mainframe>, 'column': 0, 'row': 1, 'columnspan': 1, 'rowspan': 1, 'ipadx': 0, 'ipady': 0, 'padx': 10, 'pady': 10, 'sticky': ''}
.!mainframe.!hellolabel
{'in': <__main__.MainFrame object .!mainframe>, 'column': 0, 'row': 0, 'columnspan': 2, 'rowspan': 1, 'ipadx': 0, 'ipady': 0, 'padx': 10, 'pady': 10, 'sticky': ''}

'''

'''
another way to do it?

for item in widget.keys():
        print(item)
        print(widget.cget(item))
'''