from fileinput import filelineno
import Q4

file_path = "./data-01-test-score.csv"

class ReadCSV_Q5(Q4.ReadCSV):
    #Q4에서 만든 객체를 상속해서 초기화
    def __init__(self,file_path):
        super().__init__(file_path)
    
    #알아보기 힘든 ver
    # def merge_list(self):
    #     if len(super().data) == 0 :
    #         super().read_file()
    #     try:
    #         return sorted([(
    #                 sum(list(map(
    #                     lambda x : int(x) ,line))) 
    #                 /float(len(line))) 
    #             for line in super().data])
    #     except ValueError:
    #         print("숫자형 문자가 아닌 것이 들어있습니다.")
    #         return []
        
    #알아보기 쉽게 만든 ver
    def merge_list(self):
        if len(super().data) == 0: # 아직 데이터를 읽어오지 않았다면 읽어준다.
            super().read_file()
        result = []
        for line in super().data: # 한개의 list씩 살펴본다
            try:
                line = [int(x) for x in line] # 문자형인 데이터를 정수형으로 바꿔줌
                result.append(sum(line)/len(line)) # 평균값을 구해서 result list에 append
            except ValueError:
                print("숫자형 문자가 아닌 것이 들어있습니다.")
                return []
        return sorted(result)

                
read_csv_Q5 = ReadCSV_Q5(file_path)
print(read_csv_Q5.merge_list())