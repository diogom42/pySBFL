#!/bin/bash

mkdir compare
for i in {0..8}
do
	mkdir compare/v$i
	mkdir v$i/outputs
	mkdir v$i/traces
done
