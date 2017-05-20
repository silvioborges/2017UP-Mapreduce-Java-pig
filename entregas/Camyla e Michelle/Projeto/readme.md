<h2> Count Words by book</h2>

<h3>1. Extraindo dados</h3>

1.1 Salvar arquivos dos livros em uma pasta, descompactado.<br>
1.2 Atualizar caminhos do codigo extrair_arquivos.py para pasta com extração<br>
1.3 Instalar bs4<br>
1.4 Executar script com python3

<h3>2. Subir arquivo para hdfs</h3>

2.1 Executar no terminal: <br>
<i>hadoop fs -put -f <caminho completo com arquivo final da extração> <pasta destino no hdfs, se houver. Se não passar esse parametro salvará na raiz></i>

<h3>3. Contar palavras</h3>

3.1 Atualizar o script wordCountByBook.pig com o caminho e nome do arquivo salvo no hdfs<br>
3.2 Executar.
