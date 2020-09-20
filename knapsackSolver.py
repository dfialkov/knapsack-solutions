class knapsackSolver:
    def __init__(self, objects, cap):
        self.objects = objects
        self.cap = cap
        self.powerSet = [[]]

    def displayResult(self, maxSet):
        maxSetVal = 0
        for i in maxSet:
            maxSetVal += i[1]
        print(maxSetVal)
        setWeight = 0
        for i in maxSet:
            setWeight += i[0]
        print(setWeight)
        for i in maxSet:
            print(str(i[2]), end=" ")

    def greedy(self):
        self.objects.sort(key=lambda x: (x[1]/x[0], -x[1]))
        self.objects.reverse()
        runningWeight = self.cap
        knapsack = []
        for obj in self.objects:
            if obj[0] <= runningWeight:
                knapsack.append(obj)
                runningWeight -= obj[0]
        self.displayResult(knapsack)

    def exhaustive(self):
        self.findPowerSet()
        maxSetVal = 0
        maxSet = []
        for subset in self.powerSet:
            setWeight = 0
            setVal = 0
            for obj in subset:
                setWeight += obj[0]
                setVal += obj[1]
            if setWeight <= self.cap and setVal > maxSetVal:
                maxSetVal = setVal
                maxSet = subset
        self.displayResult(maxSet)
        
    def findPowerSet(self):
        #The full powerset kills my computer if I generate it.
        #Therefore, I will skip generating powersets that cross the the weight cap to save on memory, since they are ineligible for the optimal solution anyway. 
        #This means that a set always caps out at 25 units(in practice, much lower) so the processing time cost is tiny
        #Still tons of comparisons though.  
        self.powerSet = [[]]
        #for every object...
        for idx, obj in enumerate(self.objects):
            #Power set in progress length should not update 
            subsetLen = len(self.powerSet)
            #for every set in the power set so far...
            for i in range(subsetLen):
                #if the power set has room for this item...
                setWeight = 0
                for item in self.powerSet[i]:
                    setWeight += item[0]
                if setWeight + obj[0] <= self.cap:
                    #append the object to the current set
                    self.powerSet.append(self.powerSet[i] + [obj])
            #report how many items were generated after processing the current item
            print (str(idx+3) + ": " + str(len(self.powerSet)))


def main():
        mode = input("Enter e for exhaustive or g for greedy: \n")
        inputFile = open("input.txt", "r")
        sackCap = int(inputFile.readline())
        objCount = int(inputFile.readline())
        objects = []
        for i in range(objCount):
            nextObj = inputFile.readline().split()
            objects.append((int(nextObj[0]), int(nextObj[1]), i+1))
        solver = knapsackSolver(objects, sackCap)
        if mode == "e":
            solver.exhaustive()
        elif mode == "g":
            solver.greedy()
        
if __name__ == "__main__":
    main()
