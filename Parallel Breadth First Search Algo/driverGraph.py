import subprocess
import shlex

count = 0 
command="/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar -D stream.num.map.output.key.fields=2 -D mapred.text.key.partitioner.options=-k1,1 -D mapred.reduce.tasks=4 -input /user/graph.txt -output /output_"+str(count)+" -file /home/ubuntu/mapperGraph.py -file /home/ubuntu/reducerGraph.py -mapper mapperGraph.py -reducer reducerGraph.py -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner"

while (True):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = process.communicate()
    print ("\n"+str(err)+"\n")
    if "toBeProcessedCounter" not in str(err):
        break
    count = count + 1
    command="/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar -D stream.num.map.output.key.fields=2 -D mapred.text.key.partitioner.options=-k1,1 -D mapred.reduce.tasks=4 -input /output_"+str(count-1)+"/* -output /output_"+str(count)+" -file /home/ubuntu/mapperGraph.py -file /home/ubuntu/reducerGraph.py -mapper mapperGraph.py -reducer reducerGraph.py -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner"
    