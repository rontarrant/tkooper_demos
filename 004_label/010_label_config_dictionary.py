from tkinter import *
from tkinter import ttk

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title("Configuration")
		self.width = 290
		self.height = 100
		# configure
		self.config(width = self.width, height = self.height)
		self.grid_propagate(False) # without this, window size is determined by its contents and padding
		# populate
		mainframe = MainFrame(self)

class MainFrame(ttk.Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.config(padding = "20 10 20 20")
		self.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# populate
		hello_label = SimpleLabel(self)
		# layout
		hello_label.grid(column = 0, row = 0)

class SimpleLabel(ttk.Label):
	def __init__(self, window):
		super().__init__(window)
		# object attributes
		self.text = "Print the Label Configuration Dictionary"
		self.width = len(self.text) # width is in characters
		# configure
		self.config(anchor = "center", text = self.text, width = self.width, background = "yellow", foreground = "blue", relief = "raised")
		self.print_config_list()
		
	def print_config_list(self):
		config_dict = self.config()
		
		for key, value_set in config_dict.items():
			print(f"{key} : {value_set}")


if __name__ == "__main__":
	main()

'''
background : ('background', 'frameColor', 'FrameColor', '', <string object: 'yellow'>)
foreground : ('foreground', 'textColor', 'TextColor', '', <string object: 'blue'>)
font : ('font', 'font', 'Font', '', '')
borderwidth : ('borderwidth', 'borderWidth', 'BorderWidth', '', '')
relief : ('relief', 'relief', 'Relief', '', <string object: 'raised'>)
anchor : ('anchor', 'anchor', 'Anchor', '', <string object: 'center'>)
justify : ('justify', 'justify', 'Justify', '', '')
wraplength : ('wraplength', 'wrapLength', 'WrapLength', '', '')
takefocus : ('takefocus', 'takeFocus', 'TakeFocus', '', '')
text : ('text', 'text', 'Text', '', 'Print the Label Configuration Dictionary')
textvariable : ('textvariable', 'textVariable', 'Variable', '', '')
underline : ('underline', 'underline', 'Underline', -1, -1)
width : ('width', 'width', 'Width', '', 40)
image : ('image', 'image', 'Image', '', '')
compound : ('compound', 'compound', 'Compound', <string object: 'none'>, <string object: 'none'>)
padding : ('padding', 'padding', 'Pad', '', '')
state : ('state', 'state', 'State', <string object: 'normal'>, <string object: 'normal'>)
cursor : ('cursor', 'cursor', 'Cursor', '', '')
style : ('style', 'style', 'Style', '', '')
class : ('class', '', '', '', '')
'''
