x = raw_input("Enter number: ")
if int(x) < 10:
	print 'smaller'

if int(x) > 10:
	print 'bigger'

str = " Hello"
try:
	num = int(str)
except:
	num = -1
	
print "num = ", num

str2 = "123"
try:
	num2 = int(str2)
except:
	num2 = -1
	
print "num2 = ",num2
	

print 'finish'