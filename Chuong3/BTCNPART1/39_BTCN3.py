x=float(input('x='))
y=float(input('y='))
ch=str(input('Phep toan='))
if ch=='+':
    s=x+y
    print(x,ch,y,'=',s,sep='')
elif ch=='-':
    t=x-y
    print(x,ch,y,'=',t,sep='')
elif ch=='*':
    n=x*y
    print(x,ch,y,'=',n,sep='')
elif ch=='/'and y!=0:
    c=x/y
    print(x,ch,y,'=',c,sep='')
else:
    print('Khong hop le')
    
    