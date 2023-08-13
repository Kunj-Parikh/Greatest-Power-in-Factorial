import math

def calculateMaxPower(base, FACTORIAL):
    
    # Notice that you have to divide the factorial by the power to get the multiple of the base raised to the n+1 power.
    # Therefore, divide the factorial repeatedly until it is equal to 1, at which point return the total. 
    
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
