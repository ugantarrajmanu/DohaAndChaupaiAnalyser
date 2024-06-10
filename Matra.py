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
        self.word = sentence.split(" ")  # imput: - each word
        self.sentecne = []

        guru = "ाीेैोौूं"
        laghu = "िुृँ"
        swar = "अइउऋआईऊएऐओऔ"
        temp = []
        count = 0
        for word in self.word:
            self.word_scansion = []
            self.matra = MatraCount(word)
            scansion = self.matra.getScansion()
            i = len(word) - 1
            j = len(scansion) - 1
            while (i >= 0):

                if (word[i] in laghu):
                    if word[i] == "ँ" and (word[i-1] in laghu or word[i-1] in guru):
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
                    i -= 2
            self.sentecne.append(self.word_scansion)

    def getPronunciation(self):
        return self.sentecne


class DohaRhythm(MatraCount):
    pass


# This is for clountin kala in a given Doha
class Doha(MatraCount):
    def __init__(self, doha_line):
        super().__init__(doha_line)
        self.kala = []
        self.scansion_quarters = []
        self.word_scansion_quarter = []

    # this funciton coiunts the kala of the given lines of doha respectively,
    # first we check if the word is forming a chaukal or trikal
    # if the first word is forming a chaukal then we append "C", "C" tp quarter_kala list
    # but if the first word has trikal then we append "T", "T", "D"
    # but if no chaukal or trikal is found then we add each matra in a varible count to check
    # for trikala or chaukala, and if trikala or cahukal is found and we append in quarter kala accordingly.
    def countingKala(self, line):
        quarter_kala = []
        kala_counter = 0
        found = False

        # This loop iterates through scansion of each word and then check for
        # chaukal and trikal as mentioned above
        for matra_in_word in line:

            # to check if fist word is chaukal or the sum of first and second word is chaukal or not
            if ((sum(matra_in_word) == 4 or (kala_counter+sum(matra_in_word)) == 4) and found == False):
                quarter_kala.append("C")
                quarter_kala.append("C")
                found = True
                break

            # check if the first word is trikal
            elif (sum(matra_in_word) == 3 and found == False):
                quarter_kala.append("T")
                quarter_kala.append("T")
                quarter_kala.append("D")
                break

            #  if not trikal found in first word then we go for adding
            elif (found == False):
                for matra in matra_in_word:
                    kala_counter += matra
                    if (kala_counter == 4):
                        quarter_kala.append("C")
                        quarter_kala.append("C")
                        break
                    elif (kala_counter == 3):
                        quarter_kala.append("T")
                        quarter_kala.append("T")
                        quarter_kala.append("D")
                        break
        iterator = 0
        total_count = 0
        for word in line:
            for letter in word:
                if (total_count < 8):
                    total_count += letter
                    iterator += 1
                else:
                    quarter_kala.append(letter)
                    iterator += 1
                    total_count += letter
        return quarter_kala

    def breakScansion(self):
        count = 0
        temp = []
        for i in range(len(self.word_scansion)-1, -1, -1):
            if (count < 11):
                count += sum(self.word_scansion[i])
                temp.insert(0, self.word_scansion[i])
                if (count == 11):
                    self.word_scansion_quarter.append(temp[:])
                    temp.clear()
            elif (count >= 11):
                temp.insert(0, self.word_scansion[i])
                count += sum(self.word_scansion[i])
        self.word_scansion_quarter.insert(0, temp[:])
        return self.word_scansion_quarter

    def getKala(self):
        for quarter in self.breakScansion():
            x = self.countingKala(quarter)
            self.kala.append(x[:])

        return self.kala

    def getQuarter(self):
        return self.breakScansion()


class Chaupai(MatraCount):
    def __init__(self, chaupai_line):
        super().__init__(chaupai_line)
        self.chaupai_quarters = []
        self.chaupai_quarters_kala = []

        sum_of_word = 0
        quarter = []
        for word in self.word_scansion:
            if (sum_of_word < 16):
                sum_of_word += sum(word)
                quarter.append(word)
                if (sum_of_word == 16):
                    self.chaupai_quarters.append(quarter[:])
                    quarter.clear()
            else:
                quarter.append(word)
        self.chaupai_quarters.append(quarter)

    def findingKala(self):
        kala_quarter = []
        count = 0
        t_count = 0
        if (self.word_scansion[0] != [1, 2, 1] or self.word_scansion[0] != [2, 2, 1]):
            for word in self.word_scansion:
                if (sum(word) == 4 and count == 0):
                    kala_quarter.append("C")
                    # print("1", kala_quarter)
                elif (sum(word) == 3 and count == 0):
                    t_count += 1
                    kala_quarter.append("T")
                    # print("2", kala_quarter)
                else:
                    for letter in word:
                        count += letter
                        # print(letter, count)
                        if (count == 4):
                            kala_quarter.append("C")
                            # print("3", kala_quarter)
                            count = 0
                        elif (len(kala_quarter) != 0):
                            if (count == 4):
                                kala_quarter.append("C")
                                # print("4", kala_quarter)
                                count == 0
                            elif (count == 3 and t_count < 2):
                                kala_quarter.append("T")
                                # print("5", kala_quarter)
                                t_count += 1
                                count == 0
            # print(count)
            if (count == 2):
                kala_quarter.append("D")
            self.chaupai_quarters_kala.append(kala_quarter[:])

        return self.chaupai_quarters_kala

    def getChaupaiScansion(self):
        return self.word_scansion

    def getChaupaiKala(self):
        return self.findingKala()

# a = "तुलसी रघुबर नाम के बरन बिराजत दोउ"
# b = MatraCount(a).getSentenceQuarter()
# print(b)
