# Store power in a variable
# While 2 raised to the power is less than 
# 
# For 100!, divide it by 2. Then, with 100/2, divide it further, adding it to the virtual count.
# Stop dividing until the factorial is less than 1.
import math

def calculateMaxPower(base, FACTORIAL):
    # base = int(input("Greatest power of: "))
    # FACTORIAL = int(input("What is the factorial? "))
    numToBeDividedTillOne = FACTORIAL
    total = 0
    while numToBeDividedTillOne > 1:
        numToBeDividedTillOne = math.floor(numToBeDividedTillOne/base)
        total = total + numToBeDividedTillOne

    return total

print(calculateMaxPower(int(input("Greatest power of: ")), int(input("What is the factorial? "))))
print(calculateMaxPower(2, 100))
print(calculateMaxPower(2, 2023))
print(calculateMaxPower(40, 2023))
print(calculateMaxPower(7, 2831))
print(calculateMaxPower(151, 2831))
print(calculateMaxPower(2, 2831))
