#!/bin/bash
SCRIPTPATH=$(dirname $0)

export $(cat $SCRIPTPATH/.env)
# TODO: add check for env vars

cd $SCRIPTPATH
source venv/bin/activate

date -u +'%Y-%m-%d %H:%M:%S UTC: Download starts...'
kaggle datasets download $KAGGLE_URL -p $SCRIPTPATH/$DATA_DIR --unzip --force
date -u +'%Y-%m-%d %H:%M:%S UTC: Download completed!'

date -u +'%Y-%m-%d %H:%M:%S UTC: Upload start...'
python3 upload.py -d DATA_DIR -g GDRIVE_FOLDER_ID
date -u +'%Y-%m-%d %H:%M:%S UTC: Upload completed!'

deactivate