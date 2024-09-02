import csv
import os
import json

with open(os.path.join(os.getcwd(),'dataset','Medicine_Details.csv'), 'r') as csvFile:  
    csvFile = csv.reader(csvFile)
    data = [] 
    for lines in csvFile: 
        record = {
            "medicine_name": str(lines[0]).lower(), 
            "composition": str(lines[1]).lower(), 
            "uses": str(lines[2]).lower(), 
            "side_effects": str(lines[3]).lower()
        } 
        
        data.append(record)

    # r = data[0:1000] 
    # r.extend(data[3000:4000])
    # r.extend(data[6000:7000]) 
    # r.extend(data[10000:11000])

    print(len(data))


with open(os.path.join(os.getcwd(),'dataset','Medicine_Details.json'), 'w') as jFile:  
    json.dump(data,jFile)

     

 

 