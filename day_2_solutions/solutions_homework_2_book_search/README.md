# Book Search App Possible Solution

These steps assume that you have PostgreSQL, PGVector, and Poetry installed.

You can skip steps 3, 4, and 5 if you already have the `book_search` database populated from the lab work. If you've made any modifications, you should start fresh. You can find-and-replace `book_search` with a different db name to preserve your own. 

1. From the project root, run:

    ```
    poetry install
    ```

    This will create a virtual environment and install all dependencies.

    To activate the environment, use:
    ```
    eval $(poetry env activate)
    ```

2. Create a `.env` file with `OPENAI_API_KEY=your_api_key`.

3. Create a new database, `book_search`.

4. Run `python setup_db.py`.

5.  Run `python load_embeddings.py`. You should see output like this:
    ```
    ...
    Stored embedding for: Advanced Data Structures and Algorithms: Practice:...
    Stored embedding for: Advanced Data Structures and Algorithms: Introduct...
    Stored embedding for: Advanced Data Structures and Algorithms: Terminolo...
    Stored embedding for: Advanced Data Structures and Algorithms: Problem S...
    Stored embedding for: Advanced Data Structures and Algorithms: Template...
    Stored embedding for: Advanced Data Structures and Algorithms: Demo: Per...
    Stored embedding for: Advanced Data Structures and Algorithms: Practice:...
    Stored embedding for: Advanced Data Structures and Algorithms: Conclusio...
    Processed batch 4/4
    All embeddings stored successfully!
    ```

6. Run `python app.py`. Visit the provided URL to see the application.