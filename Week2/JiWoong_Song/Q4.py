from os import read


file_path = "./data-01-test-score.csv"

class ReadCSV():
    def __init__(self,file_path):
        self.__file_path = file_path
        self.__data = []
    @property
    def data(self):
        return self.__data
    # 없어도 되는데??
    
    def read_file(self):
        try:
            self.__data = [line.split(',') for line in open(file_path).read().split()]
            return self.__data
        except FileNotFoundError as e:
            print(e)
            return []
    
    def merge_list(self):
        if len(self.__data) == 0:
            self.read_file(self)
        return [sum(list(map(
            lambda x: int(x),line))) 
                for line in self.__data]

if __name__ == '__main__':
    read_csv = ReadCSV(file_path)

    print(read_csv.read_file())
    print(read_csv.merge_list())