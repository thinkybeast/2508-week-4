# Retrieval Augmented Generation (RAG) Lab

> ⚠️ Note: This lab is _optional_. If you feel confident and are ready to start working on your own RAG project, you can skip this lab. If you'd like practice pulling all of the various RAG components together, you can work through this lab as much as you'd like. Much of the code here is pulled from day 2 labs.

In this lab, we'll walk you through a Python application that implements Retrieval Augmented Generation (RAG) using OpenAI embeddings and pgvector for vector similarity search. To recap the steps for RAG:

**Pre-processing**
We've already completed our pre-processing steps when we set up the `book_search` database and generated embeddings for the various Launch School book chapters we wanted to support.

**Runtime Pipeline**
To complete our RAG application, we'll need to:

1. Query the user for input
2. Embed the user query and use this embedding to fetch related book chapters from our vector database.
3. Format our prompt with system instructions, our list of related book chapters, and the user query.
4. Generate a response using our prompt and final provide it back to our user.

The goal of this lab is to ensure that you have all of the tools you need to implement your own RAG application and can troubleshoot any problems before your homework.

## Lab Overview

1. Set Up Environment
2. Connect to Existing pgvector Database
3. Get familiar with the code that generates embeddings and retrieves book chapters from the database
4. Build the RAG Query System
5. Test with Example Questions

## Setup Instructions

1. [Install Poetry](https://python-poetry.org/docs/#installation) if you haven't already.

2. From the project root, run:
    ```
    poetry install
    ```

    This will create a virtual environment and install all dependencies.

    To activate the environment, use:
    ```
    eval $(poetry env activate)
    ```

3. Create an `.env` file with `OPENAI_API_KEY= your_api_key`.

## Lab Tasks

### Task 1: Ensure Database Connection

We'll use the database that we setup and used for yesterday's labs called `book_search`. If you used a different name, make sure to update the following files accordingly.

Run `python src/db_check.py`. This file should:

- Connect to the PostgreSQL database using the provided connection parameters
- Execute a query to count the rows in the `book_chapter` table
- Print the number of book chapters found
- Close the database connection

You should see something like:

```
Found 333 book chapters in database
```

### Task 2: Vector Embedding Generation

Explore the code in `src/search.py` file. This file contains two functions:

1. `generate_embedding`

You should feel comfortable with this code. We're simply taking a string and generating an embedding using the same model that we used to create the embeddings in our vector database.

2. `search_similar_chapters`

This function is in charge of the "Retrieval" part of our simple RAG architecture. It:

- Takes an input query
- Generates an embedding for this query
- Searches our vector database and compiles a list of book chapters that resulted in similar embeddings
- Returns these similar chapters

Note that because we're working with a very small dataset, our similarity threshold is very low. If we had a much larger dataset, we would probably only be considering chapters with at least 0.7 or above.

### Task 3: RAG Implementation

Open `src/rag.py` and implement the `ask_study_question()` function.

This function should:

1. Find relevant book chapters using the `search_similar_chapters()` function
2. Check if any relevant chapters were found
3. Format the search results into a context string (including chapter content and similarity scores)
4. Create a prompt that includes:
   - Instructions for the AI (acting as a Launch School study assistant)
   - The context of relevant book chapters
   - The user's question
5. Call the OpenAI Responses API to generate a response based on the context
6. Return the generated response

Suggested prompt structure:
```
You are a helpful Launch School study assistant. Answer the user's coding question directly using your knowledge about programming and software development. Within your answer, suggest relevant Launch School book chapters where they can learn more about the topic. Make sure to include the chapter URLs in your response.

Available Book Chapters for Reference:
[formatted context with chapters and similarity scores]

Question: [user's question]

Please provide a comprehensive answer to the question, suggesting 1-3 relevant Launch School chapters where the student can study more about this topic.
```

### Bonus if time allows: Testing the Implementation

Open `src/main.py` and implement the `main()` function. This function should:

1. Define a list of example study-related questions
2. For each question, call the `ask_study_question()` function
3. Print the question and the answer
4. Add some formatting to make the output readable

## Expected Outputs

When your implementation is complete, you should be able to ask study-related questions and receive comprehensive answers that directly address the question, including references to relevant book chapters.

Example:
```
Question: How do I work with JavaScript functions and scope?
Answer: [A detailed answer that references relevant JavaScript chapters from the database]
```

## Bonus Challenges

1. Add error handling for cases where the similarity score is too low
2. Implement a function to get study recommendations based on multiple criteria
3. Create a nicer interface using Gradio
4. Add support for follow-up questions using conversation history