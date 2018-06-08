import json

with open('workshop.json') as f:
    data = json.load(f)
# print (data["birthday"])
month = []
dit = []
for i in range (len(data["birthday"])):
    month.append(data["birthday"][i]["date"].split("/"))

for i in range (len(month)):
    dit.append(month[i][1]) 
# print (dit)        

for i in range (len(dit)):
    print ("month is : "+dit[i])
    for j in range (len(data["birthday"])):
        # print (data["birthday"][j]["date"].split("/")[1])
        if (dit[i]== data["birthday"][j]["date"].split("/")[1]):
            print ("Name :"+data["birthday"][j]["name"])
