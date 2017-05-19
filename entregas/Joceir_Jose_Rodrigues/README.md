Equipe:
 
[Joceir Chaves](https://github.com/Joceir)
 
[Jose Rodrigues](https://github.com/jrodrigues1977)

Trabalhos desenvolvidos:

1- As 1500 palavras mais utilizadas em um livro - Alice.txt

2- As 1500 palavras comuns em dois livros - Alice.txt e Flatland.txt

3- Tradução artigo Big Data

Linguagens utilizadas:

Shell Script para tratar textos html e Pig latin

Colocar aqui como faz para executar seu script


Avaliacao
* Onde esta o readme.md e3xplicando o trabalho e como rodar os scripts? 

Instruções para execução:

Instruções para execução:

1. Pré requisitos:

	Toda a atividade foi desenvolvida e testada na VM cloudera-quickstart-vm-5.5.0-0-virtualbox
	

2. Localização dos itens dentro das pastas do projeto:

	2.1 Pig_Latin_code: Scripts em pig para executar os trabalhos propostos 1 e 2.

	2.2 Resultados: Saídas dos dois trabalhos testados já extraídas do HDFS.

	2.3 extrator_textos: Script em Shell para converter livros de html para txt.

	2.4 livros_html: Livros em html para serem convertidos em textos.

	2.5 livros_txt: Livros convertidos em texto para serem processados, no caso os livros descritos no item 2 dos trabalhos desenvolvidos


3. Etapas de execução do projeto

	3.1 Executar o script extrator.sh dentro do diretório do nome do livro (ex: ~/alices-adventures-in-wonderland/./extrator.sh arquivo_de_saida_.txt)

		Utilizar fonte da pasta livros_html

	3.2 Gerar dois arquivos de saída .txt com o script, no caso foram criados Alice.txt e Flatland.txt (conforme pasta livros_txt)

	3.3 Criar um diretório no HDFS para carga dos arquivos .txt: hdfs fs -mkdir /user/cloudera/pig

	3.4 Carregar no HDFS os dois arquivos de livros .txt e mais o arquivo stopwords.txt (da pasta livros_txt)

		hdfs -fs put /user/cloudera/pig/arquivo.txt
	
4. Rodar o script WordCountLivro.pig (pasta Pig_Latin_code): WordCountLivro.pig

	O script está preparado para carregar o arquivo do HDFS: /user/cloudera/pig/Alice.txt e gerar uma saída /user/clouderapig/book_1500_words
	
	Para utilizar outros arquivos .txt, alterar o script comentado
	
5. Rodar o script VocabularioComum.pig (pasta Pig_Latin_code): ~ VocabularioComum.pig

	O script está preparado para carregar os seguintes arquivos do HDFS:
	
	/user/cloudera/pig/Alice.txt
	
	/user/cloudera/pig/Flatland.txt
	
	/user/cloudera/pig/stopwords.txt
	
	Será encontrado as palavras comuns entre os dois livros e eliminado palavras não relevantes conforme conteúdo de "stopwords.txt"
	
	Será gerado o resultado no HDFS: /user/cloudera/pig/common_1500_words_2_books
	
	Para utilizar outros arquivos .txt, alterar o script comentado
