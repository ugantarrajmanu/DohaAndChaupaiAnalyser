# This is for operations on Doha 
# like getting its scansion, breaking doha into quarters
# getting pronunciation of words, and at last rhythm of the
# Doha but for only Doha without matra balancing case.

from Matra import MatraCount, PronunciationDictionary as pd
from MatraDrop import DohaMatraDrop
from termcolor import colored, cprint

class Doha:
    # takes a doha line and then converts it into list
    def __init__(self, doha: str):
        output = {}

        doha = doha.split("\n")

        self.scansion_quartered =  []
        self.doha_quartered = []
        self.word_pronunciation = []
        self.sentence_pronunciation = []
        self.rhythm = []

        for x in doha:
            a = MatraCount(x).getSentenceQuarter()
            for i in a:
                self.doha_quartered.append(i)
        for x in self.doha_quartered:
            a = MatraCount(x).getScansion()
            self.scansion_quartered.append(a[:])
        
        for x in range (0, len(self.scansion_quartered)):
            a = pd(self.doha_quartered[x], self.scansion_quartered[x]).getPronunciation()
            self.word_pronunciation.append(a)
        
        for i in range(len(self.scansion_quartered)):
            if sum(self.scansion_quartered[i]) == (13 if i == 0 or i == 2 else 11):
                print(sum(self.scansion_quartered[i]))

                for x in self.word_pronunciation:
                    temp = []
                    for y in x:
                        for z in y:
                            temp.append(z)
                    self.sentence_pronunciation.append(temp[:])
                    temp.clear()

                first_rhythm = 0
                temp_rhythm = []
                for x in self.word_pronunciation[i][0]:
                    first_rhythm += sum(x)
                if first_rhythm == 4:
                    temp_rhythm.append("C")
                    count = 0
                    for x in range(len(self.word_pronunciation[i][0]), len(self.sentence_pronunciation[i])):
                        if len(temp_rhythm) < 2:
                            count += sum(self.sentence_pronunciation[i][x])
                        if len(temp_rhythm) >= 2:
                            for y in self.sentence_pronunciation[i][x]:
                                temp_rhythm.append(y)
                        if count == 4:
                            temp_rhythm.append("C")
                            count = 0
                    self.rhythm.append(temp_rhythm[:])
                    temp_rhythm.clear()
                
                elif first_rhythm == 3:
                    temp_rhythm.append("T")
                    count = 0
                    found3 = False
                    for x in range(len(self.word_pronunciation[i][0]), len(self.sentence_pronunciation[i])):
                        if len(temp_rhythm) < 3:
                            count += sum(self.sentence_pronunciation[i][x])
                            if count == 3 and not found3:
                                temp_rhythm.append("T")
                                found3 = True
                                count = 0
                            elif count == 2 and found3:
                                temp_rhythm.append("D")
                                count = 0
                        else:
                            for y in self.sentence_pronunciation[i][x]:
                                temp_rhythm.append(y)
                    
                    self.rhythm.append(temp_rhythm[:])
                    temp_rhythm.clear()
                
                elif first_rhythm == 2:
                    count = first_rhythm
                    for x in range(len(self.word_pronunciation[i][0]), len(self.sentence_pronunciation[i])):
                        if len(temp_rhythm) < 2:
                            count += sum(self.sentence_pronunciation[i][x])
                        if len(temp_rhythm) >= 2:
                            for y in self.sentence_pronunciation[i][x]:
                                temp_rhythm.append(y)
                        if count == 4:
                            temp_rhythm.append("C")
                            count = 0
                    self.rhythm.append(temp_rhythm[:])
                    temp_rhythm.clear()
            else:
                pass
    
    def getQuarteredScansion(self):
        return self.scansion_quartered

    def getQuarteredDoha(self):
        return self.doha_quartered

    def getPronunciation(self):
        return self.word_pronunciation

    def getRhythm(self):
        return self.rhythm
    

a = "श्रीगुरु चरन सरोज रज निजमनु मुकुरु सुधारि\nबरनउँ रघुबर बिमल जसु जो दायकु फले चारि"
print(Doha(a).getRhythm())
