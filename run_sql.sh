#!/bin/bash
python main.py
python pip install --upgrade pip
python pip install fandogh-cli
git checkout --force circleci
git --no-pager log --no-color -n 1 
fandogh service deploy --image hesam80/flaskapp --version latest
echo "fandogh log"