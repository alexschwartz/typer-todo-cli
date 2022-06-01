"""This module provides the PET little_helferlein CLI."""
# pet_little_helferlein/cli.py

from pathlib import Path
from typing import Optional, List

import typer

from pet_little_helferlein import __app_name__, __version__

cli = typer.Typer()

@cli.command()
def remove(
    todo_id: int = typer.Argument(...),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Force deletion without confirmation.",
    ),
) -> None:
    """Remove a to-do using its TODO_ID."""

    typer.secho("Invalid TODO_ID", fg=typer.colors.RED)
    raise typer.Exit(1)

@cli.command(name="invoke")
def invoke(
    cmd: str = typer.Argument(...),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Force deletion without confirmation.",
    ),
) -> None:
    """Invoke a command."""

    typer.secho("Invalid TODO_ID", fg=typer.colors.RED)
    raise typer.Exit(1)


def callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@cli.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=callback,
        is_eager=True,
    )
) -> None:
    return
