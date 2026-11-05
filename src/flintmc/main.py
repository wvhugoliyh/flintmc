import typer
from lark import Lark

from flintmc.parser import FlintParser

app = typer.Typer()

@app.command()
def main(source_path: str) -> None:
    parser = Lark.open( # noqa F841
        "parser/flint.lark",
        rel_to=__file__,
        parser="lalr",
        regex=True,
        debug=True,
        transformer=FlintParser,
    )
