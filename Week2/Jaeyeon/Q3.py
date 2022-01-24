file_path = "./data-01-test-score.csv"

def read_file(file_path):
    try:
        return [line.split(',') for line in open(file_path).read().split()]
    except FileNotFoundError as e:
        print(e)
        return []

#지웅: list comprehension으로 pythonci하게 구현 그러나 open할 파일을 닫는 부분이 없음.. 저도 마찬가지여서 수정했습니다.
print(read_file(file_path))