from Matra import MatraCount

class PronunciationDictionary:
    def __init__(self, sentence):
        self.word = sentence.split(" ")   #imput: - each word
        self.sentecne = []

        guru = "ाीेैोौूं"
        laghu = "िुृँ"
        swar = "अइउऋआईऊएऐओऔ"
        temp = []
        count  = 0
        for word in self.word:
            self.word_scansion = []
            self.matra = MatraCount(word)
            scansion =  self.matra.getScansion()
            i = len(word) - 1
            j = len(scansion) - 1
            while (i >= 0):

                if(word[i] in laghu):
                    if word[i] == "ँ" and (word[i-1] in laghu or word[i-1] in guru):
                        i -= 1
                    temp.insert(0, scansion[j])
                    self.word_scansion.insert(0, temp[:])
                    temp.clear()
                    j -= 1
                    if(word[i-2] >= "क" and word[i-2] <= "ह" and i-2 >= 0):
                        i -= 2
                        temp.insert(0, scansion[j])
                        self.word_scansion.insert(0, temp[:])
                        temp.clear()
                        j -= 1
                        i -= 1
                        continue
                    elif word[i-2] == "्" and i-4 >= 0:
                        i -= 4
                        if(word[i] >= "क" and word[i] <= "ह"):
                            temp.insert(0, scansion[j])
                            self.word_scansion.insert(0, temp[:])
                            temp.clear()
                            j -= 1
                            i -= 2
                    else:
                        i -= 2

                elif(word[i] in guru):
                    temp.insert(0, scansion[j])
                    self.word_scansion.insert(0, temp[:])
                    temp.clear()
                    j -= 1
                    if word[i] == "ं":
                        i -= 3 if word[i-1] in laghu or word[i-1] in guru else 2
                    else:
                        i -= 2

                elif((word[i] >= "क" and word[i] <= "ह") or word[i] == "ड़"):
                    temp.insert(0, scansion[j])
                    if scansion[j] == 2:
                        self.word_scansion.insert(0, temp[:])
                        temp.clear()
                    j -= 1
                    i -= 1
                    if len(temp) == 2:
                        self.word_scansion.insert(0, temp[:])
                        temp.clear()
                        count = 0
                        continue
                    if i < 0 and len(temp) != 0:
                        self.word_scansion.insert(0, temp[:])
                        temp.clear()

                elif (word[i] in swar):
                    temp.insert(0, scansion[j])
                    self.word_scansion.insert(0, temp[:])
                    temp.clear()
                    j -= 1
                    i -= 1
                    if i >= 0:
                        temp.insert(0, scansion[j])
                        self.word_scansion.insert(0, temp[:])
                        temp.clear()
                        j -= 1
                        if(word[i] >= "क" and word[i] <= "ह") or word[i] == "ड़" or word[i] in swar:
                            i -= 1
                        elif (word[i] in laghu or word[i] in guru):
                            i -= 2 

                elif word[i] == "्":
                    if i-2 < 0 and len(temp) > 0:
                        self.word_scansion.insert(0, temp[:])
                    i -= 2
            self.sentecne.append(self.word_scansion)
            

    def getPronunciation(self):
        return self.sentecne



a = "जय हनुमान ज्ञान गुन सागर"
c = []

b = PronunciationDictionary(a).getPronunciation()
c.append(b)
print(b)
