#!/bin/bash
#Jasdeep Nijjar - 100493157

#WANT THIS PROGRAM TO DO THE FOLLOWING: REOMVE K LINES FROM TOP AND M LINES FROM BOTTOM PRINT TO TERMINAL
read k #number of lines to remove from top
read m #number of lines to remove from bottom
read filename #name of file


let "k += 1" #add 1 to k so tail doesnt go out of bounds
            
echo | tail -n +$k $filename | head -n -$m  #runs input->tail->output->head->output->terminal
