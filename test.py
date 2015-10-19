num = 2
while num <= 10:
	is_prime = True
	trial = 2
	while trial**2 < num:
		if (num % trial) == 0:
			is_prime = False
		trial += 1
	if is_prime:
		print (num)
	num += 1
	
	#fix