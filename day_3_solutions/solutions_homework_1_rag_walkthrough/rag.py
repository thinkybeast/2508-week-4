import os
import openai
from dotenv import load_dotenv
from search import search_similar_chapters

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_study_question(question):
    """
    Implement RAG to answer study-related questions using retrieved context.
    """
    try:
        # 1. Find relevant book chapters
        search_results = search_similar_chapters(question, 3)
        
        if not search_results:
            return "I couldn't find any relevant book chapters to help with your question. Please try rephrasing your question or ask about a different programming topic."
        
        # 2. Format context from search results
        context = "\n".join([
            f"- {result['chapter_title']} from {result['book_title']} (Similarity: {result['similarity_score']:.2f})"
            for result in search_results
        ])
        
        # 3. Create prompt with context
        prompt = f"""
You are a helpful Launch School study assistant. Answer the user's coding question directly using your knowledge about programming and software development. Within your answer, suggest relevant Launch School book chapters where they can learn more about the topic. Make sure to include the chapter URLs in your response.

Available Book Chapters for Reference:
{context}

Question: {question}

Please provide a comprehensive answer to the question, suggesting 1-3 relevant Launch School chapters where the student can study more about this topic.
"""
        
        # 4. Get response from OpenAI
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error in RAG: {e}")
        raise e 

if __name__ == "__main__":
    # Test question
    print(ask_study_question('How do I work with JavaScript functions and scope?'))