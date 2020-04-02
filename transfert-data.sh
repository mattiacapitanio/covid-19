#!/bin/bash
SCRIPTPATH=$(dirname $0)

export $(cat $SCRIPTPATH/.env)
# TODO: add check for env vars
KAGGLE_URLS=( $(echo ${KAGGLE_URLS} | tr ";" " ") )

cd $SCRIPTPATH
source venv/bin/activate

for url in "${KAGGLE_URLS[@]}"; do
    date -u +'%Y-%m-%d %H:%M:%S UTC: Download dataset from Kaggle ('${url}')'
    kaggle datasets download $url -p $SCRIPTPATH/$DATA_DIR --unzip --force
    date -u +'%Y-%m-%d %H:%M:%S UTC: Download completed!'
done

date -u +'%Y-%m-%d %H:%M:%S UTC: Upload datasets on Drive'
python3 upload.py -d DATA_DIR -g GDRIVE_FOLDER_ID
date -u +'%Y-%m-%d %H:%M:%S UTC: Upload completed!'

deactivate