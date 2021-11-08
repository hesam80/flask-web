#!/bin/bash

python -m pip install --upgrade pip
python -m pip install fandogh-cli
fandogh login --username hesam80 --password sa13801380
fandogh service apply  -f flaskapp.yml
echo "fandogh log"