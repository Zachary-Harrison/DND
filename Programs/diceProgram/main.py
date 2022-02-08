import sys
from DiceSet import DiceSet
import math


if __name__ == "__main__":
    # n = 100
    # for i in range(n+1):
    #     print(f"{i}! = {math.factorial(n)}")
    #
    # for r in range(n+1):
    #     print(f"C({n}, {r}) = {math.comb(n, r)}")
    args = sys.argv[1:]
    if len(args) < 1:
        print("Error: Too few arguments.")
        sys.exit(1)
    numOfDice = int(args[0].split("d")[0])
    numOfSides = int(args[0].split("d")[1])
    if len(args) == 1:
        diceSet = DiceSet(numOfDice, numOfSides)
    elif len(args) < 2:
        print("Error: Incorrect Number of arguments")
        sys.exit(1)
    else:
        dropLowest = int(args[1][1:])  # drop minus sign
        dropHighest = int(args[2][1:])  # drop plus sign
        diceSet = DiceSet(numOfDice, numOfSides, dropLowest, dropHighest)
    diceSet.printMean()
    diceSet.printStandardDev()
    diceSet.makeTable()


