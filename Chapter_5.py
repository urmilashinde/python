while True:
	line = raw_input('>')
	if line == 'done':
		break
	print line
	
print "Finish"

friends= [ "Madhura", "Aarti", "Shruti", "Dimpi"]

for friend in friends:
	print "Happy New Year ", friend
	
for i in[5,4,3,2,1]:
	print i

smallest = None
for value in[9, 13, 2, 8, 54]:
	if smallest is None:
		smallest = value
	elif value < smallest:
		smallest = value

print "smallest value is: ", smallest
	
	
print "DONE"