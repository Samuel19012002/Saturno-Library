import typer

from saturn.cache.cleaner import clear_cache


cache_app = typer.Typer(
    help="Manage Python cache."
)


@cache_app.command(
    "clear",
    help="Clear Python cache files and __pycache__ directories.",
)
def clear() -> None:
    clear_cache()