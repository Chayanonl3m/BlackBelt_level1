import random
num = random.randint(1, 10)
loop = True
while loop:
    date = int(input("Guess the number: "))
    if date == num:
        print ("Correct!")
        loop = False
    else :
        print ("Wrong, try again! ")

