import typer

from saturn.cli.commands.serve import serve
from saturn.cli.commands.cache import cache_app


app = typer.Typer(
    name="sr",
    help="Saturn CLI",
)


@app.callback()
def main() -> None:
    pass


app.command()(serve)

app.add_typer( cache_app, name="cache" )
     
    
