#### O exemplo a seguir foi executado em uma VM Cloudera, carregando arquivos .txt de livros extraidos de paginas html no Hadoop Distributed File System (HDFS). Usando linguagem scala no Apache Spark.

##### Exemplo: 
* hdfs dfs -copyFromLocal 

* /home/cloudera/input #hdfs dfs -ls
* /user/cloudera/input

##### Inicia spark shell: 
* spark-shell 
###### Execure o algoritimo a seguir:

val rdd = sc.textFile("hdfs://localhost:8020/user/cloudera/input/*") val rddone = sc.textFile("hdfs://localhost:8020/user/cloudera/input/") val topWordCount = rdd.flatMap(str => str.split(" ")).filter(!_.isEmpty).map(word => (word,1)).reduceByKey( _ + _ ).map{case (word, count) => (count, word)}.sortByKey() topWordCount.saveAsTextFile("hdfs://localhost:8020/user/cloudera/output")

topWordCount.take(1500).foreach(x => println(x))
