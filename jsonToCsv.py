import json
import csv

fileToWrite = 'test.csv'
fileToRead  = 'all_data_dump.txt'

#Open file handle
writeFileHandle = open(fileToWrite,'w+', encoding='utf8')

#Define the headers for the data
headers = ['<ALL YOUR HEADERS, COMMA SEPARATED, QUOTED>']

#Create a dictWriter instance and write the header in the file
csv_file = csv.DictWriter(writeFileHandle,fieldnames=headers,restval="Not provided",extrasaction='ignore')
csv_file.writeheader()

#open the file where JSON dump is stored
with open(fileToRead, "r", encoding="utf8") as fileHandle:
    data = fileHandle.readlines()

    #can loop directly over fileHandle too
    for line in data:
        dictJsons = json.loads(line)

        #Selecting the JSON fields to write
        for idx in range(len(dictJsons['<your_json_field>'])):
            csv_file.writerow(dictJsons['<your_json_field>'][idx]['<your_json_field1>'])

print("CSV File ready!")
