install-spark:
	sudo wget https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz --no-check-certificate
	mkdir /opt/spark
	sudo mv spark-3.5.0-bin-hadoop3.tgz /opt/spark/
	tar -zxvf /opt/spark/spark-3.5.0-bin-hadoop3.tgz -C /opt/spark

install-python3:
	sudo yum install -y python3
	sudo unlink /usr/bin/python
	sudo ln -s /usr/bin/python3 /usr/bin/python
 
start-namenode:
	hdfs namenode

install-zeppelin:
	sudo wget https://dlcdn.apache.org/zeppelin/zeppelin-0.11.2/zeppelin-0.11.2-bin-all.tgz
	mkdir -p /opt/zeppelin
	sudo tar zxvf zeppelin-0.11.2-bin-all.tgz --strip-components=1 -C /opt/zeppelin
	sudo cp /opt/zeppelin/conf/zeppelin-env.sh.template /opt/zeppelin/conf/zeppelin-env.sh
	echo 'export JAVA_HOME=/usr/lib/jvm/jre/' | sudo tee -a /opt/zeppelin/conf/zeppelin-env.sh > /dev/null
	echo 'export ZEPPELIN_ADDR=0.0.0.0' | sudo tee -a /opt/zeppelin/conf/zeppelin-env.sh > /dev/null
	echo 'export SPARK_HOME=/opt/spark/spark-3.5.0-bin-hadoop3' | sudo tee -a /opt/zeppelin/conf/zeppelin-env.sh > /dev/null
	sudo /opt/zeppelin/bin/zeppelin-daemon.sh start
