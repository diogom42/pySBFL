#!/bin/bash

problem="0"
input="versions"


mkdir data

while IFS= read -r i
do
	IFS='-' read -ra ADDR <<< "$i"

	if [ "$problem" != "${ADDR[0]}-${ADDR[1]}" ]; then
		problem=${ADDR[0]}-${ADDR[1]}
		mkdir data/${ADDR[0]}-${ADDR[1]}
		mkdir data/${ADDR[0]}-${ADDR[1]}/fix
		mkdir data/${ADDR[0]}-${ADDR[1]}/fix/outputs
		mkdir data/${ADDR[0]}-${ADDR[1]}/fix/traces
		mkdir data/${ADDR[0]}-${ADDR[1]}/pool
		mkdir data/${ADDR[0]}-${ADDR[1]}/compare
		mkdir data/${ADDR[0]}-${ADDR[1]}/compare/fix
		cp codeflaws/$i/${ADDR[0]}-${ADDR[1]}-${ADDR[4]}.c data/${ADDR[0]}-${ADDR[1]}/fix/${ADDR[0]}-${ADDR[1]}.c
		cp codeflaws/$i/heldout-input-pos* data/${ADDR[0]}-${ADDR[1]}/pool		
		ls data/${ADDR[0]}-${ADDR[1]}/pool > data/${ADDR[0]}-${ADDR[1]}/universe
		cp scripts/* data/${ADDR[0]}-${ADDR[1]}
		echo fix >> data/${ADDR[0]}-${ADDR[1]}/versions
	fi
	mkdir data/${ADDR[0]}-${ADDR[1]}/$i
	mkdir data/${ADDR[0]}-${ADDR[1]}/compare/$i
	mkdir data/${ADDR[0]}-${ADDR[1]}/$i/outputs
	mkdir data/${ADDR[0]}-${ADDR[1]}/$i/traces
	cp codeflaws/$i/${ADDR[0]}-${ADDR[1]}-${ADDR[3]}.c data/${ADDR[0]}-${ADDR[1]}/$i/${ADDR[0]}-${ADDR[1]}.c
	echo $i >> data/${ADDR[0]}-${ADDR[1]}/versions

done < "$input"



