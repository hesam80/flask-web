#!/bin/bash
python main.py
python pip install --upgrade pip
python pip install fandogh-cli
coomit = git --no-pager log --no-color -n 1 --format='%h'
fandogh service deploy --image hesam80/flaskapp --version $commit
echo "fandogh log"