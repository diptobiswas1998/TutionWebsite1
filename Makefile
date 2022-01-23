.DEFAULT_GOAL=help

req:
	pip freeze > requirement.txt

set-up: ## For initial set-up
	pip install virtualenv
	python -m virtualenv venv
	.\venv\Scripts\activate
	pip install -r .\requirement.txt

run: ## To run the application
	python main.py

req-mac:
	pip3 freeze > requirement.txt

set-up-mac: ## For initial set-up(for mac)
	pip3 install virtualenv
	python3 -m virtualenv venv
	pip3 install -r requirement.txt

run-mac: ## To run the application(for mac)
	python3 main.py

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
