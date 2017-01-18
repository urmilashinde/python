print [1,[2,3],4]

# string(immutable) Vs Lists(mutable)

fruit = 'banana'
try:
	fruit[0] = 'b'
except:
	print "cannot change single item in the string"

print fruit.lower()

nums = [23, 45, 51,4]

print nums

nums[2] = 50

print nums

print "Legnth of the list is: ", len(nums)

print range(5)

print range(len(nums))

friends = [ 'Aarti', 'Ritu', 'Madhura', 'Shruti']

for i in range(len(friends)):
	friend = friends[i]
 	print "Happy New Year:", friend
 	
stuff = list()
stuff.append('Mango')
stuff.append('Apple')
stuff.append('Orange')
stuff.append('Peach')

print stuff

stuff.sort()

print stuff

#average cal using list methods
numlist = list()
while True:
	inp = raw_input("Enter a number: ")
	if inp == 'done':
		break
	value = float(inp)
	numlist.append(value)

Average = sum(numlist) / len(numlist)

print "Average of nums is:", Average

# String split up into the List of strings 

str = 'My name is Urmila'
lst = str.split()

print lst

print "length of the list lst is:", len(lst)

# splitting using other char than blank space
str2 = 'mango ; banana; apple; orange'
lst2 = str2.split(';')

print lst2