import tkinter as tk

def main():
	app = Application()
	app.mainloop()


class Application(tk.Tk):
	def __init__(self):
		super().__init__()


if __name__ == "__main__":
	main()
