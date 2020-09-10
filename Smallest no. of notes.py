rupee = []
cases=int((input("Enter the number of test cases\n")))
count = 0       
for i in range (0, cases):
    rupee.append(int(input("Enter the sum of money:\n")))
    while (rupee[i] >= 100):
        rupee[i] = (rupee[i] - 100)
        count += 1
    while (rupee[i] >= 50):
        rupee[i] = (rupee[i] - 50)
        count += 1
    while (rupee[i] >= 10):
        rupee[i] = (rupee[i] - 10)
        count += 1
    while (rupee[i] >= 5):
        rupee[i] = (rupee[i] - 5)
        count += 1
    while (rupee[i] >= 2):
        rupee[i] = (rupee[i] - 2)
        count += 1
    while (rupee[i] >= 1):
        rupee[i] = (rupee[i] - 1)
        count += 1
    print(count)
    count = 0
