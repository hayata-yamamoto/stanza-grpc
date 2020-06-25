default: | help

SHELL=/bin/bash

protoc: ## compile .proto into .py
	poetry run python commands/genproto.py

format: ## format codes 
	poetry run yapf -r -i --style pep8 .

isort: ## reorder imports
	poetry run isort -rc src

mypy: ## check static typing 
	poetry run mypy --html-report ./.report src/

flake8: ## check PEP8 style 
	poetry run flake8 src/

test: ## unit testing 
	poetry run pytest tests/

start-server: 
	poetry run python3 commands/server.py

# This help command is cited from https://ktrysmt.github.io/blog/write-useful-help-command-by-shell/
help: ## print this message
	@grep -E '^[/a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | perl -pe 's%^([/a-zA-Z_-]+):.*?(##)%$$1 $$2%' | awk -F " *?## *?" '{printf "\033[36m%-30s\033[0m %-50s %s\n", $$1, $$2, $$3}'	
