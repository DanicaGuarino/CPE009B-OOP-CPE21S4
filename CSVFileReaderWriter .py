from FileReaderWriter import FileReaderWriter
import csv


class CSVFileReaderWriter(FileReaderWriter):
        def read(self, filepath):
            with open (filepath, newline='') as csvfile:
                data = csv.reder(csvfile, delimeter=',', quotechar='|')
                for row in data:
                    print (row)
                return data
        
        def write(self, filepath, data):
            with open(filepath,'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimeter=',',
                                    quotechar='|',quoting=csv.QUOTE_MINIMAL)
                writer.writerow(data)
