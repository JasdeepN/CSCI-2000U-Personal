#!/bin/bash
#Jasdeep Nijjar - 100493157

#removes k lines from top and m lines from bottom of input file use > to output to file
read k #number of lines to remove from top
read m #number of lines to remove from bottom
read filename #name of file


let "k += 1" #add 1 to k so tail doesnt go out of bounds

echo | tail -n +$k $filename | head -n -$m  #runs input->tail->output->head->output->terminal
