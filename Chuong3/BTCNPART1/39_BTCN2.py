m1=int(input('M1='))
m2=int(input('M2='))
m3=int(input('M3='))
tieuthu=int(input('S='))
if tieuthu<100:
  i=tieuthu*m1
elif tieuthu<150:
    i=m1*100+m2*(tieuthu-100)
else:
    i=m1*100+m2*50+m3*(tieuthu-150)
print('Phai tra=',i,sep='')

    
