import os
s = open('words.txt', 'r', encoding = 'utf-8')
f = s.read().splitlines()
print(f)
dict = {}

for i in range(0, len(f)):
	d,e = f[i].split(' - ')
	dict[d] = e
	
print(dict)
s.close()
a = input("Введи слово на русском: ")
suc = False
opeen = True
while 2!=1:
	if opeen == True:
		q = int(input("1 - перевести слово" + '\n 2 - добавить слово' + '\n 3 - не показывать это меню(старый выбор)'))
	os.system('cls')
	if q == 3:
		opeen = False
		
	if q == 1 or opeen == False:
		if a in dict:		
			print(a, '-', dict[a])
			suc = True
		else:
			suc == False
	
	if q == 2 or opeen == False and suc == False:
		r = input("Введи слово на русском: ")
		e = input("Введи слово на английском: ")
		dict[r] = e
		print("Слово", r, "добавлено в словарь!")
		s = open('words.txt', 'a', encoding = 'utf-8')
		s.write('\n' + r + ' - ' + e)
		s.close()
	a = input("Введи слово на русском: ")	
		
		
		
		
		
		
		
		
		
		
