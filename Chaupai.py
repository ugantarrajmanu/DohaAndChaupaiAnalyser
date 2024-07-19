from Repo.Matra import MatraCount, PronunciationDictionary as pd

class Chaupai:
    def __init__(self, chaupai):
        self.chaupai = chaupai.split("\n")
        self.score = 0
        self.rhtyhm = []
        matra_balance = False
        chaupai_type = 0
        
        for line in self.chaupai:
            scansion = MatraCount(line).getScansion()
            
            if sum(scansion) == 16:
                pronunciation = pd(line, scansion).getPronunciation()
                sentence_pronunciation = []
                for x in pronunciation:
                    for y in x:
                        sentence_pronunciation.append(y)
                
                word_pronunciation_sum = []
                for x in pronunciation:
                    temp = []
                    for y in x:
                        temp.append(sum(y))
                    word_pronunciation_sum.append(temp[:])

                temp_sum_of_pronunciation = []
                for x in sentence_pronunciation:
                    temp_sum_of_pronunciation.append(sum(x))

                # print(temp_sum_of_pronunciation)

                temp_rhythm = []
                
                for x in word_pronunciation_sum:
                    if sum(x) <= 4:
                        if sum(x) == 2:
                            temp_rhythm.append("D")
                        elif sum(x) == 3:
                            temp_rhythm.append("T")
                        elif sum(x) == 4:
                            temp_rhythm.append("C")
                    else:
                        count = 0
                        for y in x:
                            count += y
                            if count == 2:
                                if len(temp_rhythm) > 1 and temp_rhythm[-1] == "T" and temp_rhythm[-2] != "T":
                                    continue
                                temp_rhythm.append("D")
                                count = 0
                            elif count == 3:
                                temp_rhythm.append("T")
                                count = 0
                
                for3 = 0
                for i in range (0, len(temp_rhythm)):
                    if temp_rhythm[i] == "T":
                        for3 += 1
                        if temp_rhythm[i+1] != "T" and for3 != 2:
                            chaupai_type = 2
                        elif for3 == 2:
                            for3 = 0

                self.rhtyhm.append(temp_rhythm[:])

            else:
                chaupai_type = 3

            if chaupai_type == 3:
                self.score = 1
            elif chaupai_type == 2:
                self.score = 2
            else:
                self.score = 3

    
    def getRhythm(self):
        return self.rhtyhm
    
    def getScore(self):
        return str(self.score) + "/3 (" + str(self.score/3) + ")"
    
    def getType(self):
        if self.score == 1:
            return "Type 3"
        if self.score == 2:
            return "Type 2"
        if self.score == 3:
            return "Type 1"


a = "जय हनुमान ज्ञान गुण सागर\nजय कपीस तिहुँ लोक उजागर\nराम दूत अतुलित बल धामा\nअंजनि पुत्र पवनसुत नामा"
print(Chaupai(a).getRhythm())
print(Chaupai(a).getScore())
print(Chaupai(a).getType())