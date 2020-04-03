#!/bin/bash

# check requirements
# sudo apt update && sudo apt install python3 python3-pip virtualenv
type -P python3 > /dev/null 2>&1
test $? = 1 && echo "Error: please install Python3" && exit 1
type -P pip3 > /dev/null 2>&1
test $? = 1 && echo "Error: please install pip" && exit 1
type -P virtualenv > /dev/null 2>&1
test $? = 1 && echo "Error: please install virtualenv" && exit 1

KAGGLE_API_TOKEN=~/.kaggle/kaggle.json

echo "Setup environment..."
virtualenv venv
source venv/bin/activate
mkdir log

echo "Install dependencies..."
pip3 install -r requirements.txt

echo "Check environment..."
if test -f "$KAGGLE_API_TOKEN"; then
    echo "Kaggle API token file found!"
    chmod 600 ~/.kaggle/kaggle.json
    kaggle --version
else 
    echo "Error: Kaggle API token file not found!"
    echo "Please create a valid token file under $KAGGLE_API_TOKEN"
    echo "See: https://github.com/Kaggle/kaggle-api"
    exit 1
fi

echo "Configure cron..."
crontab -l | { cat; echo "0 6 * * * $(pwd)/transfer-data.sh >> $(pwd)/log/crontab.log 2>&1"; } | crontab -
echo "Done!"
