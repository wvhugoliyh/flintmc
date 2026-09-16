""" FlintMC is a CLI tool used to transpile Flint code into Minecraft datapacks. """

from pathlib import Path

import typer
from lark import Lark

from flintmc.flint_parser import FlintParser
from flintmc.sort_ast import sort_ast

app = typer.Typer()

@app.command()
def main(source_path: str, dest_path: str) -> None:
  parser = Lark.open("grammar.lark", rel_to=__file__, parser="lalr", transformer=FlintParser())
  source_path_obj = Path(source_path).resolve()
  ast = parser.parse(source_path_obj.read_text())
  print(sort_ast(ast, "test"))