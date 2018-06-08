birthday ={
    "Albert Einstein" : "9/12/1995",
    "Benjamin Franklin" : "16/2/1990",
    "Ada Lovelace" : "26/11/2011",
}

print ("Welcome to the birthday dictionary. We know the birthdays of: ")
for key,value in birthday.items():
    print (key)

name = input("Who's birthday do you want to look up?")
if name in birthday:
    print (name +"'s birthday is "+birthday[name])