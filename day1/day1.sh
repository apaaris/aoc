#!/bin/bash

file="in.txt"
temp=0
counter=0

while read line; do
	if (( line > temp));
    then
	    counter=$((counter+1))

    fi
    temp=$line
done < "$file"
counter=$((counter-1))
echo "$counter"
exit 1

