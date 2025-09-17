import os
import psycopg2
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_db_connection():
    """Create and return a database connection"""
    return psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        database="book_search"
    )

def search_similar_chapters(query, top_k=5):
    """
    Search for book chapters similar to the given query
    
    Args:
        query (str): Natural language search query
        top_k (int): Number of top results to return
    
    Returns:
        list: List of dictionaries containing chapter information
    """
    # Generate embedding for the query
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=[query]
    )
    query_embedding = response.data[0].embedding
    
    # Connect to database and search
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Use cosine similarity to find most similar chapters
        cursor.execute("""
            SELECT book_title, chapter_title, chapter_url, content,
                   embedding <=> %s::vector as distance
            FROM book_chapter
            ORDER BY distance
            LIMIT %s
        """, (query_embedding, top_k))
        
        results = []
        for row in cursor.fetchall():
            results.append({
                'book_title': row[0],
                'chapter_title': row[1],
                'chapter_url': row[2],
                'content': row[3],
                'similarity_score': 1 - row[4]  # Convert distance to similarity
            })
        
        return results
        
    except Exception as e:
        print(f"Error searching database: {e}")
        return []
    
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    # Test the search functionality
    print("Testing book search functionality...")
    
    test_query = "JavaScript functions and scope"
    print(f"\nSearching for: '{test_query}'")
    
    results = search_similar_chapters(test_query, top_k=3)
    
    if results:
        print(f"\nFound {len(results)} results:")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result['book_title']}")
            print(f"   Chapter: {result['chapter_title']}")
            print(f"   URL: {result['chapter_url']}")
            print(f"   Similarity: {result['similarity_score']:.3f}")
    else:
        print("No results found.")