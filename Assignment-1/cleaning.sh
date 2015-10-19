#!/bin/bash
find */data/NOTES -delete
mv */*/ assignment_1/cleaned_data
for file in *; do mv $file $file.txt; done