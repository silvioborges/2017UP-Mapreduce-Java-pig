Equipe: Lucas Fleck de Souza Castro

Trabalho:
	
 - O trabalho mostra as urls que se repetem em arquivos de um diretório.
 - O Trabalho foi rodado na base lit2go após terem sido removidas tags e elementos HTML, rodando o script 'strip_html.py'.
 - Após a limpeza dos arquivos foi rodado o script em spark 'trabalho_mapreduce.py' com o comando 'spark-submit --master yarn --deploy-mode client --executor-memory 1g --name trabalho --conf "spark.app.id=trabalho" trabalho_mapreduce.py 'dir_name|filename''
 - Os resultados são jogandos em 'trabalho_mapreduce-out'.

Exercicio:

 - Foi escolhido o exercicio 09 (Encontrar o vocabulário de palavras diferente entre 2 livros removendo as palavras que forem encontradas nos dois livros).
 - Executar com `spark-submit --master yarn --deploy-mode client --executor-memory 1g --name exercise09 --conf "spark.app.id=exercise09" exercise09.py 'file1' 'file2'`.
 - A saida sera gerada em exercise09-out
 
 Avaliacao
 * Onde esta o resultado do processamento?
 * Como posso parametrizar o livros que posso ler ?
 
