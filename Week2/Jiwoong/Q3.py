
file_path = "./data-01-test-score.csv"

# def read_file(file_path):
#     f = open(file_path)
#     data = f.read().split('\n')
#     data = [i.split(',') for i in data ]
#     return data

#short_ver : 
def read_file(file_path):
    try:
        return [line.split(',') for line in open(file_path).read().split()]
    except FileNotFoundError as e:
        print(e)
        return []

print(read_file(file_path))
