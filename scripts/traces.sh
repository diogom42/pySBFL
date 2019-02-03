#!/bin/bash

#variavel com caminho do diretorio do projeto
directory="/home/diogo/Documentos/codeflaws2/data/$1"

input="$directory/versions"

while IFS= read -r i
do
	gcc -fprofile-arcs -ftest-coverage "$i/$1.c"
        echo $i	

	#trace sem execucao
	lcov -c -i -d $directory -o "$i/traces/app_base.info" --test-name base -q

                test=0
                universe="universe"
                while IFS= read -r u
                do
			test=$((test + 1)) 
			lcov -z -d $directory -q
			timeout 5s ./a.out < pool/$u > $i/outputs/out$test
			if [ $? = 124 ] ; then
				echo "timeout"
				echo "timeout" > $i/outputs/out$test"timeout"
			fi
			
			lcov -c -d $directory -o $i/traces/trace$test.info --test-name trace$test -q
                	
                done < "$universe"

done < "$input"
