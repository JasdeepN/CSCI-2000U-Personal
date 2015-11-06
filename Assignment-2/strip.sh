#!/bin/bash
#Jasdeep Nijjar - 100493157

#WANT THIS PROGRAM TO DO THE FOLLOWING: REOMVE K LINES FROM TOP AND M LINES FROM BOTTOM PRINT TO TERMINAL
read k #number of lines to remove from top
read m #number of lines to remove from bottom
read filename #name of file

#cat $filename | head -n $k #returns top k lines
#cat $filename | tail -n $m #returns bottom m lines
#echo "Printing >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" $filename
#cat $filename

#cat $filename | head -n $k 

#cat $filename
                 # Integer.
let "k += 1"
echo "k = $k "           # a = 2335         
tail -n +$k $filename | head -n -$m | cat > "temp_file_1.txt"
#head -n -$m "temp_file_1.txt"
#want top 26 lines and bottom 2 lines removed everything else stays
#TAIL | HEAD | cat 