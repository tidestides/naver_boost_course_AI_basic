import re
file_path = "./data-01-test-score.csv"
data_list = list()


class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path
    

    def read_file(self):
        
        with open(file_path, "r", newline='') as filepath:
                
            while True:
                data = filepath.readline()
                if not data: break

                else:
                    data_list.append(data.split(","))  

        return data_list

    def merge_list(self):
        
        with open(file_path, "r", newline='') as filepath:
                
            while True:
                data = filepath.readline() 
                if not data: break

                else:
                    data_list.append(data.split(","))
               

        total_list = []
        for line in data_list:
            
            t_data = line
            total = 0
            count = 0
            for t in t_data:
                total = total + int(re.sub(',', '', t))
                count+=1
            total_list.append(total/count)
            total_list.sort()
        return total_list


read_csv = ReadCSV(file_path)
#print(read_csv.read_file())
print(read_csv.merge_list())