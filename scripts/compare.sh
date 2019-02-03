#!/bin/bash

outputs="/home/diogo/Documentos/codeflaws2/data/$1/fix/outputs"
directory="/home/diogo/Documentos/codeflaws2/data/$1"

ls $outputs > outputs.txt

input="versions"
while IFS= read -r i
do
	input2="outputs.txt"
	while IFS= read -r var
	do
		if !(cmp -s $outputs/"$var" $directory/$i/outputs/"$var")
		then
			echo "The files $var e $var-$i are different"
			cmp $outputs/"$var" $directory/$i/outputs/"$var" > $directory/compare/$i/"$var"
		fi
	done < "$input2"

	ls $directory/compare/$i > $directory/comp$i

done < "$input"
