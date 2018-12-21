#!/bin/bash

outputs="/home/diogo/Documents/Pesquisa/$1/v0/outputs"
directory="/home/diogo/Documents/Pesquisa/$1"

ls $outputs > outputs.txt

input="versions"
while IFS= read -r i
do
	input2="outputs.txt"
	while IFS= read -r var
	do
		if !(cmp -s $outputs/"$var" $directory/v$i/outputs/"$var")
		then
			echo "The files $var e $var-v$i are different"
			cmp $outputs/"$var" $directory/v$i/outputs/"$var" > $directory/compare/v$i/"$var"
		fi
	done < "$input2"

	ls $directory/compare/v$i > $directory/compv$i

done < "$input"
