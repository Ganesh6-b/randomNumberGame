import random
import sys

randomnum = random.randint(1,9)

guess = 0
count = 0
while guess!=randomnum and guess != "exit":
    guess = int(input("enter the random number:"))
    if guess == "exit":
        break;
    count+=0
    if guess<randomnum:
        print("Your guessed num is less that randomnum")
    elif guess>randomnum:
        print("Your guessed num is greater than randomnum")
    elif guess==randomnum:
        print("Wow! you found that correct number")
        print("You made only {} tries".format(count))
    else:
        print("Enter the valid number")
