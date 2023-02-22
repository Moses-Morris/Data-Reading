from csv import reader

open_File = open("titanic.csv")
read_File = reader(open_File)

data_from_file = list(read_File)

print(data_from_file[0:])
print("Number of Rows : ",len(data_from_file))

open_File.close()
