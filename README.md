# Saturn Library

Saturn Library is a Python development toolkit and CLI designed to simplify common development workflows.

It provides a command-line interface through the `sr` command.

## Installation

Install Saturn Library from PyPI:

```bash
pip install saturn-library
```

After installation:

```bash
sr --help
```

## Commands

The current CLI structure is:

```text
sr
├── server
│   ├── run
│   ├── kill
│   └── kill-all
└── cache
    └── clear
```

## Server

### Run a server

Start an ASGI development server using Uvicorn:

```bash
sr server run
```

By default, Saturn uses:

```text
Application: app:app
Host:        127.0.0.1
Port:        8000
Reload:      enabled
```

You can customize the ASGI application:

```bash
sr server run --app main:app
```

Change the port:

```bash
sr server run --port 8001
```

Change the host:

```bash
sr server run --host 0.0.0.0
```

Or combine the options:

```bash
sr server run --app main:app --host 0.0.0.0 --port 8001
```

### Stop Saturn servers

Stop development servers started and tracked by Saturn:

```bash
sr server kill
```

### Stop detected development servers

Stop development server processes detected by Saturn:

```bash
sr server kill-all
```

This command is more aggressive than `sr server kill` and may terminate development servers that were not started through Saturn.

## Cache

Clear Python cache files and `__pycache__` directories from the current project:

```bash
sr cache clear
```

## Development

Clone the repository:

```bash
git clone https://github.com/Samuel19012002/Saturno-Library.git
cd Saturno-Library
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it on macOS or Linux:

```bash
source venv/bin/activate
```

Install Saturn in editable mode:

```bash
python3 -m pip install -e .
```

Then test the CLI:

```bash
sr --help
```

## Status

Saturn Library is under active development. Additional developer tooling, cloud integrations, and AI-related capabilities may be added in future releases.
