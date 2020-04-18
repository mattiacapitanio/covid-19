import pandas as pd 
import sys
import os

DATA_DIR = sys.argv[1]

class Covid19ItalyProcessor():
    INPUT_REGION_FILENAME = 'covid19_italy_region.csv'
    OUTPUT_REGION_FILENAME = 'covid19_italy_region_groupby_date.csv'

    def files_to_process(self): 
        return [
            self.INPUT_REGION_FILENAME
        ]
    def process(self, file, data_dir):
        if file == self.INPUT_REGION_FILENAME:
            self._process_file_region(file, data_dir)

    def _get_file_region_columns(self):
        return [
            'Date', 
            'HospitalizedPatients', 
            'IntensiveCarePatients', 
            'TotalHospitalizedPatients', 
            'HomeConfinement', 
            'CurrentPositiveCases', 
            'NewPositiveCases', 
            'Recovered', 
            'Deaths', 
            'TotalPositiveCases', 
            'TestsPerformed'
        ]

    def _process_file_region(self, file, data_dir):
        print('Process file: {}'.format(file))
        df = pd.read_csv(
            '{}/{}'.format(data_dir, file), 
            usecols=self._get_file_region_columns()
        )
        group_by_date = df.groupby(df['Date'].str[0:10])
        group_by_date.sum().to_csv(
            '{}/{}'.format(data_dir, self.OUTPUT_REGION_FILENAME)
        )

class Covid19WorldProcessor():
    def files_to_process(self): 
        return []
    def process(self):
        pass

class Covid19KoreaProcessor():
    def process(self):
        pass
    def files_to_process(self): 
        return []

class Processor:
    def __init__(self, data_dir, processor):
        self._data_dir = data_dir
        self._processor = processor

    def _files_in_dir(self, path):
        files = []
        for r, d, f in os.walk(path):
            for file in f:
                files.append(file)
        return files

    def process(self):
        files_in_dir = self._files_in_dir(self._data_dir)
        for f in self._processor.files_to_process():
            if f in files_in_dir:
                self._processor.process(f, self._data_dir)

Processor(DATA_DIR, Covid19ItalyProcessor()).process()
Processor(DATA_DIR, Covid19KoreaProcessor()).process()
Processor(DATA_DIR, Covid19WorldProcessor()).process()