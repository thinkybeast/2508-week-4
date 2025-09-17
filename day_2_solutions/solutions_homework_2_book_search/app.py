import gradio as gr
from book_search import search_similar_chapters
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def search_books(query):
    """Search for book chapters and format results for display"""
    if not query.strip():
        return "Please enter a search query."
    
    results = search_similar_chapters(query, top_k=5)
    
    if not results:
        return "No results found for your query."
    
    # Generate LLM summary of the results
    try:
        # Prepare the results for the LLM
        results_text = ""
        for i, result in enumerate(results, 1):
            results_text += f"{i}. {result['book_title']}: {result['chapter_title']}\n"
            results_text += f"   URL: {result['chapter_url']}\n\n"
        
        # Create prompt for the LLM
        prompt = f"""
        A user searched for: "{query}"
        
        Here are the most relevant Launch School book chapters found:
        
        {results_text}
        
        Please provide a helpful, conversational response that incorporates the relevant URLs within the conversation. You should:
        1. Acknowledge their search query
        2. Identify chapters that are relevant and point them to them, suggesting what they'll find in these chapters
        3. Encourage them to explore the provided URLs
        
        Keep the response friendly and informative, around 2-3 sentences.
        """
        
        # Get LLM response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "developer", "content": "You are a helpful assistant that helps users find relevant educational content from Launch School books."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        llm_summary = response.choices[0].message.content.strip()
        
        return llm_summary
        
    except Exception as e:
        # Fallback to original format if LLM fails
        print(f"LLM error: {e}")
        output = f"Found {len(results)} results for: '{query}'\n\n"
        
        for i, result in enumerate(results, 1):
            output += f"**{i}. {result['book_title']}**\n"
            output += f"Chapter: {result['chapter_title']}\n"
            output += f"URL: {result['chapter_url']}\n"
            output += f"Similarity: {result['similarity_score']:.3f}\n\n"
        
        return output

# Create the Gradio interface
with gr.Blocks(title="Book Search Assistant") as demo:
    gr.Markdown("# 📚 Book Search Assistant")
    gr.Markdown("Search for relevant Launch School book chapters using natural language queries.")
    
    with gr.Row():
        with gr.Column():
            query_input = gr.Textbox(
                label="Search Query",
                placeholder="Enter your search query here...",
                lines=2
            )
            search_button = gr.Button("Search", variant="primary")
        
        with gr.Column():
            results_output = gr.Markdown(label="Results")
    
    # Connect the search function
    search_button.click(
        fn=search_books,
        inputs=[query_input],
        outputs=results_output
    )
    
    # Allow Enter key to trigger search
    query_input.submit(
        fn=search_books,
        inputs=[query_input],
        outputs=results_output
    )

if __name__ == "__main__":
    demo.launch()
