#!/usr/bin/env python3

import random

print("Hello! Welcome to the Apple Lottery. Please answer the questions below to get started.")
print("In this lottery the numbers that are drawn CANNOT be identical!")
print("Remember to choose different lottery numbers! So no [2, 2]!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

iterations = int(input("How many rolls (iterations)? "))
nums = []

myNum1 = int(input("What is your 1st Lottery Pick? "))
myNum2 = int(input("What is your 2nd Lottery Pick? "))
printDataInput = input("Should I print all of the rolls that were generated? (y/n) ")

if(printDataInput == 'y'):
    printData = True
else:
    printData = False

yellow = 0
red = 0
green = 0

num1 = 0
num2 = 0

for i in range(iterations):
    num1 = random.randint(1, 6    )    
    num2 = random.randint(1, 6)

    while(num2 == num1):
        num2 = random.randint(1, 6)

    nums.append([num1, num2])

if(printData):
    print(nums)

for i in range(0, len(nums)):
    if(nums[i] == [myNum1, myNum2] or nums[i] == [myNum2, myNum1]):
        yellow += 1
    elif(nums[i][1] == myNum1 or nums[i][1] == myNum2 or nums[i][0] == myNum1 or nums[i][0] == myNum2):
        green += 1
    else:
        red += 1

redExP = red / iterations
yellowExP = yellow / iterations
greenExP = green / iterations

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Yellow: ", yellow)
print("Red: ", red)
print("Green: ", green)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Yellow Experimental Probability: ", yellowExP)
print("Red Experimental Probability: ", redExP)
print("Green Experimental Probability: ", greenExP)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
