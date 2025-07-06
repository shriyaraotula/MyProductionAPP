# MyProductionAPP/wait_for_db.py
import time

import psycopg2
from psycopg2 import OperationalError


def wait_for_postgres(host, db, user, password, port=5432, retries=10, delay=2):
    for attempt in range(retries):
        try:
            print(
                f"🔄 Atmpt {attempt + 1}/{retries}:Cntng PSQL @ {host}:{port} (DB: {db},User:{user})"
            )
            conn = psycopg2.connect(
                host=host,
                dbname=db,
                user=user,
                password=password,
                port=port,
            )
            conn.close()
            print("✅ PostgreSQL is ready!")
            return
        except OperationalError as e:
            print(f"⏳ PostgreSQL not ready ({attempt + 1}/{retries}): {e}")
            time.sleep(delay)
    raise Exception("❌Couldn't connect to PostgreSQL after multiple attempts.")
