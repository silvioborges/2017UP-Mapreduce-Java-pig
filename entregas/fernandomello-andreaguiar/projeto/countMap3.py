#!/usr/bin/python3
import sys
import re
from nltk.corpus import wordnet as wn
from nltk import pos_tag
import nltk


for line in sys.stdin:
	line = re.sub(re.compile('([^A-Z a-z])+'), ' ', line)
	words = nltk.word_tokenize(line)
	classificacao = pos_tag(words)
	for word in classificacao:
		#removendo as preposicoes do texto
		if (word[1] != 'IN'):
			print (word[0].upper() + '\t1')	
