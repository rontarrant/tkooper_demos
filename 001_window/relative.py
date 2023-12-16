import os
from tkinter import *

class RelativePath:
	def get_image_path(file_name):
		current_directory = os.path.dirname(__file__)
		path = os.path.join(current_directory, file_name)
		image_handle = PhotoImage(file = path)

		return image_handle
