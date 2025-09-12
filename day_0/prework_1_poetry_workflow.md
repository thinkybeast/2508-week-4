Throughout the course, we'll be using Poetry to manage our Python dependencies and virtual environments. Poetry makes it easy to install packages and keep our projects organized. You'll need to understand how to work with Poetry for each lab.

If you haven't yet installed poetry, you can [follow the instructions here](https://python-poetry.org/docs/).

## ⚠️ Configure Poetry! ⚠️

We'll be installing a lot of packages and creating many virtual environments. By default, Poetry stores these enviornments elsewhere, which can be good for some things, but not great for us. We want Poetry to follow the same pattern that many dependency managers do, using a `.venv` directory **inside our project**. To do so, you just need to run this command once:

```
poetry config virtualenvs.in-project true
```

To ensure that this command worked, you can run:

```
poetry config virtualenvs.in-project
```

And you should see `true` output.

This means that when you create new virtual environments, you'll see a `.venv` file in your project. If you run into installation/version issues and need to start fresh, simply delete this directory and re-run `poetry install`.

> Note: If you already use Poetry, you can skip this. These instructions use the newer `eval $(poetry env activate)` command instead of `poetry shell`, but using an older version that uses `poetry shell` works just as well.

## 1. What is Poetry?
Poetry is a modern dependency management and packaging tool for Python. It helps you:
- Manage project dependencies in a `pyproject.toml` file
- Create and manage virtual environments automatically
- Install packages with their exact versions
- Keep your projects isolated and reproducible

## 2. Starting a new lab
When you begin a new lab, you'll typically receive a zip file containing the project. Here's how to get started:

**1. Extract the lab files**
- Unzip the lab file to a location on your computer
- Navigate to the extracted directory in your terminal

**2. Install dependencies**
- Run `poetry install` to install all dependencies listed in the `pyproject.toml` file
- This will create a virtual environment and install the required packages

**3. Activate the virtual environment**
- Run `eval $(poetry env activate)` to activate the virtual environment
    - Why `eval $()`? The command `poetry env activate` simply prints out the command you can use to activate the virtual environment. You could run this command, and then copy/paste the command that's been printed out. `eval $()` skips the copy/pasting step.
- You'll see your terminal prompt change to indicate you're in the Poetry environment
- Now you can run your Python scripts and use the installed packages
- Alternatively, you can use `poetry run python some_file.py` to run the file in the proper virtual environment. Activating the virtual environment with `eval $(poetry env activate)` just means you can skip typing `poetry run`.

## 3. Working with Poetry commands

**Check your environment**
```bash
poetry env info
```

**Run a script within the Poetry environment**
```bash
poetry run python your_script.py
```

**Deactivate the environment**
```bash
deactivate
```

**Add a new dependency**
```bash
poetry add package_name
```

**Add a development dependency**
```bash
poetry add --group dev package_name
```

## 4. Installing additional packages
If you need to install additional packages during a lab:

**For packages you'll use in production:**
```bash
poetry add package_name
```

**For packages only needed during development:**
```bash
poetry add --group dev package_name
```

**For packages with specific versions:**
```bash
poetry add "package_name==1.2.3"
```

**For packages with version constraints:**
```bash
poetry add "package_name>=1.0,<2.0"
```

> ⚠️ Always use `poetry add` instead of `pip install`!
> 
> This ensures that new dependencies are properly recorded in your `pyproject.toml` file and that everyone working on the project has the same versions of packages.

## 5. Creating a new project from scratch
Some labs will ask you to create a new project from scratch rather than providing a pre-made project. Here's how to set up a new Poetry project:

**1. Create a new directory and navigate to it**
```bash
mkdir my_new_project
cd my_new_project
```

**2. Initialize a new Poetry project**
```bash
poetry init
```
This will walk you through creating a `pyproject.toml` file. You can press Enter to accept the defaults for most options. If you want to make a basic bare-bones `pyproject.toml` without configuration options, you can run `poetry init --no-interaction` instead. This is usually sufficient for small projects.

**3. Add your dependencies**
```bash
poetry add package_name
```

**4. Activate the environment and start coding**
```bash
eval $(poetry env activate)
```

## 6. Troubleshooting

**If you get permission errors:**
- Make sure you're in the correct directory
- Check that the `pyproject.toml` file exists
- Try running `poetry install --verbose` for more detailed output

**If packages aren't found:**
- Make sure you're in the Poetry shell (`poetry shell`)
- Check that the packages are listed in `pyproject.toml`
- Try running `poetry install` again

Remember: Poetry will handle creating and managing your virtual environment automatically, so you don't need to create one manually like with `python -m venv`.
