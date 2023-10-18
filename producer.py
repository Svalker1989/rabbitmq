#!/usr/bin/env python
# coding=utf-8
import pika
credentials = pika.PlainCredentials('str', 'qwerty')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.148',5672,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
connection.close()
