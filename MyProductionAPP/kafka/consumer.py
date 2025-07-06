# MyProductionAPP/kafka/consumer.py
from kafka import KafkaConsumer
import json
import os
import time

#KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"
TOPIC_NAME = os.getenv("KAFKA_TOPIC", "orders")

import uuid

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    group_id=f"order-consumer-group-{uuid.uuid4()}",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)


def process_order(order):
    print(f"🛒 Processing order: {order}")
    time.sleep(1)
    print(f"✔️ Done: {order['order_id']}")

def start_consumer():
    print("📥 Kafka Consumer started...")
    for message in consumer:
        print(f"Received raw message: {message}")
        process_order(message.value)


if __name__ == "__main__":
    start_consumer()
