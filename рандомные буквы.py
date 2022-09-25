import random, colorama
a = ["1","2","3","4","5","6","7","8","9","0"]

from colorama import Fore, Back, Style
colorama.init()



for i in range(1800):
	b = random.randint(0,9)
	print(Fore.GREEN + a[b], end = " ")
