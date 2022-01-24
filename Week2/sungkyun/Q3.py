# 파일의 경로를 file_path로 설정
# ex) file_path = "./data-01-test-score.csv"

file_path = "./data-01-test-score.csv"

def read_file(file_path):
    data_list = list()
    
    with open(file_path) as filepath:
            
        while True:
            data = filepath.readline() # 한줄씩 데이터를 읽어오기
            if not data: break

            else:
                data_list.append(data.split(","))  

    return data_list 

#출력함수
print(read_file(file_path))

#지웅: with open 구문으로 file close부분이 필요없게 구현. 수빈님과 유사한듯
#수빈: 