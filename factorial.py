b = 1
a = int(input("Введите число от 1 до 20! " ))
while a > 20 or a < 1:
	a = int(input("Введите число от 1 до 20! "))
while a != 0:
	b *= a
	a -= 1
	print(a)
print(b)
