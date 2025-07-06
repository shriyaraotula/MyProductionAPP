# MyProductionAPP/kafka/producer.py
import json
import os

from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
TOPIC_NAME = os.getenv("KAFKA_TOPIC", "orders")

# Lazy init: only create the producer when needed
_kafka_producer = None


def get_kafka_producer():
    global _kafka_producer
    if _kafka_producer is None:
        _kafka_producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
    return _kafka_producer


def send_order_to_kafka(order_data: dict):
    producer = get_kafka_producer()
    producer.send(TOPIC_NAME, value=order_data)
    producer.flush()
    print(f"✅ Sent to Kafka: {order_data}")
