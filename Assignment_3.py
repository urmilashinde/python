

Hours = raw_input("Enter the number of hours")
Rate = raw_input("Enter the rate per hour")

if float(Hours) <= 40:
	Pay = float(Hours) * float(Rate)
else:
	Pay = 40 * float(Rate) + (int(Hours) - 40) * 1.5 * float(Rate)

print "Your pay is:", Pay