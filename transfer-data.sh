#!/bin/bash
SCRIPTPATH=$(dirname $0)

export $(cat $SCRIPTPATH/.env)
# TODO: add check for env vars
KAGGLE_URLS=( $(echo ${KAGGLE_URLS} | tr ";" " ") )
GDRIVE_FOLDER_IDS=( $(echo ${GDRIVE_FOLDER_IDS} | tr ";" " ") )

cd $SCRIPTPATH
source venv/bin/activate

len=${#KAGGLE_URLS[@]}

for (( i=0; i<$len; i++ )); do 
    date -u +'%Y-%m-%d %H:%M:%S UTC: Download dataset from Kaggle ('${KAGGLE_URLS[$i]}')'
    kaggle datasets download ${KAGGLE_URLS[$i]} -p $SCRIPTPATH/$DATA_DIR --unzip --force
    date -u +'%Y-%m-%d %H:%M:%S UTC: Download completed!'

    date -u +'%Y-%m-%d %H:%M:%S UTC: Process dataset ('${KAGGLE_URLS[$i]}')'
    python3 process.py ${DATA_DIR}

    # TODO: add check getting the i element from GDRIVE_FOLDER_IDS 
    date -u +'%Y-%m-%d %H:%M:%S UTC: Upload datasets on Drive'
    python3 upload.py ${DATA_DIR} ${GDRIVE_FOLDER_IDS[$i]}
    date -u +'%Y-%m-%d %H:%M:%S UTC: Upload completed!'

    rm -r data/*
done

deactivate