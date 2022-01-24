def read_file(filepath):
    file = open(filepath, "r")
    csv_list = []
    while True:
        line = file.readline().strip("\n")
        if not line:
            break
        csv_list.append(line.split(","))
    return csv_list

file_path = "./data-01-test-score.csv"
print(read_file(file_path))

#지웅: 저나 재연님과 마찬가지 파일을 닫는 부분이 없는 게 좀 아쉽습니다. 반복문 + append로 구현한 모습. list comprehension을 써봅시다.