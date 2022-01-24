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