
* Link do artigo traduzido: https://software.intel.com/sites/default/files/article/402274/etl-big-data-with-hadoop.pdf

* Nosso desafio:  Contar todas as palavras de um livro.

* Livro escolhido para teste: The-adventure.txt

* Resultado optido está em: resultado.txt

* Código utilizado: conta_palavra_livro.pig

* Como executar o código:
	- O código em questão foi feito em PIG, e para executar o mesmo é necessário um equipamento onde o PIG está totalmente funcional.
	- Não será contemplado a configuração do  equipamento, entendemos que aquestão do ambiente deverá ser tratado em separado.
	
	
	- Baixar o script "conta_palavra_livro.pig" e executar o mesmo com o comando : pig conta_palavra_livro.pig
	- Carregar o arquivo "The-adventure.txt" no hadoop;
	- Executar o script "conta_palavra_livro.pig"
	
	*Caso não utilize os arquivos fornecidos, será necessário efetuar alterações no script. Abaixo segue os passos para alteração*
	
	- Editar o script "conta_palavra_livro.pig" e alterar:
		-- linha 1 : informar o arquivo original que será contabilizado;
		-- linha 4 : informar o arquivo original que será contabilizado;
		-- linha 24: informar o arquivo de resultado;
		-- OBS: informar o "path" completo até os arquivos;
	- O resultado será gravado no local informado na linha 24 do script.

	
* O arquivo de texto do livro necessita estar em formato TXT e o conteúdo deve estar em "lowercase"(todo em minúsculo)
