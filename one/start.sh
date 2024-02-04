#!/usr/bin/env bash

python3 -m venv test_env

source test_env/bin/activate

python3 -m pip install --upgrade pip

python3 -m pip install -r requirements.txt

python3 -m pytest tests


