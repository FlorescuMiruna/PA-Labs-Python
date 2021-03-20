def min_max(*args):
    if len(args) == 0:
        return None
    for x in args:
        if type(x) is not int:
            return None
        if type(x) is int and x <10:
            return None

    return max(args), min(args)


#try:
 #   f = open("Nuumere.txt",'r')
#except FileNotFoundError:
  #  print("Nu exista un fisier cu acest nume")
 #   quit()


    f = open("Numere.txt",'r')

    data = f.read()
    print(data)
    f.close()

    #lst = list(map(int, data.split()))
    lst = [int(x) for x in data.split()]
    print(lst)