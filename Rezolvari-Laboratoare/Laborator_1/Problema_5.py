n = int(input("n = "))
if(n<2):
    print("Imposibil")
else:
    maxim_2 = 0
    maxim_1 = int(input())
    n-=1

    while maxim_2 != 0 and n:
        if x != maxim_1:
            maxim_1 = x
        n-=1

    if maxim_1 > maxim_2:
        maxim_2,maxim_1 = maxim_1,maxim_2

    for i in range(n):
        x = int(input())
        if x > maxim_2:
            maxim_1 = maxim_2
            maxim_2 = x
        else:
            if x > maxim_1:
                maxim_1 = x

    if maxim_1 > maxim_2:
        maxim_2,maxim_1 = maxim_1,maxim_2

    if maxim_1 == maxim_2:
        print("Imposibil")
    else:
        print(maxim_1,maxim_2)

