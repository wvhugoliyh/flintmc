import typer

app = typer.Typer()

@app.command()
def main(source_path: str, dest_path: str):
  pass