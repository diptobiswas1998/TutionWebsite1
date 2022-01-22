.DEFAULT_GOAL=help

set-up:
	pip install virtualenv
	python -m virtualenv venv
	.\venv\Scripts\activate
	pip install -r .\requirement.txt

run:
	python main.py

help:
	@echo 1. "make set-up" for initial set-up
	@echo 2. "make run" to run the application
