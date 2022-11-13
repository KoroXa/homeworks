ls = input('Введите предложение: ').split(' ')or(',')
ml = 0
a = 0
sl = 0
ii = len(ls)

for i in range(0, len(ls)):
	a = 0
	for j in range(0, len(ls[i])):
		
		a += 1
		if a > ml:
			ml = a
			sl = ls[i]
		
print(ii, sl)






