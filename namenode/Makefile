ZEPPELIN_HOME=/opt/zeppelin
SPARK_HOME=/opt/spark/spark-3.5.0-bin-hadoop3

install-spark:
	if [ ! -d "$(SPARK_HOME)" ]; then \
		echo "Spark not found. Downloading and installing..."; \
		sudo wget https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz --no-check-certificate -O /tmp/spark.tgz; \
		mkdir -p /opt/spark; \
		sudo tar -zxvf /tmp/spark.tgz -C /opt/spark; \
		rm -f /tmp/spark.tgz; \
	else \
		echo "Spark is already installed."; \
	fi

install-python3:
	if ! command -v python3 > /dev/null 2>&1; then \
		echo "Python 3 not found. Installing..."; \
		sudo yum install -y python3; \
		if [ -L /usr/bin/python ]; then \
			sudo unlink /usr/bin/python; \
		fi; \
		sudo ln -s /usr/bin/python3.6 /usr/bin/python; \
	else \
		echo "Python 3 is already installed."; \
	fi

install-zeppelin:
	if [ ! -f "$(ZEPPELIN_HOME)/conf/zeppelin-env.sh" ]; then \
		echo "Zeppelin not configured. Downloading and installing..."; \
		sudo wget https://dlcdn.apache.org/zeppelin/zeppelin-0.11.2/zeppelin-0.11.2-bin-all.tgz -O /tmp/zeppelin.tgz; \
		mkdir -p $(ZEPPELIN_HOME); \
		sudo tar zxvf /tmp/zeppelin.tgz --strip-components=1 -C $(ZEPPELIN_HOME); \
		rm -f /tmp/zeppelin.tgz; \
		sudo cp $(ZEPPELIN_HOME)/conf/zeppelin-env.sh.template $(ZEPPELIN_HOME)/conf/zeppelin-env.sh; \
		echo 'export JAVA_HOME=/usr/lib/jvm/jre/' | sudo tee -a $(ZEPPELIN_HOME)/conf/zeppelin-env.sh > /dev/null; \
		echo 'export ZEPPELIN_ADDR=0.0.0.0' | sudo tee -a $(ZEPPELIN_HOME)/conf/zeppelin-env.sh > /dev/null; \
		echo 'export SPARK_HOME=$(SPARK_HOME)' | sudo tee -a $(ZEPPELIN_HOME)/conf/zeppelin-env.sh > /dev/null; \
		echo 'export PYSPARK_PYTHON=/usr/bin/python3.6' | sudo tee -a $(ZEPPELIN_HOME)/conf/zeppelin-env.sh > /dev/null; \
		echo 'export PYSPARK_DRIVER_PYTHON=/usr/bin/python3.6' | sudo tee -a $(ZEPPELIN_HOME)/conf/zeppelin-env.sh > /dev/null; \
		sudo /opt/zeppelin/bin/zeppelin-daemon.sh start; \
	else \
		echo "Zeppelin is already configured."; \
		echo 'export JAVA_HOME=/usr/lib/jvm/jre/' | sudo tee -a $(ZEPPELIN_HOME)/conf/zeppelin-env.sh > /dev/null; \
		echo 'export ZEPPELIN_ADDR=0.0.0.0' | sudo tee -a $(ZEPPELIN_HOME)/conf/zeppelin-env.sh > /dev/null; \
		echo 'export SPARK_HOME=$(SPARK_HOME)' | sudo tee -a $(ZEPPELIN_HOME)/conf/zeppelin-env.sh > /dev/null; \
		echo 'export PYSPARK_PYTHON=/usr/bin/python3.6' | sudo tee -a $(ZEPPELIN_HOME)/conf/zeppelin-env.sh > /dev/null; \
		echo 'export PYSPARK_DRIVER_PYTHON=/usr/bin/python3.6' | sudo tee -a $(ZEPPELIN_HOME)/conf/zeppelin-env.sh > /dev/null; \
		sudo /opt/zeppelin/bin/zeppelin-daemon.sh start; \
	fi

start-namenode:
	hdfs namenode \
