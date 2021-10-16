import pandas
file_1_list = pandas.read_csv("file1.txt")
file_2_list = pandas.read_csv("file2.txt")
result = [int(num) for num in file_2_list if num in file_1_list]
print(result)