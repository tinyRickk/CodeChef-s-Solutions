import array as arr
while True:
    x=input("Enter number/word to check")
    arr = list(x)
    print(arr)
    n=len(arr)
    a =(arr[ ::-1])
    if(a == arr):
        print("is palindrome")
    else:
        print("is not palindrome")
            
    
    
