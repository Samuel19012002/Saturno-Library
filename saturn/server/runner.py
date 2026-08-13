from pathlib import Path
import os

import uvicorn


PID_FILE = Path.home() / ".saturn" / "servers.pid"


def _register_server() -> None:
    PID_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with PID_FILE.open("a") as file:
        file.write(f"{os.getpid()}\n")


def run_server(
    app: str = "app:app",
    host: str = "127.0.0.1",
    port: int = 8000,
    reload: bool = True,
) -> None:
    _register_server()

    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=reload,
    )