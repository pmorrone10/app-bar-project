PYTHON := python3
PIP := pip3
TEST_DIR := tests
VENV_DIR := venv

# Reglas
.PHONY: help install init test clean

install:
	$(PIP) install -r requirements.txt

init:
	$(PYTHON) -m venv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate && $(PIP) install -r requirements.txt

test: $(VENV_DIR)/bin/activate
	. $(VENV_DIR)/bin/activate && $(PYTHON) -m unittest discover $(TEST_DIR)

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +
	rm -rf $(VENV_DIR)