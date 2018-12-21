#!/bin/bash

#variavel com caminho do diretorio do projeto
directory="/home/diogo/Documents/Pesquisa/$1/"

input="versions"

while IFS= read -r i
do
	gcc -fprofile-arcs -ftest-coverage "v$i/$1.c"
        echo $i	

	#trace sem execucao
	lcov -c -i -d $directory -o "v$i/traces/app_base.info" --test-name base -q

		lcov -z -d $directory -q
		./a.out < pool/input1.tes > v$i/outputs/out1
		lcov -c -d $directory -o v$i/traces/trace1.info --test-name trace1 -q
		lcov -z -d $directory -q
		./a.out < pool/input2.tes > v$i/outputs/out2
		lcov -c -d $directory -o v$i/traces/trace2.info --test-name trace2 -q
		lcov -z -d $directory -q
		./a.out < pool/input3.tes > v$i/outputs/out3
		lcov -c -d $directory -o v$i/traces/trace3.info --test-name trace3 -q
		lcov -z -d $directory -q
		./a.out < pool/input4.tes > v$i/outputs/out4
		lcov -c -d $directory -o v$i/traces/trace4.info --test-name trace4 -q
		lcov -z -d $directory -q
		./a.out < pool/input5.tes > v$i/outputs/out5
		lcov -c -d $directory -o v$i/traces/trace5.info --test-name trace5 -q
		lcov -z -d $directory -q
		./a.out < pool/input6.tes > v$i/outputs/out6
		lcov -c -d $directory -o v$i/traces/trace6.info --test-name trace6 -q
		lcov -z -d $directory -q
		./a.out < pool/input7.tes > v$i/outputs/out7
		lcov -c -d $directory -o v$i/traces/trace7.info --test-name trace7 -q
		lcov -z -d $directory -q
		./a.out < pool/input8.tes > v$i/outputs/out8
		lcov -c -d $directory -o v$i/traces/trace8.info --test-name trace8 -q
		lcov -z -d $directory -q
		./a.out < pool/input9.tes > v$i/outputs/out9
		lcov -c -d $directory -o v$i/traces/trace9.info --test-name trace9 -q
		lcov -z -d $directory -q
		./a.out < pool/input10.tes > v$i/outputs/out10
		lcov -c -d $directory -o v$i/traces/trace10.info --test-name trace10 -q
		lcov -z -d $directory -q
		./a.out < pool/input11.tes > v$i/outputs/out11
		lcov -c -d $directory -o v$i/traces/trace11.info --test-name trace11 -q
		lcov -z -d $directory -q
		./a.out < pool/input12.tes > v$i/outputs/out12
		lcov -c -d $directory -o v$i/traces/trace12.info --test-name trace12 -q
		lcov -z -d $directory -q
		./a.out < pool/input13.tes > v$i/outputs/out13
		lcov -c -d $directory -o v$i/traces/trace13.info --test-name trace13 -q
		lcov -z -d $directory -q
		./a.out < pool/input14.tes > v$i/outputs/out14
		lcov -c -d $directory -o v$i/traces/trace14.info --test-name trace14 -q
		lcov -z -d $directory -q
		./a.out < pool/input15.tes > v$i/outputs/out15
		lcov -c -d $directory -o v$i/traces/trace15.info --test-name trace15 -q
		lcov -z -d $directory -q
		./a.out < pool/input16.tes > v$i/outputs/out16
		lcov -c -d $directory -o v$i/traces/trace16.info --test-name trace16 -q
		lcov -z -d $directory -q
		./a.out < pool/input17.tes > v$i/outputs/out17
		lcov -c -d $directory -o v$i/traces/trace17.info --test-name trace17 -q
		lcov -z -d $directory -q
		./a.out < pool/input18.tes > v$i/outputs/out18
		lcov -c -d $directory -o v$i/traces/trace18.info --test-name trace18 -q
		lcov -z -d $directory -q
		./a.out < pool/input19.tes > v$i/outputs/out19
		lcov -c -d $directory -o v$i/traces/trace19.info --test-name trace19 -q
		lcov -z -d $directory -q
		./a.out < pool/input20.tes > v$i/outputs/out20
		lcov -c -d $directory -o v$i/traces/trace20.info --test-name trace20 -q
		lcov -z -d $directory -q
		./a.out < pool/input21.tes > v$i/outputs/out21
		lcov -c -d $directory -o v$i/traces/trace21.info --test-name trace21 -q
		lcov -z -d $directory -q
		./a.out < pool/input22.tes > v$i/outputs/out22
		lcov -c -d $directory -o v$i/traces/trace22.info --test-name trace22 -q
		lcov -z -d $directory -q
		./a.out < pool/input23.tes > v$i/outputs/out23
		lcov -c -d $directory -o v$i/traces/trace23.info --test-name trace23 -q
		lcov -z -d $directory -q
		./a.out < pool/input24.tes > v$i/outputs/out24
		lcov -c -d $directory -o v$i/traces/trace24.info --test-name trace24 -q
		lcov -z -d $directory -q
		./a.out < pool/input25.tes > v$i/outputs/out25
		lcov -c -d $directory -o v$i/traces/trace25.info --test-name trace25 -q

done < "$input"
