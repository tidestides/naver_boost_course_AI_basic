import csv
from fileinput import filelineno
import Q4

file_path = "./data-01-test-score.csv"

class ReadCSV_Q5(Q4.ReadCSV):
    def __init__(self,file_path):
        super().__init__(file_path)
    
    def merge_list(self):
        if len(super().data) == 0 :
            super().read_file()
        return [
            (
                sum(list(map(lambda x : int(x) ,line)))/
                float(len(line))) 
            for line in super().data
            ]

read_csv_Q5 = ReadCSV_Q5(file_path)
print(read_csv_Q5.merge_list())