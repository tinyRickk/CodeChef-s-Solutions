T = int(input("Enter the no. of test cases\n"))
while(T != 0):
    n= int(input("Enter the no. of movies\n"))
    l_list = []
    r_list = []
    m_list = []
    maxr = 0
    pos = 0
    for i in range(n):
        l_list.append(float(input("Enter the length of movies\n")))
        r_list.append(float(input("Enter the rating of movies\n")))
    for i in range(n):
        m_list.append(l_list[i]*r_list[i])
    lr_max = max(m_list)
    for i in range(len(m_list)):
        if(m_list[i] == lr_max):
            if(r_list[i] > maxr):
                maxr = r_list[i]
                pos = i
    print("Go watch movie")
    print(pos+1)
    T = T-1

    
