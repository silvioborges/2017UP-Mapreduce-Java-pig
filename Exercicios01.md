Exercicios.md

Exercícios 01
Data a sequinte entrada de dados (Card1.txt): 

-- Conteudo
DIAMONDS 3
sPADes Jack
hearts 3
hearts 2
hearts Ace
JOKER JOKER
DIAMONDS Queen
spades 3
hearts 6
spades 10
cLUbs 8
HeARts 7
SpAdEs 4
Diamonds 6
Diamonds 3
HEARTS 8
diamonds 7
CLUBs 4
Diamonds 7
Spades 9
clubS 7
SPADES 5
diamonds 10
DiamONDs King


Crie um MapReduce Java que capitalise as palavras e sumarise os valores de todas as chaves e escreva o resultado no file sistem do Hadopp. 
O resultado deverá ser : 
•	clubs 19
•	diamonds 36
•	hearts 26
•	spades 31


Exercício 2
Data as seguintes entradas Card1.txt (do exercio anterior)
•	Card2.txt com o seguinte conteúdo:
Carro casa 
Haddop data prossesing
JACK joker diamonds 
Universidade positivo 
Crie um MapReduce que seja capaz gerar uma saída com o seguinte formato :
<WORD> <FILE> <COUNT> , <FILE> <COUNT>,<FILE> <COUNT> ... 
WORD  é “PALAVRA” encontrada no arquivo 
FILE é o caminho + o nome do arquivo 
COUNT é a quantidade de ocorrências da palavra no arquivo

