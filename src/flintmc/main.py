import typer

app = typer.Typer()

@app.command()
def main(source_path: str) -> None:
    ...
