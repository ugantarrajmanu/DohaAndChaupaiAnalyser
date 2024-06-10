from PronunciationDictionary import PronunciationDictionary as pd
from termcolor import colored, cprint


with open("HanumanChalisa.txt", "r", encoding="utf8") as file:
    for line in file:
        if line != "\n":
            a = line.strip().split(" ")
            print(line.strip(), end=" --->\t")
            pronun = []
            cprint("[", "red", end=" ", attrs=["bold"])
            for b in a:
                print(b)
                c = pd(b).getPronunciation()
                cprint("[", "green", attrs=["bold"], end=" ")
                for x in c:
                    cprint("[", "yellow", attrs=["bold"], end=" ")
                    for y in x:
                        print(y, end=" ")
                    cprint("]", "yellow", attrs=["bold"], end=" ")
                cprint("]", "green", attrs=["bold"], end=" ")
            cprint("]", "red", attrs=["bold"])
            print("\n")