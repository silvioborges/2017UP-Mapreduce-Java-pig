A = load '/user/cloudera/the-adventure_minusculo.txt';

-- load the stop words list
SW = load '/user/cloudera/the-adventure_minusculo.txt' as (stopword:chararray);    

B = foreach A generate flatten(TOKENIZE((chararray)$0)) as word;

-- join the data with a left outer join
-- using replicated should be done with the right relation (SW) is small
SW2 = join B by word LEFT OUTER, SW by stopword USING 'replicated';

-- filter out where the stopword is null, meaning it is not in the stopword list
C = filter SW2 by stopword IS NULL;

-- remove the stopword column that we don't need.
C = foreach C generate word;

D = group C by word;

E = foreach D generate COUNT(C) as count, group as word;

F = order E by count desc;

store F into '/user/cloudera/the-adventure-saida-3';

