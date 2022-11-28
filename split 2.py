a = int(input("Введите кол-во строк"))
while a != 0:
	a -= 1
	b = input()
	B = b.split()
	for i in range(len(B)):
		B[i] = int(B[i])
	
	print(min(B))
	

