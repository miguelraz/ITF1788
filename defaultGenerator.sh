#!/usr/bin/env bash

python3 setup.py build

export PYTHONPATH=build/lib

if [ ! "$@" ]; then
    python3 -m itf1788 -s itl -o output
else
    python3 -m itf1788 "@*"
fi
