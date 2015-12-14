def greet():
	return 'Good evening, master'

def greet(name):
	answer = 'Hello, ' + name
	return answer

temp = greet('doctor') #python doesnt have multiple function definitions, takes the last one
print(temp)

def add(a):
	b = a + 1 #adds 1 to the inputed number
	return b

def double(c):
	d = 2 * add(c) #doubles returned number
	return d

val = 10
result = double(val) #add 1 then double
print (result)

print(greet('from print'))

def sign(num):
	if num > 0:
		return 1
	elif num == 0:
		return 0
	else: 
		return -1

print(sign(3))
print(sign(-9))

def sign(num): #overwirte old sign function
	if num > 0:
		return 1
	elif num == 0:
		return 0
	# else: 
	# 	return -1

print(sign(3))
print(sign(-9)) 

def double (x):
	return 2 * x

print(double(2)) #fix below
print(double('two'))


def double (x):
	if type(x) == int:
		return 2 * x
	elif type(x) == str:
		return x
	else:
		return 0

print(double(2)) #fix below
print(double('two'))

def greet (name=''): #name doesnt have to be given a value
	return ('Hello, ' + name)
	
print(greet('test'))
print(greet())	

def adjust(value, amount=2.0):
	return value*amount

print(adjust(5))
print(adjust(5, 2.5))	

#running multiple functions in one command
funcs = [sign, adjust]

for f in funcs:
	print(f(3))


#variable list of inputs for function
def add_all (func='add', *argv):
	total = 0;
	if func == 'mul':
		for a in argv:
			total += (a*2)
	elif func == 'sub':
		for a in argv:
			total -= a		
	else:
		for a in argv:
			total += a
	return total

print(add_all())
print(add_all('sub', 1,2,3))
print(add_all('mul', 1,2,3))








