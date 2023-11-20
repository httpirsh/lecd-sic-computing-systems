#!/usr/bin/env python
# reads messages from the test topic

from kafka import KafkaConsumer

if __name__ == '__main__':
    print("Starting consumer script...")
    consumer = KafkaConsumer(bootstrap_servers='192.168.23.130:9093')
    print("KafkaConsumer passed!")
    consumer.subscribe(['sic-topic'])
    print("Subscribed to the topic!")
    print("Waiting for message...")

for msg in consumer:
    print("Msg: " + msg.value.decode('utf-8'))
    print("Waiting for message...")
    print("Ending script!")