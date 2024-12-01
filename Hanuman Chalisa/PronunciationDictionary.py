from Matra import MatraCount

class PronunciationDictionary:
    def __init__(self, sentence):
        self.word = sentence.split(" ")   #input: - complete line
        self.sentecne = []      # resultant pronunciation of complete sentence, word by word.

        guru = "ाीेैोौूं"
        laghu = "िुृँ"
        swar = "अइउऋआईऊएऐओऔ"
        temp = []       # temporary variable to store the pronunciation inside the word
        count  = 0

        # iterating each word in the word array.
        for word in self.word:
            # for storing pronunciationof each word
            self.word_scansion = []

            # scanion of each word.
            self.matra = MatraCount(word)
            scansion =  self.matra.getScansion()

            i = len(word) - 1
            j = len(scansion) - 1

            # this while loop is iterating from the back or the end of the word.
            while (i >= 0):
                
                # if a laghu matra is found then we check if there is anunashik and if there is any 
                # matra before anunashik then decrease the value of i(initialized as end index of the word)
                # then append the scansion of the laghu swar in temp variable and then append it to word_scansion.
                # and if there is vyanjan without any matra before the laghu is found then we append its scanison
                # in temp variable and then append it to word_scanion
                if(word[i] in laghu):
                    if word[i] == "ँ" and (word[i-1] in laghu or word[i-1] in guru):
                        i -= 1
                    temp.insert(0, scansion[j])
                    self.word_scansion.insert(0, temp[:])
                    temp.clear()
                    j -= 1

                    # it vyanjan without any matra is found at i-2 position we append its scanison to temp and then append 
                    # temp to word_pronunciation
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

                # if guru swar if found then we append its scansion ot then temp and then append temp
                # to word_pronunciation
                elif(word[i] in guru):
                    temp.insert(0, scansion[j])
                    self.word_scansion.insert(0, temp[:])
                    temp.clear()
                    j -= 1
                    if word[i] == "ं":
                        i -= 3 if word[i-1] in laghu or word[i-1] in guru else 2
                    else:
                        i -= 2

                # if a vyanjan is found then its scansion of appended to the temp but donot append in word_pronunciation.
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

                # if a swar if found then append it to temp and temp is appended to word_pronunciation
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

                # if halant is found skip the the loop but if first syllable is half then and the 
                # length of the temp is not zero then append the temp in word_pronunciation.
                elif word[i] == "्":
                    if i-2 < 0 and len(temp) > 0:
                        self.word_scansion.insert(0, temp[:])
                    i -= 2
            self.sentecne.append(self.word_scansion)
            
    # fucntion to return the final pronunciation of each word of the sentence.
    def getPronunciation(self):
        return self.sentecne


# driver code
# a = "जय हनुमान ज्ञान गुन सागर"
# c = []
# b = PronunciationDictionary(a).getPronunciation()
# c.append(b)
# print(a)
# print(b)
