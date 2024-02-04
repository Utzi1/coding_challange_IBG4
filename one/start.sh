#!/usr/bin/env bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the dependencies
pip install pytest networkx numpy

# and run pytest:
python -m pytest tests
