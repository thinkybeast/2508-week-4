import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    database="book_search"
)

cur = conn.cursor()

try:
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS book_chapter (
            id SERIAL PRIMARY KEY,
            book_title TEXT NOT NULL,
            chapter_title TEXT NOT NULL,
            chapter_url TEXT NOT NULL,
            content TEXT NOT NULL,
            embedding vector(1536)
        );
    """)
    conn.commit()
    print("Database setup complete!")
except Exception as e:
    print("Error during setup:", e)
finally:
    cur.close()
    conn.close()