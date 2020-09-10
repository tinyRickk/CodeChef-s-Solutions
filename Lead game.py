ap1 = []
rounds = int(input("Enter the no. of rounds played:\n"))
for i in range(0, rounds):
    ap1.append(int(input("Enter the score of player 1 in next round\n")))
ap2 = []
for i in range(0, rounds):
    ap2.append(int(input("Enter the score of player 2 in next round\n")))
aplead = []
apleader = []
for i in range(0, rounds):
    if (ap1[i] > ap2[i]):
        aplead.append(int(ap1[i]-ap2[i]))
        apleader.append(str("player 1"))
    elif (ap2[i] > ap1[i]):
        aplead.append(int(ap2[i]-ap1[i]))
        apleader.append(str("player 2"))
y=aplead.index(max(aplead))
print (apleader[y])
print (max(aplead))
