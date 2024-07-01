from Matra import MatraCount

class DohaMatraDrop(MatraCount):
    # COnstructor
    def __init__(self, line, matra_count):
        self.line = line
        matra = MatraCount(self.line)

        # scasion of the given Line
        scansion = matra.getScansion()
        sum_of_scansion = MatraCount(self.line).getSumOfMatra()

        # stores modified scansion after matra balancing
        self.modified_scansion = []

        self.candidates = self.dropCandidate(line)

        # how many matra are to be dropped
        how_many_matra_to_drop = sum_of_scansion - 13

        # combinatin of indexes which can be dropped in quarter 1
        combis = self.findCombination(self.candidates, how_many_matra_to_drop)

        # dropping the matra in scanion for making new scansion
        for x in combis:
            new_scansion = scansion[:]
            for y in x:
                new_scansion[y] = 1      # dropping matra at the candidate indexs.
            self.modified_scansion.append(new_scansion[:])
        
    def findCombination(self, candidate, matras_to_drop):
        # variable to store all the combinations
        res = []

        # recursive funtion for finding the combinations. for more information
        # search for combiantions
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



    def dropCandidate(self, line):
        matras = "अंािीुूेैोौं"
        swaras = "अआइईउऊएऐओऔ"
        droppingCandidate = []
        j = -1

        # loop for finding the index which can be dropped
        # it has same approach as finding scansion 
        # if we find a vyanjan which has no matra or a swar or a  matra we increase j and 
        # if swar is the dropping candidate
        # then append it to dropping Candidates
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

    def getModifiedScansion(self):
        return self.modified_scansion

    def getCandidates(self):
        return self.candidates


# a = "बरनउँ रघुबरो बिमल जसु"
# DohaMatraDrop(a, 13)
