a,b=[int(x) for x in input().split()]
if (a and b)<=100:
    if b!=0:
        print (a+b)
        print(a-b)
        print(a*b)
        print(round(a/b,2))
    elif(b==0):   
        print(a+b)
        print(a-b)
        print(a*b)
        print('INF')