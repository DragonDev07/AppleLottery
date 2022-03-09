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

print("Yellow: ", yellow)
print("Red: ", red)
print("Green: ", green)

print("Yellow Experimental Probability: ", yellowExP)
print("Red Experimental Probability: ", redExP)
print("Green Experimental Probability: ", greenExP)
