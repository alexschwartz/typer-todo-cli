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


def test_version():
    result = runner.invoke(cli.cli, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout

def test_invoke():
    result = runner.invoke(cli.cli, ["invoke", "ls"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


