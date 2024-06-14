from Matra import MatraCount, PronunciationDictionary as pd
from MatraDrop import DohaMatraDrop
from termcolor import colored, cprint

class Doha:
    # takes a doha line and then converts it into list
    def __init__(self, doha: str):
        output = {}

        doha = doha.split("\n")

        scansion_quartered =  []
        doha_quartered = []
        word_pronunciation = []
        sentence_pronunciation = []
        rhythm = []

        for x in doha:
            a = MatraCount(x).getSentenceQuarter()
            for i in a:
                doha_quartered.append(i)
        for x in doha_quartered:
            a = MatraCount(x).getScansion()
            scansion_quartered.append(a[:])
        
        for x in range (0, len(scansion_quartered)):
            a = pd(doha_quartered[x], scansion_quartered[x]).getPronunciation()
            word_pronunciation.append(a)

        for x in word_pronunciation:
            temp = []
            for y in x:
                for z in y:
                    temp.append(z)
            sentence_pronunciation.append(temp[:])
            temp.clear()
        
        for i in range(len(scansion_quartered)):
            if sum(scansion_quartered[i]) == 13 if i == 0 or i == 2 else 11:
                first_rhythm = 0
                temp_rhythm = []
                for x in word_pronunciation[i][0]:
                    first_rhythm += sum(x)
                if first_rhythm == 4:
                    temp_rhythm.append("C")
                    count = 0
                    for x in range(len(word_pronunciation[i][0]), len(sentence_pronunciation[i])):
                        if len(temp_rhythm) < 2:
                            count += sum(sentence_pronunciation[i][x])
                        if len(temp_rhythm) >= 2:
                            for y in sentence_pronunciation[i][x]:
                                temp_rhythm.append(y)
                        if count == 4:
                            temp_rhythm.append("C")
                            count = 0
                    rhythm.append(temp_rhythm[:])
                    temp_rhythm.clear()
                
                elif first_rhythm == 3:
                    temp_rhythm.append("T")
                    count = 0
                    found3 = False
                    for x in range(len(word_pronunciation[i][0]), len(sentence_pronunciation[i])):
                        if len(temp_rhythm) < 3:
                            count += sum(sentence_pronunciation[i][x])
                            if count == 3 and not found3:
                                temp_rhythm.append("T")
                                found3 = True
                                count = 0
                            elif count == 2 and found3:
                                temp_rhythm.append("D")
                                count = 0
                        else:
                            for y in sentence_pronunciation[i][x]:
                                temp_rhythm.append(y)
                    
                    rhythm.append(temp_rhythm[:])
                    temp_rhythm.clear()

                
                elif first_rhythm == 2:
                    count = first_rhythm
                    for x in range(len(word_pronunciation[i][0]), len(sentence_pronunciation[i])):
                        if len(temp_rhythm) < 2:
                            count += sum(sentence_pronunciation[i][x])
                        if len(temp_rhythm) >= 2:
                            for y in sentence_pronunciation[i][x]:
                                temp_rhythm.append(y)
                        if count == 4:
                            temp_rhythm.append("C")
                            count = 0
                    rhythm.append(temp_rhythm[:])
                    temp_rhythm.clear()
            else:
                pass
        print(rhythm)
    
    def getQuarteredScansion(self):
        return scansion_quartered

    def getQuarteredDoha(self):
        return doha_quartered

    def getPronunciation(self):
        return word_pronunciation

    def getQuarteredDoha(self):
        return rhythm
    

a = "श्रीगुरु चरन सरोज रज निजमनु मुकुरु सुधारि\nबरनउँ रघुबर बिमल जसु जो दायकु फल चारि"
Doha(a)