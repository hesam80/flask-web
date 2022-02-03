#!/bin/bash
python main.py
python pip install --upgrade pip
python pip install fandogh-cli
fandogh service deploy --image hesam80/flaskapp --version latest
echo "fandogh log"