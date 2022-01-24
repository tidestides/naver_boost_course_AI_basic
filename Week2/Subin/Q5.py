class ReadCSV():
    def __init__(self, filepath):
        self.__filepath = filepath
        self.__csv_list = []
        self.__merge_list = []

    def read_file(self):
        file = open(self.__filepath,"r")
        while True:
            line = file.readline().strip("\n")
            if not line:
                break
            self.__csv_list.append(line.split(","))
        return self.__csv_list
    
    def merge_list(self):
        for item in self.__csv_list:
            sum = 0
            for data in item:
                sum += int(data)
            self.__merge_list.append(sum/len(item))
        self.__merge_list.sort()
        return self.__merge_list


file_path = "./data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())

#지웅: sum() 을 리스트에 적용하면 안에 있는 원소들을 다 더한 값을 반환해 줍니다. 참고하시길 바랍니다!