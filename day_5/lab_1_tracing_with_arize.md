# Tracing with Arize

In this lab, you'll use Arize to add tracing to your RAG application. [Follow the Quickstart Guide here.](https://arize.com/docs/ax/observe/quickstart-llm). You'll need to create a free account to get an API key. If you run into issues, check out their [demo notebook](https://colab.research.google.com/github/Arize-ai/tutorials/blob/main/python/llm/tracing/openai/openai-tracing.ipynb). (_Note: Google Colab is just an online version of Jupyter Notebooks. You can run it directly in your browser._)

> 💡 Reminder: Whenever you see `pip install`, use `poetry add` instead to keep your dependencies up to date.

> 💡 It can be tricky to find the dashboard from the docs. To access it, go to `arize.com` instead of staying on `arize.com/docs`.

Once you have tracing working, run your app a few times and explore the logs in Arize. While there are many tracing tools, most look and behave similarly, so what you’re seeing here will be familiar on other platforms. Then, try breaking your app and running it again to see what an error looks like in the logs.
