from rich.console import Console
from rich.theme import Theme

err_output = Console(theme=Theme({
    "warning": "yellow",
    "error": "red",
}), stderr=True)