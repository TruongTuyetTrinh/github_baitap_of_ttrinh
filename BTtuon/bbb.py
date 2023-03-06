a,b,c=[int(x) for x in input ().split()]
if (a and b and c)>0 and(a and b and c)<=10000:
        if a>b and a>c:
            print(a)
        else:
            if b>c:
                print(b)
            else :
                print(c)

