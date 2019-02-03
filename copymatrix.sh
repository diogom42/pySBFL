#!/bin/bash

problem="0"
input="versions"


mkdir matrix

while IFS= read -r i
do
	IFS='-' read -ra ADDR <<< "$i"

	if [ "$problem" != "${ADDR[0]}-${ADDR[1]}" ]; then
		problem=${ADDR[0]}-${ADDR[1]}
		mkdir matrix/${ADDR[0]}-${ADDR[1]}
		mkdir matrix/${ADDR[0]}-${ADDR[1]}/fix
		cp data/${ADDR[0]}-${ADDR[1]}/fix/matrix matrix/${ADDR[0]}-${ADDR[1]}/fix/matrix
	fi
	mkdir matrix/${ADDR[0]}-${ADDR[1]}/$i
	cp data/${ADDR[0]}-${ADDR[1]}/$i/matrix matrix/${ADDR[0]}-${ADDR[1]}/$i/matrix

done < "$input"



