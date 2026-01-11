#!/bin/sh
if [ ./.venv/bin/activate ]; then source ./.venv/bin/activate; fi
python3 -m pytest system-test -q $*
