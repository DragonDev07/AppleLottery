import random

iterations = int(input("How many iterations? "))
nums = []

myNum1 = int(input("What is your 1st Lottery Pick? "))
myNum2 = int(input("What is your 2nd Lottery Pick? "))

yellow = 0
red = 0
green = 0

for i in range(iterations):
    nums.append([random.randint(1, 6), random.randint(1, 6)])

print(nums)

for i in range(len(nums)):
    if(nums[i] == [myNum1, myNum2]):
        yellow += 1

print("Yellow: ", yellow)
print("Red: ", red)
