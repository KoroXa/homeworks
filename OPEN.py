import os,time

for i in range(5):
	file_path = r'C:\windows\system32\cmd.exe'
	os.system("start "+file_path)
	time.sleep(1)
