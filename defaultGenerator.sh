#!/usr/bin/env bash

WORKING_DIR=$(pwd)
ITF1788_HOME="$( cd "$( dirname "$0" )" && pwd )"
cd "${ITF1788_HOME}/src"

if [ ! "$@" ]; then
    python3 "$ITF1788_HOME/src/main.py" -s "${ITF1788_HOME}/itl/" -o "${ITF1788_HOME}/output/"
else
    python3 "$ITF1788_HOME/src/main.py" "@*"
fi

cd "$WORKING_DIR"

