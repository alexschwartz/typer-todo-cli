## TYPER-TODO-CLI

Todo CLI application built with Typer Easy to code. Based on Python type hints.

> To learn more about ConfigParser [Click Here](https://zetcode.com/python/configparser/)

### To get started follow these steps

1. Create Virtual Environment and Activate It

```shell
> python -m venv env
> source env/bin/activate
```

2. Install Dependencies

```shell
> pip install -r requirements.txt
```

3. Run the below command to see all available options

```shell
> python -m todo --help
```

> Available options

```
Usage: todo [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version         Show the application's version and exit.
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.

  --help                Show this message and exit.

Commands:
  add       Add a new to-do with a DESCRIPTION.
  clear     Remove all to-dos.
  complete  Complete a to-do by setting it as done using its TODO_ID.
  init      Initialize the to-do database.
  list      List all to-dos.
  remove    Remove a to-do using its TODO_ID.

```

4. Add/Run Tests (Optional)

   > You can add more tests to `tests/test_todo.py`

```shell
# run tests
> python -m pytest tests/.
```
