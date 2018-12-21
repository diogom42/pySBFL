#!/bin/bash

for i in {1..25}
do
		echo "lcov -z -d \$directory -q"
		echo "./a.out < pool/input$i.tes > v\$i/outputs/out$i"
		echo "lcov -c -d \$directory -o v\$i/traces/trace$i.info --test-name trace$i -q"
		#cat v0/outputs/out$i
		#cat v0/temp/heldout-output-pos$i
done
