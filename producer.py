#!/usr/bin/env python
# coding=utf-8
import pika
# логин и пароль от УЗ, под которой будем работать
credentials = pika.PlainCredentials('str', 'qwerty')
# ip адрес и порт rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.148',5672,'/',credentials))
channel = connection.channel()
#Создаем очередь
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
connection.close()
