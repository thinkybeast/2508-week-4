import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = "book_search"

def check_database():
    """Check if we can connect to the database and if the book_chapter table exists."""
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            user="postgres",
            database=DATABASE_NAME
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM book_chapter;")
        count = cursor.fetchone()[0]
        print(f"Found {count} book chapters in database")
        
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise e
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    check_database() 