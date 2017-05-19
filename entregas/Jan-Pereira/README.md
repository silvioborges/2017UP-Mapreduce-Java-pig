# Universidade Positivo - Disciplina sobre Map Reduce

### Aluno

  - [Jan Antonio Pereira]

### Artigo

O artigo escolhido por mim para ser traduzido foi escrito pela equipe de infraestrutura de dados do Facebook:

Hive – A Petabyte Scale Data Warehouse Using Hadoop

Obs: O artigo original e a respectiva tradução pode ser encontrada na pasta artigo.


### Projeto / Problema

Dado um conjunto de livros dividos em diversos capítulos em formato HTML extraídos do site https://etc.usf.edu/lit2go/books.


1) Extrair apenas os textos de cada capítulo e produzir um arquivo único em formato .txt contendo todo o livro com todas as palavras em caixa-baixa.

2) Remover as preposições e outras classes de palavras menos significantes dos livros.

3) Mover a pasta dos livros com os arquivos txts gerados para o HDFS. 

4) Fornecer uma palavra e mostrar em que arquivos encontramos a palavra.

5) Fornecer uma palavra e mostrar em que arquivos encontramos a palavra e a quantidade de ocorrências.

6) Mover o resultado do processamento Hadoop MapReduce para o Sistema de Arquivo Local. 


### Requisitos

  - Como ambiente de desenvolvimento foi baixado o VirtualBox e uma imagem da VM do cloudera-quickstart-vm-5.7.0.0.
  - A VM cloudera já nos entrega instalado um ambiente completo, mas escolhemos utilizar na solução deste problema Python 2.7, Hadoop e Pig.
  - Para extrair os textos dos arquivos HTMLs foi instalada a biblioteca python BeautifulSoup (bs4).
  - Para extrair as preposições dos textos foi instalada a biblioteca python NLTK.
  - Para procurar e contar palavras dentro dos arquivos textos foi utilizada a linguagem Pig.
  
  
### Solução

Para a execução dos scripts abaixo, utilize o terminal disponível na VM cloudera.


1) Para extrair e gerar os textos em formato txt de cada capítulo para cada livro, execute o script abaixo:

python extract_text.py <input_path_book_html> <output_path_book_txt>

ex:  python extract_text.py /home/janpereira/books /home/janpereira/books/fullbooks

Obs: Certifique-se que o diretório de destino exista antes executar o extract_text.py. 


2) Para extrair e gerar os textos em formato txt removendo as preposições e outras classes de palavras, execute o script abaixo:

python remove_class_words.py <input_path_book_txt> <output_path_book_txt>

ex: python remove_class_words.py /home/janpereira/books/fullbook /home/janpereira/books/wordsbooks

Observações:

Lembre-se de instalar a biblioteca python NLTK.

Para analisar as classes de palavras será importante fazer o download dos datasets da linguagem inglesa.

Após instalar a biblioteca NLTK, para auxiliá-lo no download dos datasets basta executar python download_nltk.py.

Agora sim, basta se certificar que o diretório de destino exista e executar o remove_class_words.py.


3) Para mover a pasta books para o HDFS, execute o script abaixo:

hdfs dfs -put <path_local_book> <path_hdfs_book>


4) Para procurar e listar os livros que contenham uma dada palavra, execute o script abaixo:

pig -f SearchWordFile.pig -param keyword=<informe_a_palavra> -param input=<input_path_hdfs_books> -param output=<output_path_hdfs_books>


5) Para procurar, listar e contar os livros que contenham uma dada palavra, execute o script abaixo:

pig -f SearchWordCountFile.pig -param keyword=<informe_a_palavra> -param input=<input_path_hdfs_books> -param output=<output_path_hdfs_books>


6) Para mover a pasta configurada de saída do processamento das pesquisas para o ambiente local, execute o script abaixo:

hdfs dfs -get <path_hdfs_output> <path_local_output>


Obs: Os códigos-fontes e os livros utilizados na solução deste problema em forma de exercícios utilizando python e pig podem ser encontrados na pasta projeto.
