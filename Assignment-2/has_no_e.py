#python
#finds weather file contains the letter e returns true if it finds the letter 'e'
def has_no_e(input_string):
	for x in input_string:
		pass
		if (x == 'e'):
			print ('true')
			return
	print('false')
		

#opens the file for reading 
def main():
	filex  = open('gadsby.txt', "r") #open file in read only mode
	for line in filex: #sends line by line to has_no_e
		has_no_e(line);
	filex.close() #close the file
		
main()
#has_no_e(raw_input()) #terminal input 