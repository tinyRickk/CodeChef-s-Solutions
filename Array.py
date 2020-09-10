from array import *
n=int(input("Enter the No. of rounds\n"))
for i in range(n):
    print("Enter the score for round",i)
    for j in range(2):
        arr[i][j]=int(input("Enter the score for player"))
for i in range(n):
    print("\n")
    for j in range(2):
        print(arr[i][j])
        print("\t")
        
        
