install: ## Create a python3.6 virtual env and install requirements into it.
	@python3.6 -m venv venv
	@venv/bin/pip install -r requirements.lock
