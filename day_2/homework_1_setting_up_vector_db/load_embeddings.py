import os
import json
from openai import OpenAI
import psycopg2
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_book_data():
    """Load book chapter data from JSON file"""
    with open('book_chapter_data.json', 'r') as file:
        return json.load(file)

def generate_embeddings(batch_size=100):
    # Connect to Postgres
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        database="book_search"
    )
    cursor = conn.cursor()

    try:
        book_chapters = load_book_data()
        
        # Process chapters in batches
        for i in range(0, len(book_chapters), batch_size):
            batch = book_chapters[i:i + batch_size]
            
            # Prepare batch data
            batch_contents = []
            batch_metadata = []
            
            for chapter in batch:
                # Create content string combining book title and chapter title
                content = f"{chapter['book_title']}: {chapter['chapter_title']}"
                batch_contents.append(content)
                batch_metadata.append({
                    'book_title': chapter['book_title'],
                    'chapter_title': chapter['chapter_title'],
                    'chapter_url': chapter['chapter_url'],
                    'content': content
                })
            
            # Create embeddings for the entire batch
            response = client.embeddings.create(
                model="text-embedding-3-small",
                input=batch_contents
            )
            
            # Store each embedding with its metadata
            for j, embedding_data in enumerate(response.data):
                metadata = batch_metadata[j]
                embedding = embedding_data.embedding
                
                cursor.execute(
                    """INSERT INTO book_chapter 
                       (book_title, chapter_title, chapter_url, content, embedding) 
                       VALUES (%s, %s, %s, %s, %s)""",
                    (metadata['book_title'], metadata['chapter_title'], 
                     metadata['chapter_url'], metadata['content'], embedding)
                )
                print(f"Stored embedding for: {metadata['content'][:50]}...")
            
            print(f"Processed batch {i//batch_size + 1}/{(len(book_chapters) + batch_size - 1)//batch_size}")

        conn.commit()
        print("All embeddings stored successfully!")

    except Exception as e:
        print("Error generating embeddings:", e)

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    generate_embeddings()