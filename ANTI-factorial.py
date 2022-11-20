b = 1
a = int(input("Введите число! " ))
c = [1, 2, 6, 24,120, 720, 5040, 40320, 362880, 3628800]
e = 0

for i in range(0, len(c)):
	if a > c[i]:#c[i] // 2 < c[i - 1] * 2:# and a < c[i + 1]:
		e += 1


print(c[e])
