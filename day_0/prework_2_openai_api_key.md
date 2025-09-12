Throughout the course, we’ll be using the OpenAI API. The API gives us access to lots of cool tools to play with—and it’s surprisingly cheap. You’ll need to create and manage your own API key for the week.

## 1. Create an OpenAI account and generate your API Key
- Go to https://auth.openai.com/log-in
- If you’re new, you’ll be guided through account setup and prompted to generate your first API key
- ⚠️ Be sure to copy and save your API key somewhere safe. You won’t be able to see it again later.

## 2. Add some API credits
- If you’re new, you’ll be prompted to add credits. You’ll need to add $5 (the minimum).
- If you already have an account, you can visit https://platform.openai.com/settings/organization/billing/overview to view or add credits. You should also visit this URL to ensure that “Auto recharge” is turned off to avoid any unexpected charges.

    $5 will be more than enough for the week’s work—as long as you don’t over do it.

- If you lose your API key or need to create a new one, visit https://platform.openai.com/api-keys.

> ⚠️ Never upload your API key publicly!
> 
> This is why we use a `.env` file to store our API keys. `.env` should be listed in your `.gitignore` file whenever you’re pushing projects to GitHub.
> 
> This is another good reason to have “auto recharge” turned off and delete old API keys you aren’t using anymore.

## 3. Learn to access your API key safely
There are several ways to access your OpenAI API key from your projects, but we’ll look at using `python-dotenv` paired with a `.env` file. Follow along with the demonstration.

**1. Create a new project and virtual environment**

```
mkdir dotenv_test
cd dotenv_test
poetry init --no-interaction
poetry add python-dotenv
eval $(poetry env activate)
```

**2. Install `python-dotenv`**

```
poetry add python-dotenv
```

**3. Create a `.env` file and add your API key**

```
OPENAI_API_KEY=your_api_key_here
```

**4. Create a .gitignore file and add .env.**

This isn’t important for this demonstration, but it’s an important step that you should make part of your routine.

```
# Environment variables
.env
```

**5. Load the environment variable in your code**

Create a new python file, `my_app.py` with the following code:

```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv('OPENAI_API_KEY')

print(API_KEY)
```

Run `my_app.py`. If your API key is printed out, you’re all set!
