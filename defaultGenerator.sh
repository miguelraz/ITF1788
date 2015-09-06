#!/usr/bin/env bash

if [ ! "$@" ]; then
    python3 -m itf1788 -s itl -o output
else
    python3 -m itf1788 "@*"
fi
