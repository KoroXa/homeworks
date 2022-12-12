x = int(input())
y = int(input())
lx = 0
ly = 0
zx = 0
zy = 0
v = ''
for i in range(3):
	lx += 1
	ly += 1
	
if x>y:
	v = 'H'
if y>x:
	v = 'V'	

for i in range(2):
	if v =='H':
		ly -= 1
	if v == 'V':
		ly += 1

print(lx, ly)




















