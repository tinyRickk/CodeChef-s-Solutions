
T=[]
t= int(input("Enter the number of integers in Kostya's List\n"))
print("Enter the integer values\n")
for _ in range (t):
    T.append(input())
for i in range(t):
    A = list(map(int, str(T[i])))
    print(A.count(4))
    
    
    
