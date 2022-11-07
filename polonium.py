A = input()
B = False
for i in range(0, len(A)):
	if A[i] != A[len(A)-i-1]:
		B = False
	else:
		B = True
if B:
	print("Это палиндром")	
else:
	print("Это не палиндром")	
