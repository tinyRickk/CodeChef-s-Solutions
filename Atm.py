while True:
    x=int(input("Enter the amount for withdrawal in $US\n"))
    y=float(input("Enter the amount to be present in account\n"))
    if (x > 0 and x <= 2000 and y > 0 and y <= 2000): 
        if (x<y):
            if ((x%5)==0):
                print("Remaining amount=",float(y-x)-0.5)
            else:
                print("Withdrawal amount is not a multiple of 5")
        else:
            print("Insufficient fund")
        break;
    else:
        print("Try again\n")
    
