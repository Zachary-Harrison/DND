import math

import numpy as np
import matplotlib.pyplot as plt
from Distribution import Distribution


class DiceSet:
    def __init__(self, numOfDice, numOfSides, dropLow=0, dropHigh=0):
        self.numOfDice = numOfDice
        self.numOfSides = numOfSides
        self.dropLow = dropLow
        self.dropHigh = dropHigh
        self.distribution = None
        if not (dropLow == 0 and dropHigh == 0):
            self.distribution = Distribution(self.numOfDice, self.numOfSides, self.dropLow, self.dropHigh)
        self.mean = self.findMean()
        self.standDev = self.findStandDev()

    def findMean(self):
        if self.dropLow == 0 and self.dropHigh == 0:
            return self.numOfDice * (self.numOfSides + 1) / 2
        else:
            return self.distribution.getMean()

    def findStandDev(self):
        if self.dropLow == 0 and self.dropHigh == 0:
            return np.sqrt(self.numOfDice * (self.numOfSides ** 2 - 1) / 12)
        else:
            return self.distribution.getStandDev()

    def printMean(self):
        print("The mean is: ", self.mean)

    def printStandardDev(self):
        print("The standard deviation is: ", self.standDev)

    # 1, 4, 10, 20, 35, 56, 80, 104, 125, 140, 146, 140, 125, 104, 80, 56, 35, 20, 10, 4, 1

    # 1, 4, 10, 21, 38, 62, 91, 122, 148, 167, 172, 160, 131, 94, 54, 21
    # 1, 3,  6, 10, 15, 21, 25,  27,  27,  25,  21,  15,  10,  6,  3,  1
    # 0, 1,  4, 11, 23, 41, 66,  95, 121, 142, 151, 145, 121, 88, 51, 20
    def makeTable(self):
        xList, pList = [], []
        sumMin = self.numOfDice - (self.dropLow + self.dropHigh)
        sumMax = self.numOfSides * (self.numOfDice - (self.dropLow + self.dropHigh))
        if self.dropLow == 0 and self.dropHigh == 0:
            for total in range(sumMin, sumMax + 1):
                print(total, self.f(total))
                pOfTotal = self.f(total)
                if pOfTotal > .00001:
                    pList.append(pOfTotal)
                    xList.append(int(total))
        else:
            pList = self.distribution.getProbList()
            for total in range(sumMin, sumMax + 1):
                xList.append(int(total))

        # print(pList)
        # print(xList)
        if self.numOfDice < 10:
            plt.bar(xList, height=pList, width=.8)
        else:
            plt.bar(xList, height=pList, width=1)
        plt.axis([min(xList) * .95, max(xList) * 1.05, 0, max(pList) * 1.05])
        # [minX, maxX, minY, maxY]
        plt.title("Distribution Graph")
        plt.ylabel('Probability')
        plt.xlabel('Roll Results')
        plt.show()

    def f(self, Total):
        sum = 0
        for k in range(0, ((Total - self.numOfDice) // self.numOfSides) + 1):
            sum += (math.comb(self.numOfDice, k)) * ((-1) ** k) * (
                math.comb(Total - self.numOfSides * k - 1, self.numOfDice - 1))
            print("\tcomb(self.numOfDice, k): ", math.comb(self.numOfDice, k))
            print("\t((-1) ** k): ", ((-1) ** k))
            print("\tmath.comb(Total - self.numOfSides * k - 1, self.numOfDice - 1): ", math.comb(Total - self.numOfSides * k - 1, self.numOfDice - 1))
            print()
        return sum
