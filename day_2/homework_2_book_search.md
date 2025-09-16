# Homework 2: Building a Book Search Application

**Individual Exercise: ~2 hours**

Now that your vector database is set up with Launch School book chapter embeddings, it’s time to build an application that lets users search for relevant book chapters using natural language queries.

## Goal

You'll create a **Book Search Assistant** that allows users to:
1. Enter search queries in natural language
2. Retrieve the most relevant book chapters based on semantic similarity
3. Display results with book titles, chapter titles, and URLs
4. (Optional Bonus): Use an LLM to generate a natural language summary of the results

## System Flow

Your application will roughly follow this pipeline:
1. **User Input** → Accept a natural language query
2. **Query Embedding** → Convert the query into an embedding vector
3. **Vector Search** → Look up the most similar book chapters in your database
4. **Results Display** → Present the top matches with relevant details

## Implementation Guide

You can work in a Jupyter Notebook or a standalone project, your choice.

If you feel comfortable, try building the app from scratch using what you learned in Homework 1. If you'd like more structure, you can follow this suggested plan:

1. Set Up the Project
    - Create a new Poetry project
    - Install any dependencies you'll need
2. Connect to the Database
    - Write a small database helper module/file
    - Add a function that takes a string query and returns the most similar rows
3. Build the User-Facing Application
    - Start with a simple interface (e.g., print/input)
    - Optionally, experiment with a lightweight UI tool like Gradio
    - Display results to the user, including URLs to the relevant chapters
4. Bonus: Add an LLM Layer
    - Instead of showing raw results, send the query + search results + short instructions to an LLM
    - Return a natural language response (e.g., “The most relevant chapters for your query are...”)