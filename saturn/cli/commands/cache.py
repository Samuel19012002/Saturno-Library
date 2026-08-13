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
    deleted_dirs, deleted_files = clear_cache()

    typer.echo(
        f"Cache cleared: "
        f"{deleted_dirs} directories and "
        f"{deleted_files} files removed."
    )