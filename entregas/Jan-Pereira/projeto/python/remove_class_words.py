
import os, sys

import nltk

def lerArquivo(arquivo):

	file = open(arquivo, 'r')

	conteudo = file.read()

	file.close()

	return conteudo

def gravarArquivo(arquivo, conteudo):

	file = open(arquivo, 'w')

	file.write(str(conteudo))

	file.close() 

def listarLivros(path):

	books = []
	
	dirs = os.listdir( path )

	dirs.sort()

	for file in dirs:
   	
		books.append(path+"/"+file)  

	return books

input = sys.argv[1]
output = sys.argv[2]

#output = "/home/janpereira/books/words"

tipoPalavrasNaoPermitidas = ['CC', 'DT', 'IN', 'LS', 'PRP', 'RP', 'TO', 'UH', 'WDT', 'WP', 'WRB']

#books = listarLivros("/home/janpereira/books/txt")

books = listarLivros(input)

for book in books:

	conteudoNovo = ""

	conteudo = lerArquivo(book)

	tokens = nltk.word_tokenize(conteudo)

	results = nltk.pos_tag(tokens)

	for result in results:
		chave, valor = result

		if valor not in tipoPalavrasNaoPermitidas: 
			conteudoNovo += chave + " "
			#print chave + " => " + valor

	
	pasta = book.split("/")

	arquivo = output + "/" + pasta[5]

	gravarArquivo(arquivo, conteudoNovo.strip())

	#sys.exit()