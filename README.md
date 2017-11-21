Python and Kafka
================

This is a demonstration of using python and kafka

Running
-------

Start this with docker-compose:

```bash
docker-compose up
```

Once the docker containers are running you can use the following commands:

### Console Producer

This reads from standard in and writes each line to kafka as a separate message:

```bash
echo hello | ./console-producer.py
```

### Console Consumer

This reads from kafka and writes each message to standard out:

```bash
./console-consumer.py
```

### Elastic Search Consumer

This reads from kafka and writes each message to elasticsearch:

```bash
./elasticsearch-consumer.py
```

You can view the written documents [by searching for them](http://localhost:9200/example/_search?pretty).

Requirements
------------

This was written for python 3.6.2.

### Dependencies

This needs librdkafka:

```bash
wget -qO - http://packages.confluent.io/deb/3.3/archive.key | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] http://packages.confluent.io/deb/3.3 stable main"
sudo apt-get update
sudo apt-get install librdkafka-dev python-dev
```

or

```bash
sudo brew install librdkafka
```

### Kafka Advertised Hostname

This has to be correct. If it is not then it will manifest itself as writers that cannot flush.

If this has happened then run the following command and replace the value of KAFKA_ADVERTISED_HOST_NAME in docker-compose.yml:

```
docker exec -ti kafkapython_kafka_1 /sbin/ip route|awk '/default/ { print $3 }'
```
