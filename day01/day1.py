with open("./long.txt", "r") as f:
    total = 0
    for line in f:
        l = line.rstrip();
        if (l == ''):
            print('total: ', total)
            total = 0
        else: 
            total += int(l);