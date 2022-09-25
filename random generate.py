import random, os

a = 0
for i in range(1000000):
	os.system('cls')
	b = random.randint(0, 1000)
	a+= b
	
	print(a)
	
