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
            self.__merge_list.append(sum)
        return self.__merge_list


file_path = "./data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())

#지웅: 잘 구현 하셨지만 역시 파일을 닫는 부분이 없어서 아쉽습니다!