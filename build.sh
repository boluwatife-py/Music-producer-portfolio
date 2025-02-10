#!/bin/bash

# Upgrade pip and install dependencies using Python 3
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Apply migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput
