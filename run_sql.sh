#!/bin/bash
python main.py
/usr/bin/python pip install --upgrade pip
/usr/bin/python pip install fandogh-cli --upgrade
git checkout --force circleci
git --no-pager log --no-color -n 1 --format='%h'
fandogh service deploy --image hesam80/flaskapp --version latest
echo "fandogh login"
