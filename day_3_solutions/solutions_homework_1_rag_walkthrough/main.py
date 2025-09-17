from rag import ask_study_question

def main():
    """
    Run example study-related questions through the RAG system.
    
    This function:
    1. Defines a list of study-related questions
    2. For each question, calls the ask_study_question function
    3. Prints the question and the answer
    """
    # Define example study-related questions
    questions = [
        "How do I work with JavaScript functions and scope?",
        "What are the basics of Ruby object-oriented programming?",
        "How do I use Git for version control?",
        "What are the fundamentals of SQL queries?"
    ]
    
    # Process each question
    for i, question in enumerate(questions, 1):
        print(f"\n{'='*60}")
        print(f"Question {i}: {question}")
        print(f"{'='*60}")
        
        try:
            answer = ask_study_question(question)
            print(f"\nAnswer:\n{answer}")
        except Exception as e:
            print(f"\nError processing question: {e}")
        
        print(f"\n{'-'*60}")

if __name__ == "__main__":
    main()