import typer

from saturn.server.killer import (
    kill_all_servers,
    kill_saturn_servers,
)
from saturn.server.runner import run_server


server_app = typer.Typer(
    help="Manage development servers."
)


@server_app.command(
    "run",
    help="Start a development server.",
)
def run(
    app: str = typer.Option(
        "app:app",
        "--app",
        help="ASGI application path.",
    ),
    host: str = typer.Option(
        "127.0.0.1",
        "--host",
        help="Host where the server will run.",
    ),
    port: int = typer.Option(
        8000,
        "--port",
        help="Port where the server will run.",
    ),
) -> None:
    run_server(
        app=app,
        host=host,
        port=port,
    )


@server_app.command(
    "kill",
    help="Stop servers started by Saturn.",
)
def kill() -> None:
    killed = kill_saturn_servers()

    typer.echo(
        f"Stopped {killed} Saturn server(s)."
    )


@server_app.command(
    "kill-all",
    help="Stop detected development servers.",
)
def kill_all() -> None:
    killed = kill_all_servers()

    typer.echo(
        f"Stopped {killed} development server(s)."
    )