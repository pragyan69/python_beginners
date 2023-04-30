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

while True:
     user_guess = input("make a guess ")
     if user_guess.isdigit():
         user_guess = int(user_guess)
     else:
         print("Please print a number nexct time")
         continue
     

     if user_guess == c:
         print("you get it")
     else:
         print("fuck off")




 