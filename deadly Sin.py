t = int(input("Enter the number of test cases:"))
while(t>0):
    M = int(input())
    B = int(input())
    while(M != B or M==0 or B==0):
        if(M > B):
            M = M - B
        else:
            B = B - M

    print(M+B)
    t = t-1
