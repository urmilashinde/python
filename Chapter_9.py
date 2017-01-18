bag = dict()

bag['Veggie'] = 'Eggplant'
bag['fruit'] = 'Apple'

bag['chips'] = 'Lays'
bag['drink'] = 'Coke'

print bag

bag['fruit'] = 'Mango'

print bag

purse = {'age':12, 'rank':3}

print purse

print 'num' in purse

group = {}

print group 

counts = dict()

counts = { 'Uma':0, 'Umang':0, 'Sohum':0}

while True:
	name = raw_input("Enter name")

	if name in counts:
		counts[name] = counts[name]+1
	elif name == 'done':
		break
	else:
		print "name is not in the dictionary"
		break

print counts

