
file_path = "./data-01-test-score.csv"

# def read_file(file_path):
#     f = open(file_path)
#     data = f.read().split('\n')
#     data = [i.split(',') for i in data ]
#     return data

#short_ver : 
def read_file(file_path):
    try:
        f = open(file_path,'r')
        result = [line.split(',') for line in f.read().split()]
        f.close()
        return result
    except FileNotFoundError as e:
        print(e)
        return []
    

print(read_file(file_path))
