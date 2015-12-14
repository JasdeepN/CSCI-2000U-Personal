#alias - a second name for piece of data
import numpy as np
#####################################################################################################
#Normal Variables
#####################################################################################################
print("Normal Variables")
first = 'issac' 
second = first #set second to the same data as first

first = first + ' newton' #change first leaving second unchanged

print("first: " + first)
print("second: " + second)

#####################################################################################################
#List Variables
#####################################################################################################
print("\nList Variable")
first = ['issac'] #create first as a list 
second = first #set second to the same as first 

##############################
#lecture slides says first = first.append('newton')
##############################
first.append('newton') #add 'newton' to the list 

print(first)
print(second) #didnt explicitly change second

#####################################################################################################
#Grids (LIST)
#####################################################################################################
print("\nGrids")

grid = []
N = 3 #size of grid (NxN) filled with 1's

for x in range(N): #number of sub lists
	temp = []
	for y in range(N): #size of sub lists
		temp.append(y)
	grid.append(temp)
	
print(grid)
N = grid[0]
N[0] = "str data type"
N = grid[1]
N[1] = 'any data can go here'
N = grid[2]
N[2] = 43.25
print(grid)

