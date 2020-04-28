#!/bin/bash
SCRIPTPATH=$(dirname $0)

cd $SCRIPTPATH
source venv/bin/activate
python3 transfer-data.py
deactivate