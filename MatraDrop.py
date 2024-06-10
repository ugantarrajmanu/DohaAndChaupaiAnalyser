from Matra import MatraCount

class DohaMatraDrop(MatraCount):
    def __init__(self, line):
        self.line = line
        matra = MatraCount(self.line)
        scansion = matra.getScansion()
        sum_of_scansion = MatraCount(self.line).getSumOfMatra()

        self.modified_scansion = []
        if (matra.getSumOfMatra() > 24):
            index_for_making_quarter = self.breakingScansion(matra.getWordScansion())

            quarter1 = scansion[:index_for_making_quarter]
            quarter2 = scansion[index_for_making_quarter:]

            candidates = self.dropCandidate(line)

            if sum(quarter1) > 13:
                to_drop = []
                for x in candidates:
                    if x < index_for_making_quarter:
                        to_drop.append(x)
                how_many_matra_to_drop = sum(quarter1) - 13
                combis = self.findCombination(to_drop, how_many_matra_to_drop)
                modified_quarter = []
                for x in combis:
                    new_scansion = quarter1[:]
                    for y in x:
                        new_scansion[y] = 1
                    modified_quarter.append(new_scansion[:])
                self.modified_scansion.append(modified_quarter)

            if sum(quarter2) > 11:
                to_drop.clear()
                for y in candidates:
                    if y > index_for_making_quarter:
                        to_drop.append(y)
                how_many_matra_to_drop = sum(quarter2) - 11
                combis = self.findCombination(to_drop, how_many_matra_to_drop)
                modified_quarter = []
                for x in combis:
                    new_scansion = quarter2[:]
                    for y in x:
                        new_scansion[y-11] = 1
                    modified_quarter.append(new_scansion[:])
                self.modified_scansion.append(modified_quarter)

        else:
            print("\tno error")

    def findCombination(self, candidate, matras_to_drop):
        res = []

        def combination(start, comb):
            if len(comb) == matras_to_drop:
                res.append(comb[:])
                return
            
            for i in range(start, len(candidate)):
                comb.append(candidate[i])
                combination(i+1, comb)
                comb.pop()
        combination(0, [])
        return res
    
    def breakingScansion(self, word_scansion):
        count = 0
        i = 0
        index = 0
        while count < 13:
            count += sum(word_scansion[i])
            index += len(word_scansion[i])
            i += 1
        return index

    def dropCandidate(self, line):
        matras = "अंािीुूेैोौं"
        swaras = "अआइईउऊएऐओऔ"
        droppingCandidate = []
        j = -1
        for i in range(len(line)):
            if ((line[i] >= "क" and line[i] <= "ह")):
                if (i+1 == len(line)):
                    j += 1
                elif (line[i+1] not in matras and line[i+1] != "्"):
                    j += 1
            elif (line[i] in swaras):
                j += 1
                if (line[i] == "ए" or line[i] == "ओ"):
                    droppingCandidate.append(j)
            elif (line[i] in matras):
                j += 1
                if (line[i] == "े" or line[i] == "ो"):
                    droppingCandidate.append(j)
        return droppingCandidate


    def getDroppedScansionOfDoha(self):
        return self.modified_scansion
        # for i in range (len(self.modified_scansion)):
        #     print("\tQuarter", i+1, ":")
        #     self.printQuarters(i)
        #     for x in self.modified_scansion[i]:
        #         print("\t\t\t", x)

    def printQuarters(self, i):
        index_for_making_quarter = self.breakingScansion(MatraCount(self.line).getWordScansion())
        scansion = MatraCount(self.line).getScansion()
        quarter1 = scansion[:index_for_making_quarter]
        quarter2 = scansion[index_for_making_quarter:]
        print("\t\toriginally --> ", quarter1, "\n\t\tmodified: -") if i == 0 else print("\t\toriginally -> ", quarter2, "\n\t\tmodified: -")



class ChaupaiMatraDrop(MatraCount):
    def __init__(self, line):
        super().__init__(line)
        self.line = line.split(" ")
        matra = MatraCount(self.line)
        scansion = matra.getScansion()
        sum_of_scansion = matra.getSumOfMatra()
        self.modified_scansion = []

        if sum_of_scansion > 16:
            matras_to_drop = sum_of_scansion - 16
            candidates = self.dropCandidate(line)
            combis = self.findCombination(candidates, matras_to_drop)
            for x in combis:
                new_scansion = scansion[:]
                for y in x:
                    new_scansion[y] = 1
                self.modified_scansion.append(new_scansion[:])

    def dropCandidate(self, line):
        matras = "अंािीुूेैोौं"
        swaras = "अआइईउऊएऐओऔ"
        droppingCandidate = []
        j = -1
        for i in range(len(line)):
            if ((line[i] >= "क" and line[i] <= "ह")):
                if (i+1 == len(line)):
                    j += 1
                elif (line[i+1] not in matras and line[i+1] != "्"):
                    j += 1
            elif (line[i] in swaras):
                j += 1
                if (line[i] == "ए" or line[i] == "ओ"):
                    droppingCandidate.append(j)
            elif (line[i] in matras):
                j += 1
                if (line[i] == "े" or line[i] == "ो"):
                    droppingCandidate.append(j)
        return droppingCandidate


    def findCombination(self, candidate, matras_to_drop):
        res = []

        def combination(start, comb):
            if len(comb) == matras_to_drop:
                res.append(comb[:])
                return
            
            for i in range(start, len(candidate)):
                comb.append(candidate[i])
                combination(i+1, comb)
                comb.pop()
        combination(0, [])
        return res

    def getDroppedScansionOfChaupai(self):
        print("Original ->\t", MatraCount(self.line).getScansion(), "\nmodified: -")
        for x in self.modified_scansion:
            print("\t->\t", x)


# a = """महाबीर बिक्रबे बजरंगी
# कुमति निवार सुमति के संगी
# कंचन बरन बिराज सुबेसा
# कानन कुण्डल कुँचित केसा"""
# a = a.split("\n")
# ChaupaiMatraDrop(a[0]).getDroppedScansionOfChaupai()
