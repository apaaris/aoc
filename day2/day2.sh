#!/bin/bash

hor=0
depth=0
f="forward"
d="down"
u="up"

while read order value; do
	if [[ "$order" == "$f" ]]; 
	then
		hor=$((hor + value))
		
	elif [[ "$order" == "$d" ]]; 
	then
		depth=$((depth + value))
	
	else [[ "$order" == "$u" ]]; 
		depth=$((depth - value))
	fi

done < "in.txt"
aim=0
echo "Task 1: $((hor*depth))"
while read order value; do
	if [[ "$order" == "$f" ]]; 
	then
		hor=$((hor + value))
		depth=$((depth + aim * value))
		
	elif [[ "$order" == "$d" ]]; 
	then
		aim=$((aim + value))	
	else [[ "$order" == "$u" ]]; 
		aim=$((aim - value))
	fi
done < "in.txt"
echo "Task 2: $((hor*depth))"
exit 1
