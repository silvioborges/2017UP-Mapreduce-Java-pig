
import os, sys, fnmatch, re

from bs4 import BeautifulSoup

def lerDiretorio(path, txt):

	conteudo = ""

	dirs = os.listdir( path )

	dirs.sort()

	for file in dirs:
   
		size = os.path.getsize(path+"/"+file)

		if (os.path.isfile(path+"/"+file)):
			
			conteudo = lerArquivo(path+"/"+file)

			conteudo += " "

			gravarArquivo(txt, conteudo)

		elif (os.path.isdir(path+"/"+file)):
				
			lerDiretorio(path+"/"+file, txt)


def lerArquivo(path):

	file = open(path, "r")
	
	html = file.read()

	return lerArquivoHtml(html)

	#sys.exit(0) 

def lerArquivoHtml(html):
	
	soup = BeautifulSoup(html, 'html5lib')

	capitulo = soup('div', {'id' : 'shrink_wrap'})

	textoFinal = ""

	if (len(capitulo) > 0):		

		for row in capitulo[0].find_all('p'):
		
			texto = row

			texto = texto.get_text()

			texto = re.sub('[^a-zA-Z 0-9]', '', texto)
		
			texto = texto.replace('\n', '').replace("'", "").replace('"', '').replace(',', '').replace('?', '').replace('!', '').replace('.', '').replace(';', '')

			texto = texto.lower().rstrip ('\n').rstrip ('\t')
		
			texto = re.sub('\s+',' ', texto)

			texto += " "

			textoFinal += texto


	return textoFinal


def gravarArquivo(arquivo, conteudo):

	file = open(arquivo, 'a')

	file.write(str(conteudo))

	file.close() 

def listarLivros(path):

	books = []
	
	dirs = os.listdir( path )

	dirs.sort()

	for file in dirs:
   
		if ((os.path.isdir(path+"/"+file)) and (str(file).isdigit())):
			
			dirs2 = os.listdir( path+"/"+file )	

			books.append(path+"/"+file+"/"+dirs2[0])  

	return books

	
input = sys.argv[1]
output = sys.argv[2]

#books = listarLivros("/home/janpereira/books")

books = listarLivros(input)

for book in books:

	pasta = book.split("/")

	#arquivo = "/home/janpereira/books/txt/" + pasta[5] + ".txt"
	
	arquivo = output + "/" + pasta[5] + ".txt"

	lerDiretorio(book, arquivo)