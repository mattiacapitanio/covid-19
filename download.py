import pycurl
from io import BytesIO
import os

class CurlDownloader():

    def _get_filename(self, url): 
        parts = os.path.split(url)
        return parts[len(parts)-1]

    def _write_file(self, content, file_path):
        f = open(file_path, 'w')
        f.write(content)
        f.close()

    def _curl(self, url):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        return buffer.getvalue().decode('utf-8')
        # Body is a byte string.
        # We have to know the encoding in order to print it to a text file
        # such as standard output.
        # print(body.decode('iso-8859-1'))

    def perform(self, urls, destination_folder):
        for url in urls:
            self._write_file(
                self._curl(url),
                '{}/{}'.format(destination_folder, self._get_filename(url))
            )

class KaggleDownloader():
    def perform(self, urls, destination_folder):
        for url in urls:
            os.system('kaggle datasets download {} -p {} --unzip --force'.format(
                url,
                destination_folder
            ))

class Downloader():
    def __init__(self, downloader, destination_folder, urls = []):
        self.urls = urls
        self.downloader = downloader
        self.destination_folder = destination_folder

    def perform(self): 
        self.downloader.perform(
            self.urls, 
            self.destination_folder
        )
