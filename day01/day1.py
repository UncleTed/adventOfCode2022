with open("./long.txt", "r") as f:
    total = 0
    carrying = []
    for line in f:
        l = line.rstrip();
        if (l == ''):
            # print('total: ', total)
            carrying.append(total)
            total = 0
        else: 
            total += int(l);
    
    s = sorted(carrying, reverse=True)
    print (s[0])
    print (s[0] + s[1] + s[2])

    # print(sorted(carrying)[-1], sorted(carrying)[-2], sorted(carrying)[-3])
    # last three are 68787 65169 64085
    #199041 is too high