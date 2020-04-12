import os
import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# TODO: add pkg to read params 
DATA_DIR = sys.argv[1]
GDRIVE_FOLDER_ID = sys.argv[2]

def update_file(file_name, file_id):
  file = drive.CreateFile({
    'id': file_id,
    'parents': [{ 'id': GDRIVE_FOLDER_ID }], 
    'title': file_name
  })  
  file.SetContentFile('{}/{}'.format(DATA_DIR, file_name))
  file.Upload()
  print('updated file: {}'.format(file_name))

def create_file(file_name):
  file = drive.CreateFile({
    'parents': [{'id': GDRIVE_FOLDER_ID}], 
    'title': file_name
  })
  file.SetContentFile('{}/{}'.format(DATA_DIR, file_name))
  file.Upload()
  print('create file: {}'.format(file_name))

def files_in_dir(path):
  files = []
  for r, d, f in os.walk(path):
      for file in f:
          if '.zip' in file or '.csv' in file:
              files.append(file)
  return files

# Creates local webserver and auto handles authentication.
def get_gdrive():
  gauth = GoogleAuth()
  gauth.LocalWebserverAuth() 
  return GoogleDrive(gauth)

def files_in_gdrive(drive):
  gdrive_files = {}
  files = drive.ListFile({
      'q': '"{}" in parents and trashed=false'.format(GDRIVE_FOLDER_ID)
    }).GetList()
  for f in files:
    gdrive_files[f['title']] = f['id']
  return gdrive_files 

def upload(files_to_upload, gdrive_files):
  for f in files_to_upload:
    if f in gdrive_files:
      update_file(f, gdrive_files[f])
    else:
      create_file(f)

if GDRIVE_FOLDER_ID is None: 
  print('Error: GDRIVE_FOLDER_ID not defined!')
elif DATA_DIR is None:
  print('Error: DATA_DIR not defined!')
else: 
  drive = get_gdrive()
  upload(
    files_in_dir(DATA_DIR),
    files_in_gdrive(drive)
  )
