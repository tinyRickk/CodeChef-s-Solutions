Weapons=[]
n= int(input("Enter the no of soldiers\n"))
print("Enter the no of weapons held by each soldier\n")
evencount = 0
oddcount = 0
for i in range(n):
    Weapons.append(input())
for i in range(n):
    if(int(Weapons[i])%2 == 0):
        evencount += 1
    else:
        oddcount += 1
if(evencount > oddcount):
    print("Ready for Battle")
else:
    print("Not ready for Battle")
    
