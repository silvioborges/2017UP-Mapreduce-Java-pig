#!/usr/bin/python3
import sys

(lastKey, sum, listagem, listagemNova)=(None, 0, {}, {})

for line in sys.stdin:
	(key, value) = line.strip().split("\t")
	
	#nova palavra
	if lastKey and lastKey != key:
		listagem[lastKey] = sum
		(lastKey, sum) = (key, int(value))
	
	#primeira palavra ou a mesma palavra
	else:
		(lastKey, sum) = (key, sum + int(value))

if lastKey:
	listagem[lastKey] = sum

for key, value in sorted(listagem.items(), key=lambda listagem: listagem[1], reverse=True):
	print (key + '\t' + str(value))

