#!/usr/bin/env bash

ITF1788_HOME=`dirname "$0"`

if [ ! "$@" ]; then
    PYTHONPATH="$ITF1788_HOME" python3 -m itf1788 -s "$ITF1788_HOME/itl" -o "$ITF1788_HOME/output"
else
    PYTHONPATH="$ITF1788_HOME" python3 -m itf1788 "@*"
fi
