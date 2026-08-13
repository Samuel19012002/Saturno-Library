import uvicorn


def run_server(
    app: str = "app:app",
    host: str = "127.0.0.1",
    port: int = 8000,
    reload: bool = True,
) -> None:
    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=reload,
    )