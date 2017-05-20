# **Contagem de palavras eliminando preposições utilizando Python e Hadoop Streaming**

## Objetivo
Contar a ocorrência de palavras contidas nos livros do site lit2go, eliminando as preposicoes encontradas e exibir de forma ordenada pelo número de ocorrências.

## Origem dos dados
Foi utilizada uma amostra da base de dados do site lit2go que contém livros em arquivos HTML.

## Etapas necessárias
 - Extrair o texto de cada um dos livros presentes nos arquivos HTML e gravar em um único arquivo TXT
 - Contar palavras executando o MapReduce do Hadoop Streaming

## Arquivos do repositório
 - **lit2go.ok.rar** - Contém a base de dados conforme descrito acima em "Origem dos dados"
 - **html2text.py** - Programa Python que extrai o texto dos livros contidos na base e devolve um arquivo TXT contendo o conteúdo de todos os livros, livre de preposições
 - **countMap.py** - Programa Python que manipula o Mapper do MapReduce
 - **countReduce.py** - Programa Python que manipula o Reducer do MapReduce
 - **livros.txt** - Arquivo que exemplifica a saída do arquivo html2text.py
 - **part-00000** - Arquivo que exemplifica a saída da execução do MapReduce no Hadoop Streaming
 
## Pré-Requisitos
 - Para realizar a extração do conteúdos dos arquivos HTML da base de dados o código Python foi desenvolvido na versão 3.4, portando Python3.4 (ou superior) é necessário para sua execução
- As bibliotecas Python BS4, NLTK, REQUESTS são necessárias para a execução dos códigos. Instrução para instalação:
- **INSTALAÇÃO NO PYTHON 3.4:**
  - sudo pip3 install -U nltk
  - sudo pip3 install requests
 -- após a instalação das 2 bibliotecas acima baixe a base de dados do nltk conforme descrito na documentação da biblioteca no seguinte link: http://www.nltk.org/data.html
  - sudo pip3 install beautifulsoup4

## **Instruções de execução**
- Colocar os arquivos do repositório na mesma pasta.
- Extrair o conteudo do arquivo lit2go.ok.tar.gz que contem os livros
- Configurar o arquivo html2text.py informando o valor das variáveis **livros** e **saida** colocando, respectivamente, o caminho da pasta que contem os livros e o caminho da pasta onde o programa python depositará o arquivo TXT final que conterá o conteúdo dos textos do livro livre de preposições.
- Executar o arquivo html2text.py a partir da pasta onde o arquivo está contido, conforme abaixo:
```sh
python3 html2text.py
```
- Ao final o programa exibirá a seguinte mensagem:
```sh
arquivos processados!
```
- Crie um diretório no HDFS para colocar os arquivos de INPUT e OUTPUT do processamento do JOB, usando o comando abaixo:
```sh
hdfs dfs -mkdir /caminhoDiretorioNoHDFS
```
- Subir o arquivo de TXT de saída para o HDFS no diretório recém criado, utilizando o comando abaixo:
```sh
hdfs dfs -put /caminhoLocalParaOArquivoTXT /caminhoDiretorioNoHDFS
```
- Executar o Hadoop Streaming referenciando os arquivos **countMap.py** e **reduceMap.py**. Conforme abaixo:
(*Atenção ambos arquivos foram desenvolvidos utilizando Python3 e portanto deverão ser executados também nesta versão). 
```sh
hadoop \
    jar /usr/lib/hadoop-mapreduce/hadoop-streaming-*.jar \
    -D mapreduce.job.name="Hadoop_Streaming_WordCount" \
    -D mapreduce.map.memory.mb=4096 \
    -D mapred.reduce.tasks=1 \
    -mapper "python3 /home/cloudera/bigdata/hadoop_streaming_mapred/countMap.py" \
    -reducer "python3 /home/cloudera/bigdata/hadoop_streaming_mapred/countReduce.py" \
    -input "/caminhoDiretorioNoHDFS/livros.txt" \
    -output "/caminhoDiretorioNoHDFS/wordcount_livros/"
```
- Entendo os parâmetros do código acima:
 

| Parâmetro | Explicação |
| ------ | ------ |
| hadoop | inicia o Hadoop |
| jar /usr/lib/hadoop-mapreduce/hadoop-streaming-*.jar | Informa o arquivo .JAR responsável pela execução do Hadoop Streaming. Este arquivo está disponível na distribuição padrão do Hadoop na pasta que contém as libs instaladas |
| -D mapreduce.job.name="Hadoop_Streaming_WordCount" | Define o nome do Job |
| -D mapreduce.map.memory.mb=4096 | Define a memória para execução do MapReduce. 4096mb será necessário para a execução deste exercício |
| -D mapred.reduce.tasks=1 | Define a quantidade de Reduces do JOB. 1 Reduce é ideal para a base de dados utilizada neste exercício |
| -mapper "python3 /home/cloudera/bigdata/hadoop_streaming_mapred/countMap3.py" | Executa o arquivo countMap.py apontando o caminho completo até o arquivo. Este script Python define o escopo do Map |
| -reducer "python3 /home/cloudera/bigdata/hadoop_streaming_mapred/countReduce3.py" | Executa o arquivo countReduce.py apontando o caminho completo até o arquivo. Este script Python define o escopo do Reduce |
| -input "/caminhoDiretorioNoHDFS/livros.txt" | Define o arquivo que será processado no MapReduce. Informar aqui o caminho até o arquivo que foi colocado no HDFS no passo anterior e que contém o conteúdo dos livros |
| -output "/caminhoDiretorioNoHDFS/wordcount_livros/ | Define o caminho no HDFS onde o Hadoop colocará o arquivo contendo a contagem de palavras |
- Após o processamento vá até a pasta wordcount_livros dentro do diretório criado no HDFS nos passos anteriores e abra o arquivo **part-00000** para visualizar a contagem de palavras. 
