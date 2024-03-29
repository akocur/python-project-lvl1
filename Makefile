install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install: build
	python3 -m pip install --user --force-reinstall dist/*.whl
package-uninstall:
	pip uninstall hexlet-code
lint:
	poetry run flake8 --exit-zero brain_games
rec:
	poetry run asciinema rec