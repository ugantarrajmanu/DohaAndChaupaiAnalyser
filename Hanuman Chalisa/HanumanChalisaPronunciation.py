from PronunciationDictionary import PronunciationDictionary as pd
from termcolor import colored, cprint


with open("C:\ZUgantar\Internship\Hanuman Chalisa\HanumanChalisa.txt", "r", encoding="utf8") as file:
    for line in file:
        if line != "\n":
            a = line.strip().split(" ")
            print(line.strip(), end=" --->\t\n")
            pronun = []
            cprint("[", "red", end="\n", attrs=["bold"])
            for b in a:
                print('\t', b, end=" ")
                c = pd(b).getPronunciation()
                cprint("[", "green", attrs=["bold"], end=" ")
                for x in c:
                    for y in x:
                        cprint("[", "yellow", attrs=["bold"], end=" ")
                        for z in y:
                            print(z, end=" ")
                        cprint("]", "yellow", attrs=["bold"], end=" ")
                cprint("]", "green", attrs=["bold"], end="\n")
            cprint("]", "red", attrs=["bold"])
            print("\n")