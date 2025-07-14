# MyProductionAPP/kafka/consumer.py
import json
import os
import time
import uuid
from kafka import KafkaConsumer

def process_order(order):
    print(f"🛒 Processing order: {order}")
    time.sleep(1)
    print(f"✔️ Done: {order['order_id']}")


def start_consumer():
    if os.getenv("ENABLE_KAFKA", "1") == "0":
        print("🛑 Kafka consumer is disabled via ENABLE_KAFKA=0")
        return

    print("📥 Kafka Consumer starting...")
    kafka_bootstrap = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
    topic = os.getenv("KAFKA_TOPIC", "orders")

    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=kafka_bootstrap,
        group_id=f"order-consumer-group-{uuid.uuid4()}",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    )

    for message in consumer:
        print(f"📦 Received message: {message.value}")
        process_order(message.value)


if __name__ == "__main__":
    start_consumer()
