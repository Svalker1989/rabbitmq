#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('str', 'qwerty')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.148',5672,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume('hello', callback, auto_ack=True)
channel.start_consuming()
