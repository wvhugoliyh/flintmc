import sys

from rich import print


def raise_error(message: str) -> None:
    print(f"[red]Error: {message}[/red]")
    sys.exit(1)