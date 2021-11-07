#!/bin/bash
python main.py
python -m pip install --upgrade pip
fandogh login --username hesam80 --password sa13801380
fandogh service apply \ -f flaskapp.yml