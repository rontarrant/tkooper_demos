from tkinter import *

def main():
	window = Window()
	window.mainloop()
	
class Window(Tk):
	def __init__(self):
		super().__init__()
		# object attributes
		self.title_text = "Config Dictionary"
		self.width = 275
		self.height = 200
		# configure
		self.title(self.title_text)
		self.config(width = self.width, height = self.height)
		# get list of attributes that can be config'ed
		self.print_config_list()
		
	def print_config_list(self):
		config_dict = self.config()
		
		for key, value_set in config_dict.items():
			print(f"{key} : {value_set}")


if __name__ == "__main__":
	main()

"""
config's attribute dictionary for tkinter.Tk (window):
{
	'bd': ('bd', '-borderwidth'),
	'borderwidth': ('borderwidth', 'borderWidth', 'BorderWidth', <string object: '0'>, 0),
	'class': ('class', 'class', 'Class', 'Toplevel', 'Tk'),
	'menu': ('menu', 'menu', 'Menu', '', ''),
	'relief': ('relief', 'relief', 'Relief', <string object: 'flat'>, 'flat'),
	'screen': ('screen', 'screen', 'Screen', '', ''),
	'use': ('use', 'use', 'Use', '', ''),
	'background': ('background', 'background', 'Background', <string object: 'SystemButtonFace'>, 'SystemButtonFace'),
	'bg': ('bg', '-background'),
	'colormap': ('colormap', 'colormap', 'Colormap', '', ''),
	'container': ('container', 'container', 'Container', 0, 0),
	'cursor': ('cursor', 'cursor', 'Cursor', '', ''),
	'height': ('height', 'height', 'Height', <string object: '0'>, 0),
	'highlightbackground': ('highlightbackground', 'highlightBackground', 'HighlightBackground', <string object: 'SystemButtonFace'>, 'SystemButtonFace'),
	'highlightcolor': ('highlightcolor', 'highlightColor', 'HighlightColor', <string object: 'SystemWindowFrame'>, 'SystemWindowFrame'),
	'highlightthickness': ('highlightthickness', 'highlightThickness', 'HighlightThickness', <string object: '0'>, 0),
	'padx': ('padx', 'padX', 'Pad', <string object: '0'>, <string object: '0'>),
	'pady': ('pady', 'padY', 'Pad', <string object: '0'>, <string object: '0'>),
	'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '0', '0'),
	'visual': ('visual', 'visual', 'Visual', '', ''),
	'width': ('width', 'width', 'Width', <string object: '0'>, 0)
}
"""