#!/bin/bash
 
if [ ! -f "inw.txt" ]; then
	echo "Preparing field"
	cp "./in.txt" "./inw.txt"
	sed -i 's/-> //g' "inw.txt"
	sed -i 's/,/ /g' "inw.txt"
fi

count=0
c=990

function min (){
echo $(( $1 < $2 ? $1 : $2 ))
return $(( $1 < $2 ? $1 : $2))
}

function max (){
echo $(( $1 > $2 ? $1 : $2))
return $(( $1 > $2 ? $1 : $2))
}

declare -A arr
for ((i=0;i<=c;i++))
do
	for ((j=0;j<=c;j++))
	do
		arr[$i,$j]=0
	done
done

while read x1 x2 y1 y2; do	
	if ((x1 = x2)); 
	then
	       
		for ((k=$(min $y1 $y2);k<=$(max $y1 $y2)+1;k++))
		do
			arr[$k,$x1]=$((arr[$k,$x1] + 1))
			#echo "check"
		done
		continue
	elif ((y1 = y2));
	then
		for ((k=$(min $x1 $x2);k<=$(max $x1 $x2)+1;k++))
		do
			arr[$y1,$k]=$((arr[$k,$x1] + 1))
		done
		continue
	else 
		continue
	fi
done < "inw.txt"
echo "done with loops"

for((i=0;i<=c;i++))
do
	for((j=0;j<=c;j++))
	do
		if ((arr[$i,$j] >= 2));
		then
			count=$((count+1))
		fi
	done
done

echo $count
exit 1

