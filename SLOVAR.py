#prod = {"Утка" : "350 РУБ", "Соус" : "80 РУБ" , "Морс" : "120 РУБ", "Яблоко" : " 5 РУБ"}

#2. Создать интерфейс - создание словаря. Пользователь сначала вводит N - количество записей, 
#а затем вводит через пробел "индекс - значение". Программа должна вывести получившийся словарь. 
#Также, необходимо придумать оригинальный словарь, а не справочник телефонов.

a = int(input(""))#.split(' ')
sl = {}
while a != 0:
	a -= 1
	b = input()
	B = b.split()
for i in range(len(B)):
	for j in range(len(B)):
		sl[B[i]] = B[j]
	
print(sl)
