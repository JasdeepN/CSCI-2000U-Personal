def bounds(values):
	low = min(values)
	high = max(values)
	return(low,high)



print(bounds([3, -5, 9, 4, 17, 0]))

least,greatest = bounds([3, -5, 9, 4, 17, 0])

print(least)

print(greatest)