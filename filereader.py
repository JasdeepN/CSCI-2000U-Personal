#python 

file_name = raw_input ("enter name of file to write to\n")
write_mode = raw_input ("enter the write mode you wish to use\n")

filex  = open(file_name, write_mode)

print "file closed =", filex.closed
print filex.name, "opened" 
print "writing mode", filex.mode

user_input = raw_input ("enter string to write to file\n")
filex.write(user_input)
filex.write("\n")
filex.close()

filex  = open(file_name, "r")
print "writing mode", filex.mode
print "\n======FILE CONTENTS======\n"
print filex.read()

filex.close()