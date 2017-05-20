%declare file 'input/livros3.txt'
%declare stopwords 'input/stopwords.txt'
%declare file_out 'out/'

--importa dados
livros = LOAD '$file' USING PigStorage('|') AS (caminho:chararray,livro:chararray,capitulo:chararray,texto:chararray);
describe livros;

--separa palavras
words = FOREACH livros GENERATE livro, FLATTEN(TOKENIZE(texto)) as word;

--carregas palavras vazias
sw = LOAD '$stopwords' USING PigStorage() AS (sw:chararray);
stopwords = FOREACH sw GENERATE FLATTEN(TOKENIZE(sw)) as sw;

--cruza informações
j = JOIN stopwords BY sw RIGHT OUTER, words BY word;

--retira stopwords
words2 = FILTER j BY sw IS NULL;
words3 = FOREACH words2 GENERATE livro, word;

grouped = GROUP words3 BY livro;

--conta agrupando por livro
wordcount = FOREACH grouped GENERATE group, COUNT(words3) as count;

--visualiza alguns dados
--toDisplay = LIMIT wordcount  50;
--dump toDisplay;

--ordena
wordCountOrder = ORDER wordcount BY group;

--salva dados no hdfs
rmf $file_out
STORE wordCountOrder INTO '$file_out' using PigStorage(';');


--hadoop fs -cat result.txt out/part-r-00000.txt
