## Count Words by book

### 1. Extraindo dados:

1.1 Salvar arquivos dos livros em uma pasta, descompactado.
1.2 Atualizar caminhos do codigo extrair_arquivos.py para pasta com extração
1.3 Instalar bs4
1.4 Executar script com python3

### 2. Subir arquivo para hdfs

2.1 Executar no terminal: 
```sh
hadoop fs -put -f <caminho completo com arquivo final da extração> <pasta destino no hdfs, se houver. Se não passar esse parametro salvará na raiz>
```
Subir arquivo extraido e stopwords.txt

### 3. Contar palavras

3.1 Atualizar o script wordCountByBook.pig com o caminho e nome do arquivo salvo no hdfs
3.2 Executar.
