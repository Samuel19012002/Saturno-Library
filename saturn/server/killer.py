from pathlib import Path

import psutil


PID_FILE = Path.home() / ".saturn" / "servers.pid"

def kill_saturn_servers() -> int:
    if not PID_FILE.exists():
        return 0

    killed = 0
    pids = PID_FILE.read_text().splitlines()

    for value in pids:
        try:
            pid = int(value)
            process = psutil.Process(pid)

            children = process.children(
                recursive=True
            )

            for child in children:
                try:
                    child.terminate()
                    killed += 1
                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                ):
                    continue

            process.terminate()
            killed += 1

        except (
            ValueError,
            psutil.NoSuchProcess,
            psutil.AccessDenied,
        ):
            continue

    PID_FILE.unlink(missing_ok=True)

    return killed


def kill_all_servers() -> int:
    killed = 0

    server_patterns = (
        "uvicorn",
        "gunicorn",
        "vite",
        "next dev",
        "react-scripts start",
        "npm run dev",
        "npm start",
        "yarn dev",
        "yarn start",
        "pnpm dev",
    )

    for process in psutil.process_iter(
        ["pid", "cmdline"]
    ):
        try:
            cmdline = process.info["cmdline"] or []

            command = " ".join(cmdline).lower()

            if any(
                pattern in command
                for pattern in server_patterns
            ):
                process.terminate()
                killed += 1

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess,
        ):
            continue

    return killed