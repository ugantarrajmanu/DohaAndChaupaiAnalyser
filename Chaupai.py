import Matra  #for counting the matra and getting the scansion

def chaupaiKala(word_scansion):
    temp = []       #for storing the matra
    kala = []       #for storing the kala value
    first = False   # check if the fisrt kala if 4 and not 3
    for i in range(0, len(word_scansion)):
        if (sum(word_scansion[i]) == 4 and sum(temp) == 0):     # check if the word hase 4 matras
            kala.append("C")
            if (len(kala) == 1):
                first = True
        elif (sum(word_scansion[i]) == 3 and sum(temp) == 0 and first == True):     #check if word has 3 matras
            kala.append("T")
        else:
            for j in range (0, len(word_scansion[i])):
                temp.append(word_scansion[i][j])
                T_count = 0
                if (sum(temp) > 4):
                    popped = temp.pop()
                    if (sum(temp) == 3 and T_count <= 2):
                        kala.append("T")
                        T_count += 1
                        if (T_count == 2):
                            T_count = 0
                    elif (sum(temp) == 4 and T_count == 0):
                        kala.append("C")

                    temp.clear()
                    temp.append(popped)
    if (sum(temp) == 4):
        kala.append("C")
    elif(sum(temp) == 2):
        kala.append("D")
        temp.clear()
    return kala
            

chaupai = ["छाता छाता कैसा छाता", "बादल जैसा काला छाता", "आरे बादल काले बादल", "गर्मी दूर भगा रे बादल"]
for i in range(0, 3, 2):
    for j in range (i, i+2):
        print(chaupai[j], end=" | ")
    print()
for i in range (4):
    a = Matra.MatraCount(chaupai[i].split(" "))
    print(chaupaiKala(a.getWordScansion()))    