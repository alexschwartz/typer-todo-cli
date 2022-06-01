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
test_data2 = {
    "description": ["Write a blog on seo"],
    "priority": 2,
    "todo": {
        "Description": "Write a blog on seo.",
        "Priority": 2,
        "Done": False,
    },
}


def test_version():
    result = runner.invoke(cli.cli, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


@pytest.fixture
def mock_json_file(tmp_path):
    todo = [{"Description": "Learn typer", "Priority": 2, "Done": False}]
    db_file = tmp_path / "todo.json"
    with db_file.open("w") as db:
        json.dump(todo, db, indent=4)
    return db_file


@pytest.mark.parametrize(
    "description, priority, expected",
    [
        pytest.param(
            test_data1["description"],
            test_data1["priority"],
            (test_data1["todo"], SUCCESS),
        ),
        pytest.param(
            test_data2["description"],
            test_data2["priority"],
            (test_data2["todo"], SUCCESS),
        ),
    ],
)
def test_add(mock_json_file, description, priority, expected):
    todoer = todo.Todoer(mock_json_file)
    assert todoer.add(description, priority) == expected
    read = todoer._db_handler.read_todos()
    assert len(read.todo_list) == 2
