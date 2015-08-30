#!/usr/bin/env bash

if [ ! "$@" ]; then
    python3 -m src -s itl -o output
else
    python3 -m src "@*"
fi
