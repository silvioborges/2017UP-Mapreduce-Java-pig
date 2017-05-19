
## An introduction to the basics of MapReduce using Hadoop and Java
___


WordCountPath.jar and wordcountcap.jar </br>
<p align="justify">
First of all, you should download of Cloudera VM. After that, you have to put your files (txt) into the Hadoop Distributed File System (HDFS).
</p>

For example: </br>
#hdfs dfs -copyFromLocal /home/cloudera/input </br>
#hdfs dfs -ls /user/cloudera/input</br></br>
Then, execute the algorithm: </br>
#hadoop jar WordCountPath.jar /user/cloudera/input /user/cloudera/output </br>
#hadoop jar wordcountcap.jar /user/cloudera/input /user/cloudera/output
</p>
