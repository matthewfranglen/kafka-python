Python and Kafka
================

This is a demonstration of using python and kafka

Requirements
------------

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
