from Matra import MatraCount as mc

n = 0
file = open("HanumanChalisa.txt", "r", encoding="utf8")
for line in file:
    if (line != "\n"):
        n += 1
        matra = mc(line.split(" "))
        if (sum(matra.getScansion()) < 20 and sum(matra.getScansion()) != 16):
            print("Error in Chaupai:  ", ((n-3)//2), "   line: ", 1 if ((n-3)%2)==0 else 2)
        elif (sum(matra.getScansion()) > 20 and sum(matra.getScansion()) != 24):
            print("Error in Doha:  ", n//2, "   line:  ", 2 if (n%2==0) else 1)
