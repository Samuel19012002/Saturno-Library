import typer

from saturn.cli.commands.cache import cache_app
from saturn.cli.commands.server import server_app


app = typer.Typer(
    name="sr",
    help="Saturn CLI",
)


@app.callback()
def main() -> None:
    pass


app.add_typer(
    server_app,
    name="server",
)

app.add_typer(
    cache_app,
    name="cache",
)