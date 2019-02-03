#!/bin/bash

input="problems"

while IFS= read -r i
do
	echo $i
	cd data/$i
	bash traces.sh $i
	bash compare.sh $i
	cd ..
	cd ..

done < "$input"
