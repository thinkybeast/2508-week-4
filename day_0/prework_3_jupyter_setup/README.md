Throughout the course, we'll be using Jupyter notebooks for our AI experiments and labs. While they may take a little getting used to, Jupyter notebooks are extremely useful for AI work—they let you store and examine variables after running code, so you don’t have to repeat costly API calls just to check or adjust your results. This makes experimenting and iterating much faster and more efficient.

Since we're using Poetry to manage our virtual environments, we'll want to make sure our notebooks use these venvs. This will allow you to seamlessly move from a Jupyter Notebook to working in regular files.

Here's a demo of how to setup Jupyter Notebooks to work alongside Poetry with an existing project. The written instructions that follow mirror this demo, but also include instructions for creating a new project with a Jupyter notebook.

[🎥 Watch the demo!](./poetry_with_jupyter_demo.mp4)

## 1. Setting up Jupyter with Poetry

### Step 1: Create and activate your virtual environment with Poetry

Follow the steps that you used in the "Poetry Workflow" prework. For this demo, that looks like:

```bash
cd prework_3_jupyter_setup
poetry install
eval $(poetry env activate)
```

This will add Jupyter to your project dependencies and install it in your Poetry virtual environment. Note that it installs the correct packages because the `pyproject.toml` in this directory contains:

```
dependencies = [
    "jupyter (>=1.1.1,<2.0.0)",
    "ipykernel (>=6.30.1,<7.0.0)"
]
```

If you're creating a new project with a Jupyter notebook, you'll need to use `poetry add jupyter ipykernel`.

> 💡 Note: When running `poetry install`, you may see an annoying error like this:
>
> ```
> Installing the current project: my_cool_project (0.1.0)
> Error: The current project could not be installed: No file/folder found for package my_cool_project
> If you do not want to install the current project use --no-root.
> If you want to use Poetry only for dependency management but not for packaging, you can disable package mode by setting package-mode = false in your pyproject.toml file.
> If you did intend to install the current project, you may need to set `packages` in your pyproject.toml file.
> ```
>
> You can ignore this. In labs, we've configured the `pyproject.toml` so that you shouldn't get this error. If you want to fix it in your own projects, look into:
> - Disabling package mode by adding package-mode = false under [tool.poetry] in your pyproject.toml (best for notebooks, scripts, or learning projects that don’t need packaging).
> - Defining a package by adding a `src/` or project folder and telling Poetry where your code lives with a `packages` entry (best if you’re building a library or reusable module).

### Step 2: Select your venv as the kernel for your notebook

Run `poetry env info` to see an output like this:

```bash
brandi@mbp prework_3_jupyter_setup $ poetry env info

Virtualenv
Python:         3.12.2
Implementation: CPython
Path:           /Users/brandi/capstone/ai_week/prework_3_jupyter_setup/.venv
Executable:     /Users/brandi/capstone/ai_week/prework_3_jupyter_setup/.venv/bin/python
Valid:          True

Base
Platform:   darwin
OS:         posix
Python:     3.12.2
Path:       /opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12
Executable: /opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12/bin/python3.12
```

In the `Path:` section you can see the name of your environment, something like: `/Users/brandi/capstone/ai_week/prework_3_jupyter_setup/.venv`

Open the `jupyter_test.ipynb` jupyter notebook and choose "Select Kernel", then "Python Environments...", then you should see the name of your new environment (`prework-3-jupyter-setup-py3.12`) as an option, likely the recommended option. Select it.

## Step 3. Verifying your setup

To make sure everything is working correctly, run the first cell of `jupyter_test.ipynb` that looks like this:

```python
import openai # ModuleNotFoundError: No module named 'openai'
print('yay!')
```

**This should show an error**, since we haven't installed `openai` yet.

Run the command `poetry add openai`. After this, the `pyproject.toml` should now include `openai` in its list of dependencies. Re-run the cell and you should no longer have an error. Your jupyter notebook is using your poetry managed virtual environment! 