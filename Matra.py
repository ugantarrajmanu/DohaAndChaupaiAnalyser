class MatraCount:
    def __init__(self, line: str):
        # takes line as a list of string. Ex - ['कबिरा', 'खड़ा', 'बजार', 'में', 'लिए', 'लुकाठी', 'हाथ']
        self.line = line.strip().split(" ")
        self.scansion = []  # stores the scansion of the line
        # stores the scansion per word. Ex - [[1, 1, 2], [1, 2], [1, 2, 1], .....]
        self.word_scansion = []
        self.sentecne_quarter = []
        self.guru = ["ा", "ी", "ू", "े", "ै", "ो", "ौ", "ं"]
        self.laghu = ["ि", "ु", "ृ", "ँ"]

        # these are the variable which are used for finding
        # the position of the anuswar and anunashik
        anuswar = False
        anuswar_index = 0
        chandra = False
        chandra_index = 0
        scansion_iterator = -1

        # in this approach if we find a vyanjan or swar then we add 1 to scansion
        # and if after the vyanjan if there is a laghu swar then we skip it but
        # the a guru swar is after a vyanjan then we change the previously added
        # scansion and then move forward

        # this is the code for finding the scansion of the word
        # this loop iteratest through each word and then
        # iterate each letter and check the check the scansion

        # to iterate each word in the given line
        temp_word_list = []
        count = 0
        found13 = False
        for word in self.line:
            # to find the quarter in words.abs
            temp_word = ""

            # this helps in making the list of scansion of each word
            previous_scansion_iterator = scansion_iterator+1
            # to check if the first halant is found. it is used for finding index of each halant
            first_halant_found = False
            # temporary scansion of each word for appending the scansion of each word.
            temp_word_scansion = []

            # To iterate through each word and the store its matra in a list - scansion. and also in a list
            for letter in word:
                temp_word += letter

                # checking for vyanjan
                if ((letter >= "क" and letter <= "ह") or letter == "अ" or letter == "इ" or letter == "उ" or letter == "ड़" or letter == "ढ़" or letter == "ऋ"):
                    self.scansion.append(1)
                    scansion_iterator += 1

                # checking for swars
                elif (letter == "आ" or letter == "ई" or letter == "ऊ" or letter == "ए" or letter == "ऐ" or letter == "ओ" or letter == "औ" or letter == "अं" or letter == "अः"):
                    self.scansion.append(2)
                    scansion_iterator += 1

                # to check if ht eletter is im laghu list
                elif (letter in self.laghu):

                    # firs we check if the letter is anunashik then we find its postions
                    # if there are two position then we find the first positon using find method
                    # then we fint the next position of anunashik using find method but with a
                    # additonal argument, from where we have to find its position
                    # else we just skip it or reassign the presious scansion woth 1
                    if (letter == "ँ"):
                        if (anuswar == False):
                            chandra_index = word.find("ँ")
                            chandra = True
                        else:
                            chandra_index = word.find("ँ", chandra_index+1, -1)

                        if (word[chandra_index-1] in self.guru):
                            self.scansion[scansion_iterator] = 2
                        else:
                            self.scansion[scansion_iterator] = 1
                    else:
                        self.scansion[scansion_iterator] = 1

                # condition to check if the letter in guru list.
                elif (letter in self.guru):

                    # firs we check if the letter is anuswar then we find its postions
                    # if there are two position then we find the first positon using find method
                    # then we fint the next position of anuswar using find method but with a
                    # additonal argument, from where we have to find its position
                    # else we normally increase the previous scansion
                    # or reassign the presious scansion woth 1
                    if (letter == "ं"):
                        if (anuswar == False):
                            anuswar_index = word.find("ं")
                            anuswar = True
                        else:
                            anuswar_index = word.find("ं", anuswar_index+1, -1)

                        if (anuswar_index-1 > 0 and word[anuswar_index-1] == "ि"):
                            self.scansion[scansion_iterator] = 1
                        else:
                            self.scansion[scansion_iterator] = 2

                    else:
                        self.scansion[scansion_iterator] = 2

                # this is a condition to check when a halant is found.
                # if halatn is fount it checks for its position in the word
                # and then check if no word is before the half word(ardh shabhd)
                # the it ignore the matra of that letter, but if the halant is found in
                # between then we increase the matra of previous scansion by one but
                # there are some exceptions too
                elif (letter == "्"):

                    # to check if halant found is first or not. if first halant fount then we get its index and after that we used first_halant_found boolean variable and find function to find next index of halant
                    halant_index = word.find("्")
                    # this if function is used to check if first word is arrdh then we ignore it.
                    if (halant_index == 1):
                        self.scansion.pop()
                        scansion_iterator -= 1
                        first_halant_found = True
                    else:
                        if (first_halant_found == True):
                            halant_index = word.find("्", halant_index+1)
                        if (halant_index+1 < len(word) and word[halant_index+1] == "ह"):
                            self.scansion.pop()
                            scansion_iterator -= 1
                        elif (self.scansion[scansion_iterator-1] == 1):
                            self.scansion.pop()
                            scansion_iterator -= 1
                            if (scansion_iterator != -1):
                                self.scansion[scansion_iterator] = 2
                        elif (self.scansion[scansion_iterator-1] == 2):
                            self.scansion.pop()
                            scansion_iterator -= 1
        

            for i in range(previous_scansion_iterator, len(self.scansion)):
                temp_word_scansion.append(self.scansion[i])
            self.word_scansion.append(temp_word_scansion[:])

            count += sum(temp_word_scansion)
            temp_word_scansion.clear()
            
            temp_word_list.append(temp_word[:])
            if count >= 13 and not found13:
                self.sentecne_quarter.append(" ".join(temp_word_list[:]))
                temp_word_list.clear()
                found13 = True

        self.sentecne_quarter.append(" ".join(temp_word_list[:]))
        temp_word_list.clear()

    # this funciton returns the scansion of the line
    # Ex: - returns --> [ 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    def getScansion(self):
        return self.scansion

    # this function returns the sum of matras of that line
    # Ex: - returns -->  24
    def getSumOfMatra(self):
        return sum(self.scansion)

    # this function returns the scansion of each word in form of list
    # Ex: - returns --> [[1, 2, 1], [1, 1, 2], [2, 1, 2], [2, 2], [2, 2], [2, 1]]
    def getWordScansion(self):
        return self.word_scansion

    def getSentenceQuarter(self):
        return self.sentecne_quarter

# This is the pronunciation of words
class PronunciationDictionary:
    def __init__(self, sentence, scansion):
        self.word = sentence.split(" ")  # input: - each word
        self.sentecne = []
        
        words_scansion = []
        for x in self.word:
            words_scansion.append(MatraCount(x).getScansion())

        new_word_scansion = []
        l = 0
        for j in range(0, len(words_scansion)):
            temp = []
            for k in range (len(words_scansion[j])):
                temp.append(scansion[l])
                l += 1
            new_word_scansion.append(temp[:])
            temp.clear()

        guru = "ाीेैोौूं"
        laghu = "िुृँ"
        swar = "अइउऋआईऊएऐओऔ"
        temp = []
        count = 0
        word_sc_loop = 0
        for word in self.word:
            self.word_scansion = []
            self.matra = MatraCount(word)
            scansion = new_word_scansion[word_sc_loop]
            word_sc_loop += 1
            i = len(word) - 1
            j = len(scansion) - 1
            while (i >= 0):

                if (word[i] in laghu):
                    if word[i] == "ँ" and (word[i-1] >= "क" and word[i-1] <= "ह") or word[i-1] == "ड़":
                        i -= 1
                        continue
                    elif word[i] == "ँ" and (word[i-1] in laghu or word[i-1] in guru):
                        i -= 1
                    temp.insert(0, scansion[j])
                    self.word_scansion.insert(0, temp[:])
                    temp.clear()
                    j -= 1
                    if (word[i-2] >= "क" and word[i-2] <= "ह" and i-2 >= 0):
                        i -= 2
                        temp.insert(0, scansion[j])
                        self.word_scansion.insert(0, temp[:])
                        temp.clear()
                        j -= 1
                        i -= 1
                        continue
                    elif word[i-2] == "्" and i-4 >= 0:
                        i -= 4
                        if (word[i] >= "क" and word[i] <= "ह"):
                            temp.insert(0, scansion[j])
                            self.word_scansion.insert(0, temp[:])
                            temp.clear()
                            j -= 1
                            i -= 2
                    else:
                        i -= 2

                elif (word[i] in guru):
                    temp.insert(0, scansion[j])
                    self.word_scansion.insert(0, temp[:])
                    temp.clear()
                    j -= 1
                    if word[i] == "ं":
                        i -= 3 if word[i -1] in laghu or word[i-1] in guru else 2
                    else:
                        i -= 2

                elif ((word[i] >= "क" and word[i] <= "ह") or word[i] == "ड़"):
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
                        if (word[i] >= "क" and word[i] <= "ह") or word[i] == "ड़" or word[i] in swar:
                            i -= 1
                        elif (word[i] in laghu or word[i] in guru):
                            i -= 2

                elif word[i] == "्":
                    if i-2 < 0 and len(temp) > 0:
                        self.word_scansion.insert(0, temp[:])
                        temp.clear()
                    i -= 2
            self.sentecne.append(self.word_scansion)

    def getPronunciation(self):
        return self.sentecne


# a = "विहँसत"
# b = PronunciationDictionary(a, MatraCount(a).getScansion()).getPronunciation()
# print(b)
