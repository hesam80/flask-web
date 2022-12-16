#!/bin/bash
python main.py
git checkout --force circleci
git --no-pager log --no-color -n 1 --format='%h'

