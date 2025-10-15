# starter-python

Starter template for a Python monorepo with FastAPI services in `apps/` and shared libraries in `packages/`.

## Try it now!

### GitHub Template

[Create a repo from this template on GitHub](https://github.com/elonehoo-starter/python/generate).

### Clone to local

If you prefer to do it manually with a clean git history:

```bash
npx degit elonehoo-starter/python my-python-app
cd my-python-app
```

If you use uv for dependency management (recommended):

```bash
uv sync
```

## What's inside

- apps/ — FastAPI services (executables)
- packages/ — Shared libraries reused by apps
- scripts/ — Dev helper (`dev.py`) that bootstraps monorepo src paths
- .vscode/ — Ready-to-use VS Code tasks and settings
- pyproject.toml — Root config (formatters, pytest) and uv workspace members

Example modules included:
- `apps/example-service`: a FastAPI app that mounts routers from `packages/base-api` and uses `packages/example-util`.
- `packages/base-api`: common FastAPI routers (e.g. `/health`, `/info`).
- `packages/example-util`: a tiny utility library exposing `greet(name)`.

## Project structure

```
apps/
	example-service/
		pyproject.toml
		src/example_service/
			main.py
			run.py
		tests/
packages/
	base-api/
		pyproject.toml
		src/base_api/routers/
			health.py
			info.py
	example-util/
		pyproject.toml
		src/example_util/
			__init__.py
			core.py
		tests/
scripts/
	dev.py
.vscode/
	settings.json
	tasks.json
pyproject.toml
```

## Quick start

Run the FastAPI dev server (hot reload):

```bash
uv run python scripts/dev.py -m example_service.run
```

Open the docs:

- http://127.0.0.1:8000/docs

Health check:

```bash
curl -sS http://127.0.0.1:8000/health
```

Run tests:

```bash
uv run pytest -q
```

VS Code tasks:

- Dev server (uvicorn) — start the dev server with reload
- Test all — run all tests
- HTTP: GET /health — quick health probe

## Create a new package (packages)

1) Create a folder: `packages/your-lib/src/your_lib`
2) Add `packages/your-lib/pyproject.toml` (use hatchling or your builder)
3) Write code and tests in `packages/your-lib/tests/`
4) Apps can import it directly (uv workspace + dev helper make imports work during development)

## Create a new service (apps)

1) Create a folder: `apps/your-service/src/your_service`
2) Add dependencies in `apps/your-service/pyproject.toml`
3) Build APIs with FastAPI and import shared packages as needed

## Checklist

When you use this template, follow the checklist to update your info properly:

- [ ] Change the author information in `apps/*/pyproject.toml` and `packages/*/pyproject.toml`
- [ ] Rename projects in `pyproject.toml` files to your own names
- [ ] Update this `README.md` with your project description
- [ ] Remove example modules (`example-service`, `example-util`, `base-api`) if you don't need them

Enjoy and build great services!
