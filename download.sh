#!/bin/bash
KAGGLE_URL=sudalairajkumar/covid19-in-italy
SCRIPTPATH=$(dirname $0)

date -u +'%Y-%m-%d %H:%M:%S UTC: Download starts...'
cd $SCRIPTPATH
source venv/bin/activate
kaggle datasets download $KAGGLE_URL -p $SCRIPTPATH/data --unzip --force
deactivate
date -u +'%Y-%m-%d %H:%M:%S UTC: Download completed!'