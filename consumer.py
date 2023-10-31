#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('str', 'qwerty')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.174',5672,'/',credentials))
channel = connection.channel()
# Создаем очередь
channel.queue_declare(queue='hello')
#  Вызываем callback функцию, которая подписана на очередь
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
# Указываем что функция callback должна принимать сообщения из очереди hello
channel.basic_consume('hello', callback, auto_ack=True)
channel.start_consuming()
