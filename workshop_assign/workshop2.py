import json

with open('workshop.json') as f:
    data = json.load(f)
while (True):
    # print(data["birthday"])\
    print ("You want to add birthday in json ?")
    print ("Pass Y to add birthday")
    print ("Pass N to  birthday dictionary")
    status = input("Enter :")
    if (status == "Y" ):
        addname = input("Pass Enter name : ")
        adddata = input("Pass Enter data : ")
        print ("Old json :")
        print (data["birthday"])
        data["birthday"].append({"name":addname, "date":adddata})
        print ("New json :")
        print (data["birthday"])
        print ("------------------")
    elif (status == "N" ):
        print ("Welcome to the birthday dictionary. We know the birthdays of: ")
        for i in data["birthday"]:
            print (i["name"])
            # print (data["birthday"][0]["name"])

        name = input("Who's birthday do you want to look up?")

        for i in range (len(data["birthday"])):
            if (name == data["birthday"][i]["name"]):
                print (name +"'s birthday is "+data["birthday"][i]["date"])
                print ("------------------")