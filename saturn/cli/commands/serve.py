import typer

from saturn.server.runner import run_server


def serve(
    app: str = typer.Option(
        "app:app", "--app", help="ASGI application path."
    ),
    host: str = typer.Option(
        "127.0.0.1", "--host", help="Host where the server will run."
    ),
    port: int = typer.Option(
        8000, "--port", help="Port where the server will run."
    ),
) -> None:
    run_server(
        app=app,
        host=host,
        port=port,
    )