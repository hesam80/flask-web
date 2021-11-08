#!/bin/bash
python main.py
python -m pip install --upgrade pip
python -m pip install fandogh-cli
fandogh login --username hesam80 --password sa13801380
fandogh service deploy --image hesam80/flaskapp --version latest
echo "fandogh log"