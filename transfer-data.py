import json
import os
from download import Downloader, CurlDownloader, KaggleDownloader
import glob

def remove_files_in_dir(folder):
    files = glob.glob(folder)
    for f in files:
        os.remove(f)



with open("datasets.json", "r") as read_file:
    data = json.load(read_file)

for dataset in data:
    print('Download dataset')
    if dataset['type'] == 'url':
        Downloader(
            CurlDownloader(), 
            dataset['localFolder'],
            dataset['sourceUrls']
        ).perform()
    elif dataset["type"] == "kaggle":
        Downloader(
            KaggleDownloader(), 
            dataset['localFolder'],
            dataset['sourceUrls']
        ).perform()
    else:
        continue
    print('Process dataset')
    os.system('python3 process.py {}'.format(
        dataset['localFolder']
    ))
    print('Upload dataset')
    os.system('python3 upload.py {} {}'.format(
        dataset['localFolder'], 
        dataset['gDriveFolder']
    ))
    remove_files_in_dir('{}/*'.format(dataset['localFolder']))
