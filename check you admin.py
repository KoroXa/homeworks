from tkinter import *
import random

root = Tk()
root.geometry('500x500')
money = 0	# b
price = 5	# c
coof = 0	# q
a = 0	#govno
def proc():
	global price, coof, money, a
	a = random.randint(2,3)
	price *= a
	lb4.configure(text = price)
	print(price)
	if money >= price:
		coof += 1
	
def click():
	global price, coof, money, a
	if money == 0: 
		money += 1
	else:
		money += price * coof
	print(money) 
	lb3.configure(text = money)



# resourse =========================================

lb1 = Label(text = 'money', font="Arial 20")
lb1.grid(row = 0, column = 0)

lb3 = Label(text = money, font="Arial 20")
lb3.grid(row = 0, column = 1)

lb2 = Label(text = 'цена', font="Arial 20")
lb2.grid(row = 0, column = 2)

lb4 = Label(text = price, font="Arial 20")
lb4.grid(row = 0, column = 3)

bt = Button(text = 'Прокачать', command = proc)
bt.grid(row = 1, column = 1)

bt2 = Button(text = 'Click', command = click)
bt2.grid(row = 1, column = 0)
# resourse =========================================

proc()



root.mainloop()
