Python and Kafka
================

This is a demonstration of using python and kafka

Requirements
------------

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
