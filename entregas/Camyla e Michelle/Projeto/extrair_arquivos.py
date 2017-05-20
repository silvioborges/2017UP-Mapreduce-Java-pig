import string
import logging

import re

import sys

import os

import io



livros = "/home/cloudera/Python/binhara/livros/lit2go.ok"

out = "/home/cloudera/Python/binhara/livros/"

file_out = 'livros.txt' 



logging.basicConfig(filename=out+'livros.log', filemode='w', level=logging.INFO, format='%(asctime)s %(levelname)s - %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')



logging.info('### Extraindo texto ###')

logging.info('Read: %s' %livros)

logging.info('Out: %s' %out)

logging.info('')



path = os.path.join(livros, "targetdirectory")



pattern = "index.html"

list_files = []

for path, subdirs, files in os.walk(livros):

    for name in files:

        if os.path.join(path, name).find(pattern) >0 and os.path.join(path, name).find(pattern) >0:

            list_files.append(os.path.join(path, name))

print (list_files[:3])



def delete_file():

    try:

        with open(out + file_out) as existing_file:

            existing_file.close()

            os.remove(out + file_out)

    except :

        pass

    



delete_file()

loop_ok = 0

livro = 'n'



for path in list_files:

    logging.info('---')

    logging.info('Path: %s' %path)

    

    try:

        page = open(path).read()



        from bs4 import BeautifulSoup

        soup = BeautifulSoup(page, 'html.parser')

        paragrafo = soup.select('div#i_apologize_for_the_soup p')

        texto ="";

        

        for p in paragrafo:

            texto = texto + p.get_text().strip().translate(str.maketrans("|\t\n.,\'", "      "))

            

        livro = soup.find_all('h2')[0].get_text().strip().replace('|', ' ')

        

        capitulo = re.sub(re.compile('\Z'), '', soup.find_all('h4')[0].get_text().strip().replace('|\n\t', ' '))

        #capitulo_num = soup.find_all('h4')[0].get_text().split(":")[0].strip().replace('|\n\t', ' ')

        #capitulo_nome = soup.find_all('h4')[0].get_text().split(":")[1].strip().replace('|\n\t', ' ')

        

        #print("livro: " + livro)

        #print("capitulo: " + capitulo)

        #print("capitulo_num: " + capitulo_num)

        #print("capitulo_nome: " + capitulo_nome)

        logging.info('Livro: %s |Capitulo:  %s ' %(livro, capitulo))

    

        with open(out + file_out, 'a') as f:

            if loop_ok == 0:

                f.write("%s|%s|%s|%s \n" %(path, livro, capitulo, re.sub("[^0-9a-zA-Z ]", '', texto).lower()))

                loop_ok+=1

            else:

                f.write("%s|%s|%s|%s  \n" %(path, livro, capitulo, re.sub("[^0-9a-zA-Z ]", '', texto)))

                    

            f.close()

        

            

    except (IndexError, UnicodeDecodeError):

        logging.warning("Não foi possivel extrair de %s" % path)





logging.info('')

logging.info('Encerrando processamento')

        
