while True:
    n= int(input("enter no of turns\n"))
    x=0
    y=0
    for i in range (1,n+1):
        if i%4==1:
            x = x+(i*10)
        if i%4==2:
            y= y+(i*10)
        if i%4==3:
            x= x-(i*10)
        if i%4==0:
            y=y-(i*10)
    print(x)
    print(y)
