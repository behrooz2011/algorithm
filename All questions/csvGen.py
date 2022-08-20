import csv
import json

# csvfile = open('file1.csv', 'r')
# jsonfile = open('file.json', 'w')

# fieldnames = ("FirstName","LastName","IDNumber","Message")
# reader = csv.DictReader( csvfile, fieldnames)
# for row in reader:
#     json.dump(row, jsonfile)
#     jsonfile.write('\n')
arr=[]
with open ('file2.csv') as myFile:
    reader = csv.DictReader(myFile)
    for row in reader:
        arr.append(row)
    print(arr)