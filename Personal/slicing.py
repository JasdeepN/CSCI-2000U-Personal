element = 'uranium'
print("should be RAN: is " , element[1:4], "from index a to index b, [a,b)")
print("should be URAN: is " , element[:4], "from blank to index a, [start of list:a)")
print("should be IUM: is " , element[4:], "from index a to blank, [a:end of list]")
print(element[1:1])
print(element[3:1])
print(element[2:1])
print(element[1:-1])
print(element[-7:-2])