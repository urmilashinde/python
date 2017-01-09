fruit = "Urmila is the best"
print 'best' in fruit

word1 = "Umang"
word2 = "Urmila"

if word1 < word2:
	print "Umang is less than Urmila"
else:
	print "Urmila is less than Umang"
	
name = "SOHUM PAREKH"

print "Before: ", name

print "After: ", name.lower()

data = "mnfrhfiufksdk@gmail.com njkdsfkjf"

pos1 = data.find('@')

pos2 = data.find(' ', pos1)

print data[pos1+1 : pos2]