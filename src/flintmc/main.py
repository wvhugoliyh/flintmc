from pathlib import Path

import typer
from lark import Lark

from flintmc.flint_parser import FlintParser

app = typer.Typer()

@app.command()
def main(source_path: str, dest_path: str):
  parser = Lark.open("grammar.lark", rel_to=__file__, parser="lalr", transformer=FlintParser)
  source_path_obj = Path(source_path).resolve()
  print(parser.parse(source_path_obj.read_text()))
