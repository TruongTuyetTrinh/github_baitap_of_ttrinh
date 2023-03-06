n=int(input('n='))
i=1
j=1
while i<=n:
    while j>=i and j<i+10 and j<=n:
        print(j,' ',end='')
        j=j+1
    print()
    i+=10
