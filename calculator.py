def add(A,B):
    print(A+B)
def mul(A,B):
    print(A*B)
def div(A,B):
    print(float(A/B))
def sub(A,B):
    print(A-B)
A = int(input("Enter the 1st value:"))
B = int(input("Enter the 2nd value:"))
C = input("Enter the symbol,'+'or'-'or'*'or'/':")
if(C == '+'):
    add(A,B)
elif(C == '-'):
    sub(A,B)
elif(C == '*'):
    mul(A,B)
elif(C == '/'):
    div(A,B)
