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
		cp data/${ADDR[0]}-${ADDR[1]}/fix/${ADDR[0]}-${ADDR[1]}.c matrix/${ADDR[0]}-${ADDR[1]}/fix/${ADDR[0]}-${ADDR[1]}.c
		cp data/${ADDR[0]}-${ADDR[1]}/fix/traces/app_base.info matrix/${ADDR[0]}-${ADDR[1]}/fix/app_base.info
		cp data/${ADDR[0]}-${ADDR[1]}/versions matrix/${ADDR[0]}-${ADDR[1]}/versions
	fi
	mkdir matrix/${ADDR[0]}-${ADDR[1]}/$i
	cp data/${ADDR[0]}-${ADDR[1]}/$i/matrix matrix/${ADDR[0]}-${ADDR[1]}/$i/matrix
		cp data/${ADDR[0]}-${ADDR[1]}/$i/${ADDR[0]}-${ADDR[1]}.c matrix/${ADDR[0]}-${ADDR[1]}/$i/${ADDR[0]}-${ADDR[1]}.c
		cp data/${ADDR[0]}-${ADDR[1]}/$i/traces/app_base.info matrix/${ADDR[0]}-${ADDR[1]}/$i/app_base.info

done < "$input"



