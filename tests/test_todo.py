# tests/test_todo.py
import json
import pytest
from typer.testing import CliRunner

from pet_little_helferlein import (
    DB_READ_ERROR,
    SUCCESS,
    __app_name__,
    __version__,
    cli
)

runner = CliRunner()

test_data1 = {
    "description": ["Write", "a", "blog", "on", "JavaScript libraries"],
    "priority": 1,
    "todo": {
        "Description": "Write a blog on JavaScript libraries.",
        "Priority": 1,
        "Done": False,
    },
}

def test_version():
    result = runner.invoke(cli.cli, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


