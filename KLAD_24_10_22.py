import random, os, sys
x, y = 0, 0

x1,y1 = random.randint(-10, 10), random.randint(-10, 10) 

running = True
direct = 0
a = 0
print(x1, y1)
while running:
	
	direct = int(input("Куда хотите сходить? 1- вверх, 2 - вправо, 3 - вниз, 4 - налево "))
	a = int(input("Сколько шагор будет за ход? "))
	#os.system('cls')
	if direct == 1:
		y += a
		
		print("Ваши координаты:", x, y)
			
	elif direct == 2:
		x += a
		
		print("Ваши координаты:", x, y)
			
	elif direct == 3:
		y -= a
		
		print("Ваши координаты:", x, y)
			
	elif direct == 4:
		x -= a
		
		
		print("Ваши координаты:", x, y)
			
	if x + 4 > x + 3 > x1 and y + 4 > y + 3 > y1:
		print("Клад близко")
	if x == x1 and y == y1:
		os.system('cls')
		print('\nВы нашли клад!') 
		running = False
	
