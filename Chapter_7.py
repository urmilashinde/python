try:
	f_handle = open('My_file.txt')
except:
	print "File cannot be opened"
	exit()

for line in f_handle:
	print line.strip()