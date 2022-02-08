class Distribution:
    def __init__(self, numOfDice, numOfSides, dropLow, dropHigh):
        self.keepGoing = True
        self.numOfDice = numOfDice
        self.numOfSides = numOfSides
        self.dropLow = dropLow
        self.dropHigh = dropHigh
        self.head = [numOfSides]*numOfDice

        listLength = (self.numOfSides - 1) * (self.numOfDice - (self.dropLow + self.dropHigh)) + 1
        fList = [0] * listLength
        while self.keepGoing:
            tempList = self.head.copy()
            tempList.sort()
            tempList = tempList[self.dropLow: (self.numOfDice - self.dropHigh)]
            fList[sum(tempList) - (self.numOfDice - (self.dropLow + self.dropHigh))] += 1
            self.downOne()
        self.pList = [0] * listLength
        for i in range(len(self.pList)):
            self.pList[i] = fList[i] / (self.numOfSides ** self.numOfDice)

        self.mean = self.getMean()
        self.standDev = self.getStandDev

    def downOne(self):
        for i in range(self.numOfDice):
            if self.head[i] > 1:
                self.head[i] -= 1
                return
            elif self.head[i] == 1:
                self.head[i] = self.numOfSides
                if (i+1) < self.numOfDice and self.head[i + 1] > 1:
                    self.head[i+1] -= 1
                    return
        self.keepGoing = False

    def getProbList(self):
        return self.pList

    def getMean(self):
        mean = 0
        for i in range(len(self.pList)):
            index = i + (self.numOfDice - (self.dropLow + self.dropHigh))
            mean += index * self.pList[i]
        return mean

    def getStandDev(self):
        standDev = 0
        for i in range(len(self.pList)):
            index = i + (self.numOfDice - (self.dropLow + self.dropHigh))
            standDev += self.pList[i] * (index - self.mean) ** 2
        standDev = standDev ** .5
        return standDev

