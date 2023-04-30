import random
top_of_range = input("type a number ")

if(top_of_range.isdigit()):
    top_of_range = int(top_of_range)

if(top_of_range<=0):
    print("please type a number bigger than 0")
    quit()
else:
    print("please type a number")

c  = random.randint(0,top_of_range)

print(c)

 