N = int(input())		# макс размер упак
M = int(input())	# кол-во ручек

otv = 0
k = 0
m = []


while M > N:
	#k = k + N
	print()
	print(N)
	M -= N
	N -= 1
	#otv += 1
	print(M)
	
	if N == 0:
		otv = 0
		print('0')
		break


		
		
		















