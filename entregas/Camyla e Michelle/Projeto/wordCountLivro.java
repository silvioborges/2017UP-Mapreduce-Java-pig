import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.Reducer.Context;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class WordCountLivro {

	public static class Map extends
			Mapper<LongWritable, Text, Text, IntWritable> {
		private final static IntWritable one = new IntWritable(1);

		public void map(LongWritable key, Text value, Context context)
				throws java.io.IOException, InterruptedException {
			String[] prepositions = { "the", "in", "on", "at", "after",
					"around", "before", "by", "between", "for", "from", "to",
					"against", "around", "near", "and" };

			
			String arquivo = value.toString();
			// split por | para pegar o nome do livro
			String[] titulo = arquivo.split("\\|");
			// Segunda posição do array
			String nomeLivro = titulo[1];
			//corpo livro
			String texto = titulo[3];		
				
			String[] values = texto.split(" ");
						
			int size = values.length;
			Boolean preposicao = false;
			for (int i = 0; i < size; i = i + 1) {
				for (int j = 0; j < prepositions.length; j = j + 1) {
					// Verifica se é preposição
					if (values[i].trim().equals(prepositions[j])) {
						preposicao = true;
					}
				}// se não for preposição, salva no arquivo
				if (preposicao == false) {
					Text k = new Text(nomeLivro);
					context.write(k, one);
					// se for preposição, reseta a variável para a prox.
				} else {
					preposicao = false;
				}

			}

		}
	}

	public static class Reduce extends
			Reducer<Text, IntWritable, Text, IntWritable> {

		public void reduce(Text key, Iterable<IntWritable> values,
				Context context) throws IOException, InterruptedException {
			int sum = 0;
			// key= new Text("total");
			for (IntWritable val : values) {
				sum += val.get();
			}
			context.write(key, new IntWritable(sum));
		}
	}

	public static void main(String[] args) throws IOException,
			ClassNotFoundException, InterruptedException {
		// TODO Auto-generated method stub

		Configuration conf = new Configuration();

		Job job = new Job(conf, "wordCountLivro");
		job.setJarByClass(WordCountLivro.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

		job.setMapperClass(Map.class);
		job.setReducerClass(Reduce.class);

		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);

		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));

		job.waitForCompletion(true);
	}

}
