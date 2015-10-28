#!/bin/bash
#Jasdeep Nijjar - 100493157

read k #number of lines to remove from top
read m #number of lines to remove from bottom
read filename #name of file

cat $filename | tail -n $k
cat $filename | head -n $m


