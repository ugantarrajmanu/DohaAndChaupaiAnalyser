from Matra import MatraCount, PronunciationDictionary as pd
from Drop import DohaMatraDrop

class Doha:
    def __init__(self, doha):
        doha = doha.split("\n")
        self.doha_quartered = []
        self.rhythm = []
        self.score = 0
        # for doha quartered
        for x in doha:
            a = MatraCount(x).getSentenceQuarter()
            for i in a:
                self.doha_quartered.append(i)

        i = 0

        # for each quarter, find scansion and pronunciation and then
        # find the rhythm of the quarter
        for quarter in self.doha_quartered:
            scansion = MatraCount(quarter).getScansion()

            # check if the quarter is balanced. if balanced then find the pronunciation
            # and after finding the pronunciation, find the rhythm using the pronunciation
            if sum(scansion) == 13 or sum(scansion) == 11:
                pronunciation = pd(quarter, scansion).getPronunciation()
                sentence_pronunciation = []
                for x in pronunciation:
                    for y in x:
                        sentence_pronunciation.append(y)

                first_rhythm = 0
                temp_rhythm = []
                loop = 0
                for x in pronunciation[0]:
                    first_rhythm += sum(x)

                # if kala of the first word is 4 i.e chaukal then append C and 
                # check for further pronunciation to find Chaukal
                if first_rhythm == 4:
                    temp_rhythm.append("C")
                    count = 0
                    
                    # for finding chaukal after the first chaukal is found
                    for x in range(len(pronunciation[0]), len(sentence_pronunciation)):
                        if len(temp_rhythm) < 2:
                            loop = x
                            count += sum(sentence_pronunciation[x])
                            if count == 4:
                                temp_rhythm.append("C")
                                count = 0
                    self.rhythm.append(temp_rhythm[:])
                    temp_rhythm.clear()

                # if first word's kala is trikal then find trikal and dwikal.
                elif first_rhythm == 3:
                    temp_rhythm.append("T")
                    count = 0
                    found3 = False

                    # after first trikal is found, find next trikal and dwikal
                    for x in range(len(pronunciation[0]), len(sentence_pronunciation)):
                        if len(temp_rhythm) < 3:
                            loop = x
                            count += sum(sentence_pronunciation[x])

                            # if next trikal is found and found3 is used to ensure
                            # after 2 trikals are found, the 3rd shoud not be trikal and 
                            # it must be dwikal
                            if count == 3 and not found3:
                                temp_rhythm.append("T")
                                found3 = True
                                count = 0

                            # if two trikal is found then find the dwikal
                            # and found3 is used so that dwikal is found only after 
                            # 2 trikals are found and append it in temp_rhythm
                            elif count == 2 and found3:
                                temp_rhythm.append("D")
                                count = 0
                    self.rhythm.append(temp_rhythm[:])
                    temp_rhythm.clear()
                
                # if first kala is dwikal then find next scansion to make it 4 i.e. 
                # chaukal and then find another chaukal and appending then in
                # temp_rhythm
                elif first_rhythm == 2:
                    count = first_rhythm
                    for x in range(len(pronunciation[0]), len(sentence_pronunciation)):
                        if len(temp_rhythm) < 2:
                            loop = x
                            count += sum(sentence_pronunciation[x])
                        if count == 4:
                            temp_rhythm.append("C")
                            count = 0
                    self.rhythm.append(temp_rhythm[:])
                    temp_rhythm.clear()

                # after all the kalas are found, find the rhyming part
                # i.e. the second half of the quarter
                # if [2, 1, 2] and [2, 1] is found add 1 to score 
                count_rhyme = 0
                temp_rhyme = []

                # loop is starting where the finding of kala ended i.e.
                # ending index after finding rhythm of the quarter
                for x in range(loop+1, len(sentence_pronunciation)):
                    sp = sentence_pronunciation[x]

                    # if sum of pronunciation is greater than 2 then we append it as it is.
                    # and if count_rhyme, which is used when sum of pronunciation is 1, is not
                    # equal to 0 then append it first then append the rest pronunciation.
                    if sum(sp) > 2:
                        if count_rhyme != 0:
                            temp_rhyme.append(count_rhyme)
                        count_rhyme = 0
                        for j in range(len(sp)):
                            temp_rhyme.append(sp[j])
                    
                    # if sum of pronunciation is 2 then append 2 and if previous
                    # and if count_rhyme, which is used when sum of pronunciation is 1, is not
                    # equal to 0 then append it first then append the rest pronunciation.
                    elif sum(sp) == 2:
                        if count_rhyme != 0:
                            temp_rhyme.append(count_rhyme)
                        count_rhyme = 0
                        temp_rhyme.append(2)
                    
                    # if sum of pronunciation is 1 then use count_rhyme to find 2 or 1.
                    elif sum(sp) == 1:
                        count_rhyme += sum(sp)
                        if count_rhyme == 2:
                            temp_rhyme.append(count_rhyme)
                
                # check if the count_rhyme is equal to 0, if not then 
                # then append it to temp_rhyme and also cound_rhyme != 2
                if count_rhyme != 0 and count_rhyme != 2:
                    temp_rhyme.append(count_rhyme)

                # for scoring
                if temp_rhyme == ([2, 1, 2] if i == 0 or i == 2 else [2, 1]):
                    self.score += 1
                
                # for appending in the main rhythm list
                for x in temp_rhyme:
                    self.rhythm[i].append(x)
                i += 1

            # if the sum of scansion is not 13 or 11
            else:
                # get the list of all the possible new scansions using 
                # module - Drop.py
                new_scansions = DohaMatraDrop(quarter, (13 if (i == 0 or i == 2) else 11)).getModifiedScansion()

                # for each scansion in new_scansions check if the rhyming
                # can be found if not then shift to next scansion from new_scanisons
                for new_scansion in new_scansions:

                    # find the pronunciation of the new_scansion
                    pronunciation = pd(quarter, new_scansion).getPronunciation()
                    sentence_pronunciation = []

                    # for filling the sentence_pronunciation
                    for x in pronunciation:
                        for y in x:
                            sentence_pronunciation.append(y)

                    # below this everthing is same as previous code where we have to find
                    # the rhythm or kala of the first half of the quarter, only change is that 
                    # if we dont find suitable kalas i.e. chaukal after chaukal, trikal after first trikal, etc 
                    # then we break the loop and start with a new scansion
                    first_rhythm = 0
                    temp_rhythm = []
                    loop = 0
                    for x in pronunciation[0]:
                        first_rhythm += sum(x)

                    if first_rhythm == 4:
                        temp_rhythm.append("C")
                        count = 0
                        for x in range(len(pronunciation[0]), len(sentence_pronunciation)):
                            if len(temp_rhythm) < 2:
                                loop = x
                                count += sum(sentence_pronunciation[x])
                                if count == 4:
                                    temp_rhythm.append("C")
                                    count = 0
                                
                                # break the inner loop is suitable kala is not found
                                elif count > 4:
                                    break
                        # continue with the new scansion
                        if len(temp_rhythm) != 2:
                            continue
                        if len(temp_rhythm) != 0:
                            self.rhythm.append(temp_rhythm[:])
                        temp_rhythm.clear()

                    elif first_rhythm == 3:
                        temp_rhythm.append("T")
                        count = 0
                        found3 = False
                        for y in range(len(pronunciation[0]), len(sentence_pronunciation)):
                            if len(temp_rhythm) < 3:
                                loop = y
                                count += sum(sentence_pronunciation[y])
                                if count == 3 and not found3:
                                    temp_rhythm.append("T")
                                    found3 = True
                                    count = 0
                                elif count == 2 and found3:
                                    temp_rhythm.append("D")
                                    count = 0
                                # break the inner loop is suitable kala is not found
                                elif (count > 3 and not found3) or count > 2:
                                    break
                        # continue with the new scansion
                        if len(temp_rhythm) != 3:
                            continue
                        if len(temp_rhythm) != 0:
                            self.rhythm.append(temp_rhythm[:])
                        temp_rhythm.clear()

                    elif first_rhythm == 2:
                        count = first_rhythm
                        for y in range(len(pronunciation[0]), len(sentence_pronunciation)):
                            if len(temp_rhythm) < 2:
                                loop = y
                                count += sum(sentence_pronunciation[y])
                            if count == 4:
                                temp_rhythm.append("C")
                                count = 0
                            # break the inner loop is suitable kala is not found
                            elif count > 4:
                                break
                        # continue with the new scansion
                        if len(temp_rhythm) > 4:
                            continue
                        if len(temp_rhythm) != 0:
                            self.rhythm.append(temp_rhythm[:])
                        temp_rhythm.clear()

                    # for last part: 
                    # to find [2, 1, 2] or [1, 2, 2] for 1st and 3rd quarter
                    # and [2, 1] for 2nd and 4th quarter.
                    # the rest is same as the previous code where the matra balanced
                    if len(self.rhythm) != 0 and len(self.rhythm[i]) > 1:
                        count_rhyme = 0
                        temp_rhyme = []
                        for x in range(loop+1, len(sentence_pronunciation)):
                            sp = sentence_pronunciation[x]
                            if sum(sp) > 2:
                                if count_rhyme != 0:
                                    temp_rhyme.append(count_rhyme)
                                count_rhyme = 0
                                for j in range(len(sp)):
                                    temp_rhyme.append(sp[j])

                            elif sum(sp) == 2:
                                if count_rhyme != 0:
                                    temp_rhyme.append(count_rhyme)
                                count_rhyme = 0
                                temp_rhyme.append(2)

                            elif sum(sp) == 1:
                                count_rhyme += sum(sp)
                                if count_rhyme == 2:
                                    temp_rhyme.append(count_rhyme)

                        if count_rhyme != 0 and count_rhyme != 2:
                            temp_rhyme.append(count_rhyme)

                        if temp_rhyme == ([2, 1, 2] if i == 0 or i == 2 else [2, 1]):
                            self.score += 1

                        for x in temp_rhyme:
                            self.rhythm[i].append(x)
                        self.score -= 1
                        i += 1


    def getRhythm(self):
        return self.rhythm
    def getScore(self):
        return self.score/4



a = "एकु छत्र एकु मुकुटमनि सब बरननि पर जोउ\nतुलसी रघुबर नाम के बरन बिराजत दोउ"
print(Doha(a).getScore())