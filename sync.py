import json
import os
from download import Downloader, CurlDownloader, KaggleDownloader
import glob
from datetime import datetime as dt

def remove_files_in_dir(folder):
    files = glob.glob(folder)
    for f in files:
        os.remove(f)

def log(message):
    print('{} {}'.format(
        dt.now().strftime('%H:%M:%S'),
        message
    )) 

def download(dataset): 
    log('Download dataset {}...'.format(dataset['id']))
    if dataset['type'] == 'url':
        Downloader(
            CurlDownloader(), 
            dataset['localFolder'],
            dataset['sourceUrls']
        ).perform()
    elif dataset['type'] == 'kaggle':
        Downloader(
            KaggleDownloader(), 
            dataset['localFolder'],
            dataset['sourceUrls']
        ).perform()
    log('Done!')

def process(dataset):
    log('Process dataset {}...'.format(dataset['id']))
    os.system('python3 process.py {}'.format(
        dataset['localFolder']
    ))
    log('Done!')

def upload(dataset):
    log('Upload dataset {}...'.format(dataset['id']))
    os.system('python3 upload.py {} {}'.format(
        dataset['localFolder'], 
        dataset['gDriveFolder']
    ))
    log('Done!')

def load_json(file_path):
    with open(file_path, "r") as read_file:
        return json.load(read_file)

for dataset in load_json("datasets.json"):
    download(dataset)
    process(dataset)
    upload(dataset)
    remove_files_in_dir(
        '{}/*'.format(dataset['localFolder'])
    )
