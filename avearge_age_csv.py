from csv import reader

open_File = open("titanic.csv")
read_File = reader(open_File)

data_from_file = list(read_File)

#print(data_from_file[0:])
#print(len(data_from_file))

length = len(data_from_file)
total = 0
for eachRow in data_from_file[1:]:
    age = eachRow[4]
    try:
        age = float(age)
    except:
        print("Error. Invalid age Type: ", age)

    print(age)
    total  +=  age

print("The total age is : ", total)
average = total / length
print("The average age is : ", average)
open_File.close()
