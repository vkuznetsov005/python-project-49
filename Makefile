install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-uninstall:
	uv tool uninstall brain-games

lint:
	uv run ruff check brain_games

clean:
	rm -rf dist/
	rm -rf .venv/
	rm -rf *.egg-info/

reinstall: clean install build package-install