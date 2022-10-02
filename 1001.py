a = '0110'
b = ''
for i in range (0, len(a)):
	if a[i] == '0':
		b += '1'
	else:
		b += '0'
print(b)
