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
        pass
        # TODO: 1. Find relevant book chapters

        # TODO: 2. Format context from search results
        
        # TODO: 3. Create prompt with context

        # TODO: 4. Get response from OpenAI
    
    except Exception as e:
        print(f"Error in RAG: {e}")
        raise e 

if __name__ == "__main__":
    # Test question
    print(ask_study_question('How do I work with JavaScript functions and scope?'))