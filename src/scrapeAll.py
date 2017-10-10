import requests, json

base_url = 'BASE_URL_HERE'

#make the first request
base_json = requests.get(base_url)

#open the file for writing - note the file is going to overwrite if data is already present. Change the mode, if needed
with open("all_data.txt", 'w', encoding="utf8") as fileHandle:
    
    #write the json data to the file
    fileHandle.write(base_json.text)
    
    #create dict
    base_json = json.loads(base_json.text)

    #loop over the json till next field is populated
    while base_json['next']:
        #print("Next URL:", base_json['next'])
        #make the GET call to the "next" url 
        base_json = requests.get(base_json['next'])
        fileHandle.write(base_json.text)
        base_json = json.loads(base_json.text)

print("ALL DONE!")
