#!/bin/bash
python main.py
git checkout 
git --no-pager log --no-color -n 1 --format='%h'

