#### Segue abaixo os exercícios [1](https://github.com/POSBIGDATA/2017UP-Mapreduce-Java-pig/blob/master/entregas/GilmarAraujo-CristianoFontana/exercicios.jpg?raw=true) [2](https://github.com/POSBIGDATA/2017UP-Mapreduce-Java-pig/blob/master/entregas/GilmarAraujo-CristianoFontana/execiciosc.jpg?raw=true) desenvolvidos através do uso da VM Cloudera, onde é realizado a cargo dos dados no sistema de arquivos HDFS, usando linguagem scala no Apache Spark.

</br>
<p align="justify"> 
First of all, you should download of Cloudera VM. After that, you have  to put your files (txt) into the Hadoop Distributed File System (HDFS). 

For example:</br>
#hdfs dfs -copyFromLocal /home/cloudera/input </br>
#hdfs dfs -ls /user/cloudera/input

Then, start the Spark Shell: </br>
#spark-shell
</br>
and, execute the algorithm bellow.
</br> </br>
1 - Count all occurrences of words (removing prepositions and things like that). </br> </br>
val text = sc.textFile("hdfs://localhost:8020/user/cloudera/input/text.txt").cache()</br>
val stopWords = sc.textFile("file:///home/cloudera/stopwords.txt").cache() //stanfordnlp -> CoreNLP</br>
val stopWordSet = stopWords.collect.toSet</br>
val stopWordSetBC = sc.broadcast(stopWordSet) //send to any worker</br>
val words = text.flatMap(str => str.split("\\W")).filter(!_.isEmpty)</br>
val clean = words.mapPartitions{iter =></br>
    val stopWordSet = stopWordSetBC.value</br>
    iter.filter(word => !stopWordSet.contains(word))</br>
}</br>
val wordCount = clean.flatMap(str => str.split(" ")).filter(!_.isEmpty).map(word => (word,1)).reduceByKey( _ + _ )</br>
wordCount.foreach(word => println(word))</br>
wordCount.saveAsTextFile("hdfs://localhost:8020/user/cloudera/output/")</br>

<br>

2 - Count words by book. </br> </br>
val rdd = sc.textFile("hdfs://localhost:8020/user/cloudera/input")</br>
val counts = rdd.flatMap(str => str.split(" ")).filter(!_.isEmpty).map(word => (word, 1)).reduceByKey( _ + _ )</br>
counts.saveAsTextFile("hdfs://localhost:8020/user/cloudera/output")</br>
topWordCount.take(100).foreach(x => println(x))</br>

<br>

3 - Provide a word and show in which files we find the word. </br> </br>
val rdd = sc.wholeTextFiles("file:///home/cloudera/a.txt").cache()</br>
 val files = rdd.map { case (filename, content) => filename}</br>
def doProcess(file: String) = { </br>
	 val word = "z"//input word</br>
	 val rdd2 = sc.textFile(file);</br>
	 val wordFound = rdd2.flatMap(str => str.split(" ")).filter(text => text.contains(word)).collect().mkString(" ");</br>
	 println("Word: %s => filename %s".format(wordFound,file));</br>
}</br>
files.collect.foreach( filename => {</br>
    doProcess(filename)</br>
}) </br>

<br>

4- Provide a palvra and show in which files we find the word and amount of occurrences. </br> </br>
val rdd = sc.wholeTextFiles("hdfs://localhost:8020/user/cloudera/input")</br>
val files = rdd.map { case (filename, content) => filename}</br>
def doProcess(file: String) = { </br>
	 val word = "z"//input word</br>
	 val rdd2 = sc.textFile(file);</br>
	 val wordFoundCount = text.flatMap(str => str.split(" ")).filter(text => text.contains(word)).map(word => (word, 1)).reduceByKey(_+_).collect().mkString(" ");</br>
	 println("Word, total: %s => filename %s".format(wordFoundCount,file));</br>
}</br>
files.collect.foreach( filename => {</br>
    doProcess(filename)</br>
}) </br>

<br>

5 - Find the 1500 most used words in all books. </br> </br>
val rdd = sc.textFile("hdfs://localhost:8020/user/cloudera/input/*")</br>
val topWordCount = rdd.flatMap(str => str.split(" ")).filter(!_.isEmpty).map(word => (word,1)).reduceByKey( _ + _).map{case (word, count) => (count, word)}.sortByKey(false)</br>
topWordCount.saveAsTextFile("hdfs://localhost:8020/user/cloudera/output")</br>
topWordCount.take(1500).foreach(x => println(x))</br>

<br>

6 - Find the 1500 most used words in 1 book. </br> </br>
val rdd = sc.textFile("hdfs://localhost:8020/user/cloudera/input")</br>
val topWordCount = rdd.flatMap(str => str.split(" ")).filter(!_.isEmpty).map(word => (word,1)).reduceByKey( _ + _ ).map{case (word, count) => (count, word)}.sortByKey(false)</br>
topWordCount.saveAsTextFile("hdfs://localhost:8020/user/cloudera/output")</br>
topWordCount.take(10).foreach(x => println(x))</br>

<br>

7- Find the 1500 least used words. </br> </br>
val rdd = sc.textFile("hdfs://localhost:8020/user/cloudera/input/*")</br>
val rddone = sc.textFile("hdfs://localhost:8020/user/cloudera/input/")</br>
val topWordCount = rdd.flatMap(str => str.split(" ")).filter(!_.isEmpty).map(word => (word,1)).reduceByKey( _ + _ ).map{case (word, count) => (count, word)}.sortByKey()</br>
topWordCount.saveAsTextFile("hdfs://localhost:8020/user/cloudera/output")</br></br>
topWordCount.take(1500).foreach(x => println(x))</br>

<br>

8 - Find the common vocabulary of 1500 words between 2 books. </br> </br>
val file1 = sc.textFile("hdfs://localhost:8020/user/cloudera/input")</br>
val file2 = sc.textFile("hdfs://localhost:8020/user/cloudera/input")</br>
val book1 = file1.flatMap(str => str.split(" ")).map(word => (word, 1)).reduceByKey( _ + _ )</br>
val book2 = file2.flatMap(str => str.split(" ")).map(word => (word, 1)).reduceByKey( _ + _ )</br>
val result = book1.intersection(book2)</br>
result.saveAsTextFile("hdfs://localhost:8020/user/cloudera/output")</br>
result.take(1500).foreach(x => println(x))</br>

<br>

9- Find the different word vocabulary of each book between 2 books, and remove the words that are found in both books. </br> </br>
val file1 = sc.textFile("hdfs://localhost:8020/user/cloudera/input")</br>
val file2 = sc.textFile("hdfs://localhost:8020/user/cloudera/input")</br>
val book1 = file1.flatMap(str => str.split(" ")).map(word => (word, 1)).reduceByKey( _ + _ )</br>
val book2 = file2.flatMap(str => str.split(" ")).map(word => (word, 1)).reduceByKey( _ + _ )</br></br>
val result = book1.subtractByKey(book2)</br>
val temp = data.union(data1)</br>
val rem = temp.subtractByKey(res)</br>
rem.saveAsTextFile("hdfs://localhost:8020/user/cloudera/output")</br>
rem.take(10).foreach(x => println(x))</br>


</p>
