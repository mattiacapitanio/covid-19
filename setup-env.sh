#!/usr/bin/bash
# requirements: python3, pip3

KAGGLE_API_TOKEN=~/.kaggle/kaggle.json

echo "Create virtualenv..."
pip3 install virtualenv
virtualenv venv
source venv/bin/activate

echo "Setup environment..."
mkdir log
mkdir output

echo "Install kaggle..."
pip install kaggle

if test -f "$KAGGLE_API_TOKEN"; then
    echo "Kaggle API token file found!"
    chmod 600 ~/.kaggle/kaggle.json
    kaggle --version
else 
    echo "Error: Kaggle API token file not found!"
    echo "Please create a valid token file under $KAGGLE_API_TOKEN"
    echo "See: https://github.com/Kaggle/kaggle-api"
fi


