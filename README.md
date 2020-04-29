# Kaggle to Google Drive (Covid-19 project)

Simple script code for automatically downloading a dataset from Kaggle.

## Code description 

The code uses the [Python Kaggle API](https://github.com/Kaggle/kaggle-api) and crontab for automatically downloading a dataset from Kaggle. 

### Setup environment

The script `setup-env.sh` creates and prepares the enviroment for downloading the dataset. The script creates a Python virtualenv, installs the Python dependecies and adds a crontab job for automatically running the script `transfer-data.sh`.

**Note:** a valid Kaggle API token needs to be found under `~/.kaggle/kaggle.json` (see the *API credentials* section under the [Kaggle API](https://github.com/Kaggle/kaggle-api) documentation).

### Donwnload the dataset 

The script `transfer-data.sh` downloads the dataset from Kaggle and saves it under the `data` folder. A `crontab.log` file can be found under the `log` directory.



