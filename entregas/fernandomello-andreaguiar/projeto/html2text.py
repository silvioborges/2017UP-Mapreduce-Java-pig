# Executar utilizando python3
# Necessario instalar as bibliotecas bs4

#importando as bibliotecas
import sys
import os
import io

# ALTERE AS VARIAVEIS "livros" E "saida" ABAIXO:
# livros => caminho onde estao os arquivos
livros = "/home/cloudera/bigdata/exerc_lit2go/lit2go.ok"

# saida => caminho onde os resultados serão salvos.
saida = "/home/cloudera/bigdata/hadoop_streaming_mapred/"

#nome do arquivo de saida
arquivo_saida = 'livros.txt'

#transformando a string em path
caminho_pasta = os.path.join(livros, "targetdirectory")

#nomepadrao para o arquivo html
arquivo_html = "index.html"

#iniciando a variavel que contera os arquivos mapeados
lista_arquivos = []

#mapeando os arquivos encontrados no diretorio apontado na variavel livros
for caminho_pasta, subdiretorios, arquivos in os.walk(livros):
	for nome in arquivos:
		if os.path.join(caminho_pasta, nome).find(arquivo_html) >0 and os.path.join(caminho_pasta, nome).find(arquivo_html) >0:
			lista_arquivos.append(os.path.join(caminho_pasta, nome))

#funcao que apaga o arquivo de saida caso ele ja exista
def deleta_arquivo_saida():
	try:
		with open(saida + arquivo_saida) as arquivo_existente:
			arquivo_existente.close()
			os.remove(saida + arquivo_saida)
	except :
		pass

#executando a funcao deleta_arquivo_saida
deleta_arquivo_saida()

#iniciando as variaveis para o FOR IN
loop_ok = 0
livro = 'n'

#extraindo conteudo dos arquivos 
for caminho_pasta in lista_arquivos:
    
	try:
		#abre o arquivo da pagina html
		pagina = open(caminho_pasta,  encoding='utf-8').read()
		
		#importa a biblioteca bs4 
		from bs4 import BeautifulSoup

		#faz a leitura do arquivo em formato HTML
		soup = BeautifulSoup(pagina, 'html.parser')

		#busca o conjunto de paragrafos (tag <p>) dentro da div cujo ID (#) chama-se "i_apologize_for_the_soup p" e carrega o texto contido em cada um deles
		paragrafo = soup.select('div#i_apologize_for_the_soup p')
		
		#iniciando a variavel texto		
		texto = "";
        
		#percorrendo o conjunto de paragrafos e concatenando o conteudo na variavel texto
		for p in paragrafo:
			texto = texto + p.get_text().strip().replace('|', ' ').replace('\t', ' ').replace('\n', ' ')
    
		#gravando o conteudo da variavel texto no arquivo de saida
		with open(saida + arquivo_saida, 'a',encoding='utf8') as f:
			if loop_ok == 0:
				f.write("%s" %(texto))
				loop_ok+=1
			else:
				f.write("|%s" %(texto))
                    
			f.close()
        
	#caso ocorra algum erro mostra o caminho da pasta que nao foi possivel fazer a
	except (IndexError, UnicodeDecodeError):
		print (caminho_pasta)

#ao final emite uma mensagem de conclusao
print ("arquivos processados!")
