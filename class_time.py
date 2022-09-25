import tkinter as tk
import time
import os

class Timer():
	def __init__(self):		#функция отрисовки объектов Tkinter
		self.window = tk.Tk()
		self.label = tk.Label(text = '')
		self.label.pack()
		self.update_clock()
		self.window.mainloop()
		
	def update_clock(self):
		now = time.strftime('%H:%M:%S')			#функия отрожающая текущее время которое в скобках
		now2 = time.strftime('%S')
		b = int(now2)
		if b // 2 == 0:
			print("QQ")
		self.label.config(text = now)
		self.window.after(1000, self.update_clock)
		os.system('cls')
		print(time.strftime('%H:%M:%S'))
		

timer = Timer()




