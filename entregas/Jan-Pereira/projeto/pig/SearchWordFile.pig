--ex: pig -f SearchWordFile.pig -param keyword=child -param input=fullbooks -param output=fullbooks/output/search

set pig.splitCombination false;

file = load '$input' using PigStorage(',','-tagFile') as (filename, txt:chararray);

words = FOREACH file GENERATE filename, FLATTEN(TOKENIZE(txt)) AS word;

filtered_words = FILTER words BY word MATCHES '\\w+';

filtered_words = FILTER filtered_words BY word MATCHES '$keyword';

word_groups = GROUP filtered_words BY (filename, word);

word_groups = FOREACH word_groups GENERATE group;

STORE word_groups INTO '$output/$keyword';

DUMP word_groups;
