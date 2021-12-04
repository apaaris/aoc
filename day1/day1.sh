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
temp1=0
temp2=0
temp3=0
sum1=0
sum2=0
counter1=0

while read line; do
	sum1=$((temp1 + temp2 +temp3))
	sum2=$((line + temp2 + temp3))
	
	
	if (( sum2 > sum1));
    then
	    counter1=$((counter1+1))

    fi
    temp1=$temp2
    temp2=$temp3
    temp3=$line
    sum1=$sum2
done < "$file"
counter=$((counter1-3))
echo "$counter"
exit 1

